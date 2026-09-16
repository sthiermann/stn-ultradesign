#!/usr/bin/env python3
"""Validate schema-2 audit records and report declared coverage, not UX quality.

No application inspection or evidence authentication takes place. Exit 0 means
valid records, 1 invalid records, 2 an unresolved original scope when using
--require-complete. Version 1 is intentionally rejected: migrate and reconcile.
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

STATUSES = {"not-tested", "pass", "fail", "blocked", "not-applicable"}
SEVERITIES = {"critical", "high", "medium", "low"}
MODES = {"full", "scoped", "sample"}
KINDS = {"surface", "component-family", "component-usage", "widget", "state", "transition", "workflow"}
METHODS = {"source", "rendered", "interaction", "assistive-technology", "api-observation"}
RUNTIME_METHODS = METHODS - {"source"}
NA_BASES = {"unreachable-by-design", "feature-absent", "not-supported-by-contract"}
DISCOVERY_SOURCES = {"source", "runtime", "roles-and-flags", "product-docs"}


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def member(value, choices):
    return isinstance(value, str) and value in choices


def text_list(value, allow_empty=False):
    return (isinstance(value, list) and (allow_empty or bool(value))
            and all(nonempty(item) for item in value))


def validate_and_summarize(data):
    errors, gaps = [], []
    if not isinstance(data, dict):
        return {"valid": False, "errors": ["The ledger must be a JSON object."]}
    if type(data.get("schema_version")) is not int or data["schema_version"] != 2:
        return {"valid": False, "errors": ["schema_version must be integer 2. Migrate version 1; do not carry its completion claim forward."]}

    def obj(value, label):
        if isinstance(value, dict):
            return value
        errors.append(f"{label} must be an object.")
        return {}

    def require_text(record, fields, label):
        for field in fields:
            if not nonempty(record.get(field)):
                errors.append(f"{label}.{field} must contain text.")

    def strings(value, label, allow_empty=False):
        if not text_list(value, allow_empty):
            errors.append(f"{label} must be a list of nonempty strings.")
            return []
        if len(set(value)) != len(value):
            errors.append(f"{label} must not contain duplicates.")
        return value

    def records(value, label):
        if not isinstance(value, list):
            errors.append(f"{label} must be a list.")
            return {}
        result = {}
        for i, item in enumerate(value):
            record = obj(item, f"{label}[{i}]")
            identifier = record.get("id")
            if not nonempty(identifier):
                errors.append(f"{label}[{i}].id must contain text.")
            elif identifier in result:
                errors.append(f"Duplicate {label} id: {identifier}")
            else:
                result[identifier] = record
        return result

    scope = obj(data.get("scope"), "scope")
    require_text(scope, ("product", "revision", "environment", "boundary"), "scope")
    for field in ("requested_mode", "audit_mode"):
        if not member(scope.get(field), MODES):
            errors.append(f"scope.{field} must be full, scoped or sample.")
    if not member(scope.get("evidence_level"), {"source", "runtime"}):
        errors.append("scope.evidence_level must be source or runtime.")
    if scope.get("requested_mode") != scope.get("audit_mode") and not nonempty(scope.get("scope_change_approval")):
        errors.append("A mode change needs scope.scope_change_approval referencing actual user agreement.")
    if type(scope.get("inventory_complete")) is not bool:
        errors.append("scope.inventory_complete must be a boolean.")
    discovery_gaps = strings(scope.get("discovery_gaps"), "scope.discovery_gaps", True)
    gaps.extend(f"Discovery: {gap}" for gap in discovery_gaps)
    entities = records(data.get("entities"), "entities")
    contexts = records(data.get("contexts"), "contexts")
    evidence = records(data.get("evidence"), "evidence")
    checks = records(data.get("checks"), "checks")
    findings = records(data.get("findings"), "findings")
    plan = obj(data.get("plan"), "plan")
    obligations = records(plan.get("obligations"), "plan.obligations")
    if type(plan.get("reconciled")) is not bool:
        errors.append("plan.reconciled must be a boolean.")

    for cid, context in contexts.items():
        require_text(context, ("name", "coverage_reason"), f"Context {cid}")
        dimensions = obj(context.get("dimensions"), f"Context {cid}.dimensions")
        require_text(dimensions, ("role", "scope", "state", "layout", "input"), f"Context {cid}.dimensions")
        if any(not nonempty(k) or not nonempty(v) for k, v in dimensions.items()):
            errors.append(f"Context {cid} dimensions must contain text keys and values.")

    for eid, item in evidence.items():
        require_text(item, ("reference", "revision", "environment"), f"Evidence {eid}")
        if not member(item.get("method"), METHODS):
            errors.append(f"Evidence {eid} has an unknown method.")
        if not member(item.get("target"), {"application", "mock", "prototype"}):
            errors.append(f"Evidence {eid}.target must be application, mock or prototype.")
        for cid in strings(item.get("context_ids"), f"Evidence {eid}.context_ids", True):
            if cid not in contexts:
                errors.append(f"Evidence {eid} references unknown context {cid}.")

    def evidence_for(ids, label, context_id=None):
        matches = []
        for eid in strings(ids, label):
            if eid not in evidence:
                errors.append(f"{label} references unknown evidence {eid}.")
                continue
            item = evidence[eid]
            if item.get("revision") != scope.get("revision") or item.get("environment") != scope.get("environment"):
                errors.append(f"{label}: evidence {eid} is from a different revision/environment.")
                continue
            item_contexts = item.get("context_ids")
            if context_id is not None and (not text_list(item_contexts, True) or context_id not in item_contexts):
                errors.append(f"{label}: evidence {eid} does not cover context {context_id}.")
                continue
            matches.append(item)
        return matches

    inventory_sources = obj(scope.get("inventory_sources"), "scope.inventory_sources")
    runtime_discovered = False
    for source in sorted(DISCOVERY_SOURCES):
        entry = obj(inventory_sources.get(source), f"Inventory source {source}")
        status = entry.get("status")
        if not member(status, {"reconciled", "blocked", "not-applicable"}):
            errors.append(f"Inventory source {source} has invalid status.")
        if status in ("blocked", "not-applicable"):
            require_text(entry, ("reason",), f"Inventory source {source}")
        if status == "blocked":
            gaps.append(f"Inventory source {source} is blocked.")
        if status in ("reconciled", "not-applicable"):
            items = evidence_for(entry.get("evidence_ids"), f"Inventory source {source}.evidence_ids")
            if source == "runtime" and status == "reconciled":
                runtime_discovered = any(member(i.get("method"), RUNTIME_METHODS) and i.get("target") == "application" for i in items)
                if not runtime_discovered:
                    gaps.append("Runtime inventory lacks application runtime evidence.")
            if source == "source" and status == "reconciled" and not any(i.get("method") == "source" for i in items):
                errors.append("Reconciled source inventory needs source evidence.")
    if scope.get("inventory_complete") is not True:
        gaps.append("Discovery reconciliation is not complete.")
    if scope.get("evidence_level") == "runtime" and not runtime_discovered:
        gaps.append("Runtime review requires reconciled application navigation evidence.")
    if scope.get("audit_mode") == "full" and scope.get("evidence_level") != "runtime":
        gaps.append("A full frontend audit requires runtime review; source-only work remains partial.")

    excluded = {}

    def entity_ref(record, field, allowed, label):
        identifier = record.get(field)
        target = entities.get(identifier) if nonempty(identifier) else None
        if target is None or not member(target.get("kind"), allowed):
            errors.append(f"{label}.{field} must reference an entity of kind {', '.join(sorted(allowed))}.")

    for eid, entity in entities.items():
        label = f"Entity {eid}"
        require_text(entity, ("name", "location"), label)
        kind = entity.get("kind")
        if not member(kind, KINDS):
            errors.append(f"{label} has unknown kind.")
        if "exclusion" in entity:
            exclusion = obj(entity["exclusion"], f"{label}.exclusion")
            require_text(exclusion, ("reason", "approval_ref"), f"{label}.exclusion")
            excluded[eid] = exclusion
            if scope.get("audit_mode") == "full":
                errors.append("Full mode cannot exclude discovered entities; record an approved scoped/sample mode.")
        if kind in ("component-usage", "widget", "state"):
            entity_ref(entity, "surface_id", {"surface"}, label)
        if kind in ("component-usage", "widget"):
            entity_ref(entity, "family_id", {"component-family"}, label)
        if kind == "transition":
            entity_ref(entity, "from_id", {"surface", "state"}, label)
            entity_ref(entity, "to_id", {"surface", "state"}, label)
            entity_ref(entity, "workflow_id", {"workflow"}, label)
            require_text(entity, ("trigger", "preconditions"), label)
            api = obj(entity.get("api"), f"{label}.api")
            if not member(api.get("kind"), {"none", "read", "write", "job"}):
                errors.append(f"{label}.api.kind must be none, read, write or job.")
            elif api["kind"] == "none":
                require_text(api, ("reason",), f"{label}.api")
            else:
                require_text(api, ("operation", "scope", "outcomes", "persistence"), f"{label}.api")
    for eid, entity in entities.items():
        if entity.get("kind") == "workflow" and eid not in excluded and not any(e.get("kind") == "transition" and e.get("workflow_id") == eid for e in entities.values()):
            gaps.append(f"Workflow {eid} has no recorded transitions.")

    # Context relevance is planned per entity, not a global Cartesian product.
    entity_contexts = plan.get("entity_contexts")
    expected_pairs = set()
    planned_entities = set()
    if not isinstance(entity_contexts, list):
        errors.append("plan.entity_contexts must be a list.")
        entity_contexts = []
    for i, value in enumerate(entity_contexts):
        entry = obj(value, f"plan.entity_contexts[{i}]")
        eid = entry.get("entity_id")
        if not nonempty(eid) or eid not in entities or eid in excluded:
            errors.append(f"plan.entity_contexts[{i}] must reference an included entity.")
            continue
        if eid in planned_entities:
            errors.append(f"Duplicate context plan for entity {eid}.")
        planned_entities.add(eid)
        require_text(entry, ("reason",), f"Context plan {eid}")
        for cid in strings(entry.get("context_ids"), f"Context plan {eid}.context_ids"):
            if cid not in contexts:
                errors.append(f"Context plan {eid} references unknown context {cid}.")
            else:
                expected_pairs.add((eid, cid))
    unplanned_entities = sorted(set(entities) - set(excluded) - planned_entities)
    if unplanned_entities:
        gaps.append("Entities without context plans: " + ", ".join(unplanned_entities))
    unused_contexts = sorted(set(contexts) - {cid for _, cid in expected_pairs})
    if unused_contexts:
        gaps.append("Contexts not assigned to any included entity: " + ", ".join(unused_contexts))
    if plan.get("reconciled") is True:
        evidence_for(plan.get("reconciliation_evidence_ids"), "plan.reconciliation_evidence_ids")
    else:
        gaps.append("The inventory, contexts, graph and obligation plan are not reconciled.")

    pair_obligations = {pair: [] for pair in expected_pairs}
    for oid, obligation in obligations.items():
        require_text(obligation, ("entity_id", "context_id", "question"), f"Obligation {oid}")
        pair = (obligation.get("entity_id"), obligation.get("context_id"))
        if not all(nonempty(v) for v in pair) or pair not in expected_pairs:
            errors.append(f"Obligation {oid} is outside the entity/context plan.")
        else:
            pair_obligations[pair].append(oid)
        methods = strings(obligation.get("required_methods"), f"Obligation {oid}.required_methods")
        if any(m not in METHODS for m in methods):
            errors.append(f"Obligation {oid} has an unknown required method.")

    result_by_obligation = {}
    for check_id, check in checks.items():
        oid = check.get("obligation_id")
        if not nonempty(oid) or oid not in obligations:
            errors.append(f"Check {check_id} references an unknown planned obligation.")
            continue
        if oid in result_by_obligation:
            errors.append(f"Multiple current results for obligation {oid}; retain history outside the current ledger.")
        result_by_obligation[oid] = check
        status = check.get("status")
        if not member(status, STATUSES):
            errors.append(f"Check {check_id} has invalid status.")
        if status in ("blocked", "not-applicable"):
            require_text(check, ("reason",), f"Check {check_id}")
        obligation = obligations[oid]
        if status in ("pass", "fail", "not-applicable"):
            items = evidence_for(check.get("evidence_ids"), f"Check {check_id}.evidence_ids", obligation.get("context_id"))
            if status == "not-applicable":
                if not member(check.get("na_basis"), NA_BASES):
                    errors.append(f"Check {check_id} needs a design/contract na_basis; missing access or tools must be blocked.")
            else:
                provided = {e["method"] for e in items if member(e.get("method"), METHODS) and (e.get("method") == "source" or e.get("target") == "application")}
                required = obligation.get("required_methods")
                if text_list(required) and not set(required).issubset(provided):
                    errors.append(f"Check {check_id} lacks required application evidence methods: {', '.join(sorted(set(required) - provided))}.")
        if status == "fail":
            for fid in strings(check.get("finding_ids"), f"Check {check_id}.finding_ids"):
                if fid not in findings or not text_list(findings[fid].get("check_ids")) or check_id not in findings[fid]["check_ids"]:
                    errors.append(f"Check {check_id} and finding {fid} must link to each other.")

    for fid, finding in findings.items():
        require_text(finding, ("title", "impact", "recommendation", "acceptance"), f"Finding {fid}")
        if not member(finding.get("severity"), SEVERITIES):
            errors.append(f"Finding {fid} has invalid severity.")
        for cid in strings(finding.get("check_ids"), f"Finding {fid}.check_ids"):
            check = checks.get(cid, {})
            links = check.get("finding_ids")
            if check.get("status") != "fail" or not text_list(links) or fid not in links:
                errors.append(f"Finding {fid} must reference a failed check with a reciprocal link: {cid}.")

    counts = Counter()
    for oid in obligations:
        status = result_by_obligation.get(oid, {}).get("status", "not-tested")
        if member(status, STATUSES):
            counts[status] += 1
    pair_complete = {}
    uncovered_pairs = []
    for pair, ids in sorted(pair_obligations.items()):
        active = [oid for oid in ids if result_by_obligation.get(oid, {}).get("status") != "not-applicable"]
        methods = set()
        for oid in active:
            declared = obligations[oid].get("required_methods")
            if text_list(declared):
                methods.update(declared)
        kind = entities[pair[0]].get("kind")
        needed = {"source"} if scope.get("evidence_level") == "source" else (
            {"interaction"} if kind in ("transition", "workflow") else
            {"rendered"} if kind in ("surface", "component-usage", "widget", "state") else set())
        api = entities[pair[0]].get("api")
        if kind == "transition" and isinstance(api, dict) and member(api.get("kind"), {"read", "write", "job"}) and scope.get("evidence_level") == "runtime":
            needed.add("api-observation")
        if not active or not needed.issubset(methods):
            gaps.append(f"Plan lacks applicable {', '.join(sorted(needed)) or 'review'} obligations for {pair[0]} / {pair[1]}.")
        done = bool(active) and needed.issubset(methods) and all(result_by_obligation.get(oid, {}).get("status") in ("pass", "fail") for oid in active)
        pair_complete[pair] = done
        if not done:
            uncovered_pairs.append({"entity_id": pair[0], "context_id": pair[1]})
    if counts["blocked"] or counts["not-tested"]:
        gaps.append("Planned obligations remain blocked or not tested.")
    if not entities or not obligations or not expected_pairs:
        gaps.append("An empty inventory or plan cannot establish completion.")
    applicable = sum(counts[s] for s in ("pass", "fail", "blocked", "not-tested"))
    investigated = counts["pass"] + counts["fail"]
    agreed_complete = not errors and not gaps and not uncovered_pairs and applicable > 0
    full_complete = agreed_complete and scope.get("audit_mode") == "full" and scope.get("evidence_level") == "runtime" and not excluded
    original_full_complete = full_complete and scope.get("requested_mode") == "full"
    entity_coverage = {}
    for kind in sorted(KINDS):
        ids = {eid for eid, e in entities.items() if e.get("kind") == kind and eid not in excluded}
        done = {eid for eid in ids if not errors and any(item == eid for item, _ in expected_pairs) and all(complete for (item, _), complete in pair_complete.items() if item == eid)}
        entity_coverage[kind] = {"included": len(ids), "reviewed": len(done), "excluded": sum(1 for eid in excluded if entities[eid].get("kind") == kind)}
    return {
        "valid": not errors, "errors": errors, "completion_gaps": gaps,
        "audit_mode": scope.get("audit_mode"), "requested_mode": scope.get("requested_mode"),
        "evidence_level": scope.get("evidence_level"), "entities_by_kind": entity_coverage,
        "entities_without_context_plan": unplanned_entities,
        "unresolved_entity_contexts": uncovered_pairs, "excluded_entities": excluded,
        "planned_obligations": len(obligations),
        "checks_by_status": {s: counts[s] for s in sorted(STATUSES)},
        "applicable_obligations": applicable, "investigated_obligations": investigated,
        "planned_check_coverage_percent": round(100 * investigated / applicable, 1) if applicable and not errors else None,
        "findings_by_severity": dict(Counter(f["severity"] for f in findings.values() if member(f.get("severity"), SEVERITIES))),
        "agreed_scope_reviewed": agreed_complete,
        "original_full_scope_reviewed": original_full_complete,
        "all_planned_applicable_checks_pass": agreed_complete and counts["fail"] == 0,
        "original_request_reviewed": original_full_complete if scope.get("requested_mode") == "full" else agreed_complete,
        "limitation": "Self-declared records only. No app inspection, evidence authentication, discovery proof, authorization certification or UX-quality score. Source, runtime and approved samples remain distinct.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path)
    parser.add_argument("--require-complete", action="store_true", help="Exit 2 unless the original requested scope is reviewed; an approved sample never completes an original full audit.")
    args = parser.parse_args(argv)
    try:
        result = validate_and_summarize(json.loads(args.ledger.read_text(encoding="utf-8")))
    except (OSError, ValueError) as error:
        result = {"valid": False, "errors": [str(error)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result["valid"]:
        return 1
    if args.require_complete and not result["original_request_reviewed"]:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
