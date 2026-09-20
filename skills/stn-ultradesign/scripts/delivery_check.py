#!/usr/bin/env python3
"""Check delivery traceability and optionally local evidence-file integrity.

Exit 0: valid records. Exit 1: invalid input. With --require-ready, exit 2:
valid but unresolved delivery. This does not inspect an application, execute
tests, authenticate observations, certify approval, or grade design quality.
"""

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path, PurePosixPath

STAGES = ("concept", "implementation", "verification")
METHODS = {"source", "rendered", "interaction", "assistive-technology", "api-observation"}
STATUSES = {"pass", "fail", "blocked", "not-tested"}
RESULT_STATES = ("pass", "fail", "blocked", "not-tested", "stale", "missing", "invalid")
TARGETS = {"concept", "prototype", "application"}
UNRESOLVED_KINDS = {"decision": "Open decision", "access-blocker": "Access blocker",
                    "verification-gap": "Verification gap"}
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def text(value):
    return isinstance(value, str) and bool(value.strip())


def choice(value, choices):
    return isinstance(value, str) and value in choices


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(",", ":"), allow_nan=False).encode("utf-8")).hexdigest()


def relative_path(value):
    """Portable explicit paths only; no traversal, drive names, URLs or globs."""
    return (text(value) and "\\" not in value and ":" not in value
            and not any(c in value for c in ("\x00", "*", "?", "[", "]"))
            and not PurePosixPath(value).is_absolute()
            and all(part not in ("", ".", "..") for part in value.split("/")))


def _audit_validator(data):
    path = Path(__file__).with_name("audit_coverage.py")
    spec = importlib.util.spec_from_file_location("stn_delivery_audit", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate_and_summarize(data)


def validate_and_summarize(data, *, evidence_root=None, audit=None):
    """Validate a declared model. Files are read only beneath an explicit root."""
    errors, gaps, checked, unchecked = [], [], [], []
    obligation_gaps, run_gaps = {}, {}
    stale_obligations, stale_runs = set(), set()
    matched_methods = {}

    def evidence_gap(message, *, obligation_id=None, run_id=None, stale=False):
        """Retain the same readiness fact for the global and obligation reports."""
        gaps.append(message)
        if obligation_id is not None:
            obligation_gaps.setdefault(obligation_id, []).append(message)
            if stale:
                stale_obligations.add(obligation_id)
        if run_id is not None:
            run_gaps.setdefault(run_id, []).append(message)
            if stale:
                stale_runs.add(run_id)

    def obj(value, label):
        if isinstance(value, dict):
            return value
        errors.append(f"{label} must be an object.")
        return {}

    def strings(value, label, *, empty=False):
        if not isinstance(value, list) or (not empty and not value) or not all(text(v) for v in value):
            errors.append(f"{label} must be a list of nonempty strings.")
            return []
        if len(set(value)) != len(value):
            errors.append(f"{label} must not contain duplicate values.")
        return value

    def fields(record, names, label):
        for name in names:
            if not text(record.get(name)):
                errors.append(f"{label}.{name} must contain text.")

    def records(value, label):
        if not isinstance(value, list):
            errors.append(f"{label} must be a list.")
            return {}
        result = {}
        for index, value in enumerate(value):
            record = obj(value, f"{label}[{index}]")
            identifier = record.get("id")
            if not text(identifier):
                errors.append(f"{label}[{index}].id must contain text.")
            elif identifier in result:
                errors.append(f"Duplicate {label} id: {identifier}.")
            else:
                result[identifier] = record
        return result

    def ref(record, field, items, label):
        identifier = record.get(field)
        if not text(identifier) or identifier not in items:
            errors.append(f"{label}.{field} references an unknown id.")
            return None
        return items[identifier]

    def enum(record, field, choices, label):
        if not choice(record.get(field), choices):
            errors.append(f"{label}.{field} must be one of {', '.join(sorted(choices))}.")

    data = obj(data, "Delivery record")
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        errors.append("schema_version must be integer 1; audit records use a separate schema.")
    scope = obj(data.get("scope"), "scope")
    fields(scope, ("boundary", "contract_revision"), "scope")
    enum(scope, "stage", STAGES, "scope")
    enum(scope, "audit_gate", {"none", "reviewed", "passed"}, "scope")
    if type(scope.get("reconciled")) is not bool:
        errors.append("scope.reconciled must be a boolean.")
    if scope.get("reconciled") is not True:
        gaps.append("Requirements, decisions and affected obligations are not reconciled.")
    scope_gaps = strings(scope.get("open_questions"), "scope.open_questions", empty=True)
    gaps.extend(f"Open decision: {question}" for question in scope_gaps)
    current_stage = STAGES.index(scope["stage"]) if choice(scope.get("stage"), STAGES) else -1

    requirements = records(data.get("requirements"), "requirements")
    decisions = records(data.get("decisions"), "decisions")
    artifacts = records(data.get("artifacts"), "artifacts")
    obligations = records(data.get("obligations"), "obligations")
    runs = records(data.get("runs"), "runs")
    checks = records(data.get("checks"), "checks")
    unresolved_items = records(scope.get("unresolved_items", []), "scope.unresolved_items")
    item_obligations = {}
    item_closure_gaps = {}
    if not requirements:
        gaps.append("An empty requirement register cannot establish readiness.")

    for identifier, decision in decisions.items():
        label = f"Decision {identifier}"
        fields(decision, ("revision", "source_ref", "interpretation"), label)
        enum(decision, "state", {"confirmed", "delegated", "proposed", "unresolved", "superseded"}, label)

    for identifier, item in unresolved_items.items():
        label = f"Unresolved item {identifier}"
        fields(item, ("detail",), label)
        enum(item, "kind", UNRESOLVED_KINDS, label)
        enum(item, "status", {"pending", "resolved"}, label)
        kind, status = item.get("kind"), item.get("status")
        if "resolution_ref" in item or status == "resolved":
            fields(item, ("resolution_ref",), label)
        if kind == "decision":
            decision = ref(item, "decision_id", decisions, label)
            if "obligation_ids" in item:
                errors.append(f"{label}: decision items use decision_id, not obligation_ids.")
            if status == "resolved" and decision and decision.get("state") not in ("confirmed", "delegated"):
                item_closure_gaps[identifier] = ["The linked decision is not confirmed or delegated."]
        elif choice(kind, {"access-blocker", "verification-gap"}):
            ids = strings(item.get("obligation_ids"), f"{label}.obligation_ids")
            item_obligations[identifier] = ids
            for oid in ids:
                if oid not in obligations:
                    errors.append(f"{label}.obligation_ids references unknown obligation {oid}.")
            if "decision_id" in item:
                errors.append(f"{label}: access and verification items use obligation_ids, not decision_id.")
        if status == "pending" and choice(kind, UNRESOLVED_KINDS):
            gaps.append(f"{UNRESOLVED_KINDS[kind]} {identifier}: {item.get('detail')}")

    for identifier, requirement in requirements.items():
        label = f"Requirement {identifier}"
        fields(requirement, ("revision", "source_ref", "outcome"), label)
        enum(requirement, "status", {"active", "retired"}, label)
        decision = ref(requirement, "decision_id", decisions, label)
        stages = strings(requirement.get("required_stages"), f"{label}.required_stages",
                         empty=requirement.get("status") == "retired")
        if any(s not in STAGES for s in stages):
            errors.append(f"{label} declares an unknown required stage.")
        if requirement.get("status") == "retired":
            fields(requirement, ("retirement_ref", "consequences"), label)
            if decision and decision.get("state") not in ("confirmed", "delegated"):
                gaps.append(f"{label} has no confirmed or delegated retirement decision.")
        elif requirement.get("status") == "active":
            if decision and decision.get("state") not in ("confirmed", "delegated"):
                gaps.append(f"{label} has no confirmed or delegated current decision.")
            for stage in stages:
                if not any(o.get("requirement_id") == identifier and o.get("stage") == stage
                           for o in obligations.values()):
                    gaps.append(f"{label} has no planned {stage} obligation.")

    for identifier, artifact in artifacts.items():
        fields(artifact, ("revision", "reference", "environment"), f"Artifact {identifier}")
        enum(artifact, "kind", TARGETS, f"Artifact {identifier}")

    audit_result = None
    audit_obligations, audit_evidence, audit_checks = {}, {}, {}
    audit_entities, audit_contexts = {}, {}
    if audit is not None:
        try:
            audit_result = _audit_validator(audit)
        except (OSError, ValueError, TypeError, KeyError, AttributeError, RecursionError) as exc:
            errors.append(f"Audit record could not be validated: {type(exc).__name__}.")
        if audit_result and not audit_result.get("valid"):
            errors.extend(f"Audit: {e}" for e in audit_result.get("errors", []))
        if audit_result and audit_result.get("valid"):
            audit_obligations = {o["id"]: o for o in audit["plan"]["obligations"]}
            audit_evidence = {e["id"]: e for e in audit["evidence"]}
            audit_checks = {c["obligation_id"]: c for c in audit["checks"]}
            audit_entities = {e["id"]: e for e in audit["entities"]}
            audit_contexts = {c["id"]: c for c in audit["contexts"]}
            if scope.get("audit_gate") == "reviewed" and not audit_result["original_request_reviewed"]:
                gaps.append("The linked audit's original requested scope has not been reviewed.")
            if scope.get("audit_gate") == "passed" and not (
                    audit_result["original_request_reviewed"] and audit_result["all_planned_applicable_checks_pass"]):
                gaps.append("The linked audit is not complete with all planned applicable checks passing.")
    elif scope.get("audit_gate") != "none":
        gaps.append("The declared audit gate needs the existing audit record via --audit.")

    def audit_binding(obligation):
        """Bind linked behavior and planned evidence, not mutable result status."""
        entity_ids, pending = set(), [obligation["entity_id"]]
        while pending:
            identifier = pending.pop()
            if identifier in entity_ids or identifier not in audit_entities:
                continue
            entity_ids.add(identifier)
            entity = audit_entities[identifier]
            for field in ("surface_id", "family_id", "from_id", "to_id", "workflow_id"):
                if text(entity.get(field)):
                    pending.append(entity[field])
        check = audit_checks.get(obligation["id"])
        evidence_ids = check.get("evidence_ids", []) if check else []
        if not isinstance(evidence_ids, list) or not all(text(eid) for eid in evidence_ids):
            evidence_ids = []
        return {"obligation": obligation,
                "context": audit_contexts[obligation["context_id"]],
                "entities": [audit_entities[eid] for eid in sorted(entity_ids)],
                "check_id": check.get("id") if check else None,
                "evidence": [audit_evidence[eid] for eid in sorted(evidence_ids) if eid in audit_evidence]}

    fingerprints = {}
    for identifier, obligation in obligations.items():
        label = f"Obligation {identifier}"
        fields(obligation, ("expected", "failure_example", "context"), label)
        enum(obligation, "stage", STAGES, label)
        requirement = ref(obligation, "requirement_id", requirements, label)
        decision = ref(obligation, "decision_id", decisions, label)
        artifact = ref(obligation, "artifact_id", artifacts, label)
        if requirement and requirement.get("decision_id") != obligation.get("decision_id"):
            errors.append(f"{label} does not use its requirement's current decision.")
        stages = requirement.get("required_stages") if requirement else None
        if isinstance(stages, list) and obligation.get("stage") not in stages:
            errors.append(f"{label} stage is not planned by its requirement.")
        methods = strings(obligation.get("required_methods"), f"{label}.required_methods")
        if any(m not in METHODS for m in methods):
            errors.append(f"{label} declares an unknown evidence method.")
        if obligation.get("stage") in ("implementation", "verification") and artifact and artifact.get("kind") != "application":
            errors.append(f"{label}: prototype/concept evidence cannot establish application implementation or verification.")
        if obligation.get("stage") == "verification" and not any(m != "source" for m in methods):
            errors.append(f"{label}: application verification needs a runtime method.")
        linked_binding = None
        binding_available = "audit_obligation_id" not in obligation
        if "audit_obligation_id" in obligation:
            audit_id = obligation["audit_obligation_id"]
            if not text(audit_id) or audit_id != identifier:
                errors.append(f"{label} must reuse its audit obligation id without renaming it.")
            elif audit is None:
                evidence_gap(f"{label} needs its existing audit record via --audit.", obligation_id=identifier)
            elif audit_id not in audit_obligations:
                errors.append(f"{label} references an unknown audit obligation.")
            else:
                existing = audit_obligations[audit_id]
                linked_binding = audit_binding(existing)
                binding_available = True
                if obligation.get("context") != existing["context_id"]:
                    errors.append(f"{label} must use the existing audit context id.")
                if not set(existing["required_methods"]).issubset(methods):
                    errors.append(f"{label} cannot weaken the existing audit methods.")
                if artifact and (artifact.get("revision") != audit["scope"]["revision"]
                                 or artifact.get("environment") != audit["scope"]["environment"]):
                    errors.append(f"{label} artifact differs from the linked audit revision/environment.")
        if requirement and decision and artifact and binding_available:
            fingerprints[identifier] = digest({
                "requirement": requirement, "decision": decision, "obligation": obligation,
                "artifact": artifact, "contract_revision": scope.get("contract_revision"),
                "audit_binding": linked_binding,
            })

    root = None
    if evidence_root is not None:
        try:
            root = Path(evidence_root).resolve(strict=True)
            if not root.is_dir():
                raise ValueError("not a directory")
        except (OSError, ValueError, RuntimeError):
            errors.append("Evidence root must be an existing accessible directory.")
    for identifier, run in runs.items():
        label = f"Run {identifier}"
        fields(run, ("artifact_revision", "environment", "context", "observed", "reference"), label)
        enum(run, "method", METHODS, label)
        artifact = ref(run, "artifact_id", artifacts, label)
        if artifact and (run.get("artifact_revision") != artifact.get("revision")
                         or run.get("environment") != artifact.get("environment")):
            evidence_gap(f"{label} is stale for its artifact revision/environment.", run_id=identifier, stale=True)
        bindings = obj(run.get("obligation_bindings"), f"{label}.obligation_bindings")
        if not bindings:
            errors.append(f"{label} must bind at least one existing obligation before execution.")
        for oid, binding in bindings.items():
            if oid not in obligations:
                errors.append(f"{label} binds unknown obligation {oid}.")
            elif not isinstance(binding, str) or not SHA256.fullmatch(binding):
                errors.append(f"{label} binding for {oid} must be a lowercase SHA-256 digest.")
            elif binding != fingerprints.get(oid):
                evidence_gap(f"{label} has a stale execution binding for {oid}.",
                             obligation_id=oid, stale=oid in fingerprints)
        run_files = run.get("files")
        if not isinstance(run_files, list):
            errors.append(f"{label}.files must be a list, including [] when unavailable.")
            run_files = []
        seen = set()
        for index, value in enumerate(run_files):
            record = obj(value, f"{label}.files[{index}]")
            file_path, expected_hash = record.get("path"), record.get("sha256")
            if not relative_path(file_path):
                errors.append(f"{label}.files[{index}].path must be a safe relative file path.")
                continue
            if file_path in seen:
                errors.append(f"{label} repeats evidence file {file_path}.")
            seen.add(file_path)
            if not isinstance(expected_hash, str) or not SHA256.fullmatch(expected_hash):
                errors.append(f"{label}.files[{index}].sha256 must be a lowercase SHA-256 digest.")
                continue
            file_id = f"{identifier}:{file_path}"
            if root is None:
                unchecked.append(file_id)
                continue
            try:
                resolved = (root / file_path).resolve(strict=True)
                if not resolved.is_relative_to(root):
                    raise ValueError("path escapes evidence root")
                if not resolved.is_file():
                    raise ValueError("not a regular file")
                actual = hashlib.sha256()
                size = 0
                with resolved.open("rb") as stream:
                    for block in iter(lambda: stream.read(1024 * 1024), b""):
                        actual.update(block)
                        size += len(block)
                if size == 0:
                    evidence_gap(f"Evidence {file_id} is empty and cannot establish a captured observation.", run_id=identifier)
                elif actual.hexdigest() != expected_hash:
                    evidence_gap(f"Evidence {file_id} has changed (SHA-256 mismatch).", run_id=identifier)
                else:
                    checked.append(file_id)
            except (OSError, ValueError, RuntimeError) as exc:
                evidence_gap(f"Evidence {file_id} unavailable or unsafe: {exc}.", run_id=identifier)
        if "audit_evidence_ids" in run:
            evidence_ids = strings(run["audit_evidence_ids"], f"{label}.audit_evidence_ids")
            if audit is None:
                evidence_gap(f"{label} needs its existing audit record via --audit.", run_id=identifier)
            else:
                for eid in evidence_ids:
                    evidence = audit_evidence.get(eid)
                    if not evidence:
                        errors.append(f"{label} references unknown audit evidence {eid}.")
                    elif (evidence["method"] != run.get("method")
                          or evidence["revision"] != run.get("artifact_revision")
                          or evidence["environment"] != run.get("environment")
                          or run.get("context") not in evidence["context_ids"]
                          or not artifact or evidence["target"] != artifact.get("kind")):
                        errors.append(f"{label} does not match its exact audit evidence target/context/method.")

    by_obligation = {}
    for identifier, check in checks.items():
        label = f"Check {identifier}"
        obligation = ref(check, "obligation_id", obligations, label)
        enum(check, "status", STATUSES, label)
        fields(check, ("observed",), label)
        status = check.get("status")
        run_ids = strings(check.get("run_ids"), f"{label}.run_ids", empty=status in ("blocked", "not-tested"))
        if not obligation:
            continue
        oid = check["obligation_id"]
        if oid in by_obligation:
            errors.append(f"Multiple current checks for {oid}; keep history outside this current record.")
        by_obligation[oid] = check
        if not isinstance(check.get("binding_sha256"), str) or not SHA256.fullmatch(check["binding_sha256"]):
            errors.append(f"{label}.binding_sha256 must be a lowercase SHA-256 digest.")
        elif check["binding_sha256"] != fingerprints.get(oid):
            evidence_gap(f"{label} is stale: requirement, decision, obligation, contract or artifact changed.",
                         obligation_id=oid, stale=oid in fingerprints)
        provided = set()
        audit_ids = set()
        for rid in run_ids:
            run = runs.get(rid)
            if run is None:
                errors.append(f"{label} references unknown run {rid}.")
                continue
            artifact = artifacts.get(obligation.get("artifact_id")) if text(obligation.get("artifact_id")) else None
            if (run.get("artifact_id") != obligation.get("artifact_id")
                    or not artifact or run.get("artifact_revision") != artifact.get("revision")
                    or run.get("environment") != artifact.get("environment")
                    or run.get("context") != obligation.get("context")):
                evidence_gap(f"{label} run {rid} does not cover its exact current artifact/context.",
                             obligation_id=oid, stale=True)
                continue
            bindings = run.get("obligation_bindings")
            if not isinstance(bindings, dict) or bindings.get(oid) != fingerprints.get(oid):
                evidence_gap(f"{label} run {rid} was not bound to this current obligation before execution.",
                             obligation_id=oid, stale=oid in fingerprints)
                continue
            if evidence_root is not None and not run.get("files"):
                evidence_gap(f"{label} run {rid} has no local files for the requested integrity check.", obligation_id=oid)
            if choice(run.get("method"), METHODS):
                provided.add(run["method"])
            values = run.get("audit_evidence_ids", [])
            if isinstance(values, list) and all(text(v) for v in values):
                audit_ids.update(values)
        if status in ("pass", "fail"):
            required = obligation.get("required_methods")
            if isinstance(required, list) and all(text(v) for v in required) and not set(required).issubset(provided):
                evidence_gap(f"{label} lacks its required evidence methods for this artifact/context.", obligation_id=oid)
            audit_id = obligation.get("audit_obligation_id")
            if text(audit_id) and audit_id in audit_obligations:
                existing_check = audit_checks.get(audit_id)
                if not existing_check or existing_check.get("status") != status:
                    evidence_gap(f"{label} disagrees with its existing audit result.", obligation_id=oid)
                elif not set(existing_check.get("evidence_ids", [])).issubset(audit_ids):
                    evidence_gap(f"{label} does not bind the existing audit check's evidence ids.", obligation_id=oid)
        matched_methods[oid] = provided

    due, current = [], []
    for identifier, obligation in obligations.items():
        requirement = requirements.get(obligation.get("requirement_id")) if text(obligation.get("requirement_id")) else None
        if requirement and requirement.get("status") == "retired":
            continue
        stage = obligation.get("stage")
        if choice(stage, STAGES) and STAGES.index(stage) <= current_stage:
            due.append(identifier)
            if stage == scope.get("stage"):
                current.append(identifier)
            check = by_obligation.get(identifier)
            if not check or check.get("status") != "pass":
                gaps.append(f"Due obligation {identifier} is {check.get('status') if check else 'not-tested'}.")
    if not due:
        gaps.append("No active obligations are due at this stage; this is not a delivery readiness result.")
    elif not current:
        gaps.append("No active obligations support the claimed current stage; earlier-stage evidence cannot establish it.")

    obligation_results = []
    for identifier, obligation in obligations.items():
        check = by_obligation.get(identifier)
        requirement_id, artifact_id = obligation.get("requirement_id"), obligation.get("artifact_id")
        requirement = requirements.get(requirement_id) if text(requirement_id) else None
        artifact = artifacts.get(artifact_id) if text(artifact_id) else None
        run_ids = check.get("run_ids", []) if check else []
        if not isinstance(run_ids, list) or not all(text(rid) for rid in run_ids):
            run_ids = []
        required = obligation.get("required_methods", [])
        if not isinstance(required, list) or not all(text(method) for method in required):
            required = []
        matched = matched_methods.get(identifier, set())
        missing_methods = sorted(set(required) - matched)
        evidence_gaps = list(obligation_gaps.get(identifier, []))
        for rid in run_ids:
            evidence_gaps.extend(run_gaps.get(rid, []))
        evidence_gaps = list(dict.fromkeys(evidence_gaps))
        recorded = check.get("status") if check else None
        retired = bool(requirement and requirement.get("status") == "retired")
        if errors:
            effective = "invalid"
        elif identifier in stale_obligations or any(rid in stale_runs for rid in run_ids):
            effective = "stale"
        elif check is None:
            effective = "missing"
        elif recorded in ("pass", "fail") and evidence_gaps:
            effective = "blocked"
        else:
            effective = recorded

        if effective == "invalid":
            next_action = {"kind": "repair-record", "instruction": "Resolve the record's validation errors before relying on this result."}
        elif retired:
            next_action = None
        elif effective == "stale":
            next_action = {"kind": "renew-evidence", "instruction": "Review the changed binding or context, then bind and execute this obligation against its current artifact; retain old evidence as history."}
        elif evidence_gaps:
            next_action = {"kind": "resolve-evidence-gap", "instruction": "Resolve this evidence gap before relying on the recorded result.",
                           "gap": evidence_gaps[0]}
        elif effective == "blocked":
            next_action = {"kind": "resolve-blocker", "instruction": "Resolve the recorded blocker, then bind and execute this obligation.",
                           "blocker": check.get("observed")}
        elif effective == "fail":
            next_action = {"kind": "correct-outcome", "instruction": "Correct the observed failure against the expected outcome, then bind and rerun this obligation."}
        elif effective in ("missing", "not-tested"):
            next_action = {"kind": "execute", "instruction": "Record current bindings before executing this obligation with its required methods, then record the actual observation and check."}
        else:
            next_action = None
        if next_action is not None:
            next_action["timing"] = "due" if identifier in due else "not-due"

        obligation_results.append({
            "id": identifier, "requirement_id": requirement_id,
            "requirement_status": requirement.get("status") if requirement else None,
            "stage": obligation.get("stage"), "due": identifier in due,
            "current_stage": identifier in current,
            "recorded_state": recorded, "effective_state": effective,
            "check_id": check.get("id") if check else None,
            "expected": obligation.get("expected"), "observed": check.get("observed") if check else None,
            "artifact": artifact, "context": obligation.get("context"),
            "audit_obligation_id": obligation.get("audit_obligation_id"),
            "methods": {"required": required, "matched": sorted(matched), "missing": missing_methods},
            "evidence": [{"run_id": rid, "method": runs[rid].get("method"),
                          "observed": runs[rid].get("observed"), "reference": runs[rid].get("reference")}
                         for rid in run_ids if rid in runs],
            "evidence_gaps": evidence_gaps, "next_action": next_action,
        })

    unresolved_item_results = []
    results_by_id = {row["id"]: row for row in obligation_results}
    for identifier, item in unresolved_items.items():
        closure_gaps = list(item_closure_gaps.get(identifier, []))
        if item.get("kind") == "verification-gap" and item.get("status") == "resolved":
            for oid in item_obligations.get(identifier, []):
                row = results_by_id.get(oid)
                if row and row["effective_state"] != "pass":
                    closure_gaps.append(f"Obligation {oid} is {row['effective_state']}; current passing evidence is required.")
        gaps.extend(f"Unresolved item {identifier}: {gap}" for gap in closure_gaps)
        effective = "invalid" if errors else "pending" if closure_gaps else item.get("status")
        unresolved_item_results.append({
            "id": identifier, "kind": item.get("kind"), "detail": item.get("detail"),
            "recorded_status": item.get("status"), "effective_status": effective,
            "decision_id": item.get("decision_id"),
            "obligation_ids": item_obligations.get(identifier, []),
            "resolution_ref": item.get("resolution_ref"), "closure_gaps": closure_gaps,
        })

    def progress(rows):
        return {"total": len(rows), "states": {state: sum(row["effective_state"] == state for row in rows)
                                               for state in RESULT_STATES}}

    return {
        "valid": not errors, "ready": not errors and not gaps,
        "stage": scope.get("stage"), "errors": errors, "readiness_gaps": gaps,
        "due_obligations": due, "current_stage_obligations": current,
        "obligation_results": obligation_results,
        "unresolved_item_results": unresolved_item_results,
        "progress": {"all": progress(obligation_results),
                     "due": progress([row for row in obligation_results if row["due"]]),
                     "current_stage": progress([row for row in obligation_results if row["current_stage"]])},
        "binding_fingerprints": fingerprints,
        "file_integrity": {"requested": evidence_root is not None,
                           "checked": checked, "unchecked": unchecked,
                           "runs_without_files": [identifier for identifier, run in runs.items() if run.get("files") == []]},
        "audit": audit_result,
        "limitation": "Readiness concerns this declared model only. File hashes establish byte integrity, not observation truth, test execution, complete discovery, permission, user acceptance or UX quality. Unchecked and absent files remain explicit.",
    }


def load_json(path):
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError(f"Non-finite JSON number: {value}")

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs,
                      parse_constant=reject_constant)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    parser.add_argument("--audit", type=Path, help="Existing schema-2 audit record; ids and current results are reused.")
    parser.add_argument("--evidence-root", type=Path, help="Read only explicitly listed evidence files beneath this directory.")
    parser.add_argument("--require-ready", action="store_true", help="Exit 2 for a valid record with unresolved readiness gaps.")
    parser.add_argument("--fingerprints", action="store_true", help="Print current binding digests; this does not create check results.")
    parser.add_argument("--obligation", action="append", default=[], metavar="ID",
                        help="Show details only for this obligation (repeatable); readiness and counts still cover the entire record.")
    args = parser.parse_args(argv)
    try:
        data = load_json(args.record)
        audit = load_json(args.audit) if args.audit else None
        result = validate_and_summarize(data, evidence_root=args.evidence_root, audit=audit)
        if args.obligation:
            selected = set(args.obligation)
            known = {row["id"] for row in result["obligation_results"]}
            unknown = sorted(selected - known)
            if unknown:
                result["valid"] = result["ready"] = False
                result["errors"].append(f"Unknown obligation id(s): {', '.join(unknown)}.")
            result["obligation_results"] = [row for row in result["obligation_results"] if row["id"] in selected]
    except (OSError, ValueError, TypeError, KeyError, AttributeError, RecursionError, RuntimeError) as exc:
        result = {"valid": False, "ready": False, "errors": [f"Input could not be validated: {exc}"],
                  "binding_fingerprints": {}}
    output = {"valid": result["valid"], "errors": result["errors"],
              "binding_fingerprints": result["binding_fingerprints"]} if args.fingerprints else result
    print(json.dumps(output, ensure_ascii=False, indent=2))
    if not result["valid"]:
        return 1
    return 2 if args.require_ready and not result["ready"] else 0


if __name__ == "__main__":
    sys.exit(main())
