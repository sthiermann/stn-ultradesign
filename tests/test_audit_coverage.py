"""Synthetic behavioral regressions for the original schema-2 audit validator."""

import copy
import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "audit_coverage", ROOT / "skills/stn-ultradesign/scripts/audit_coverage.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def ledger():
    """A finite fictitious UI; no real app data or authenticated evidence."""
    data = {
        "schema_version": 2,
        "scope": {
            "product": "Synthetic settings example", "revision": "fixture-2", "environment": "synthetic-local",
            "requested_mode": "full", "audit_mode": "full", "evidence_level": "runtime",
            "boundary": "This invented one-screen application, its implementations and defined transitions.",
            "scope_change_approval": "", "inventory_complete": True, "discovery_gaps": [],
            "inventory_sources": {
                "source": {"status": "reconciled", "evidence_ids": ["ev.source"]},
                "runtime": {"status": "reconciled", "evidence_ids": ["ev.interaction"]},
                "roles-and-flags": {"status": "reconciled", "evidence_ids": ["ev.source", "ev.interaction"]},
                "product-docs": {"status": "reconciled", "evidence_ids": ["ev.source"]},
            },
        },
        "entities": [
            {"id": "settings", "kind": "surface", "name": "Settings", "location": "/settings"},
            {"id": "button", "kind": "component-family", "name": "Button", "location": "ui/Button"},
            {"id": "save-button", "kind": "component-usage", "name": "Save control", "location": "/settings#save", "surface_id": "settings", "family_id": "button"},
            {"id": "status", "kind": "widget", "name": "Save status widget", "location": "/settings#status", "surface_id": "settings", "family_id": "button"},
            {"id": "saved", "kind": "state", "name": "Saved result", "location": "/settings#saved", "surface_id": "settings"},
            {"id": "edit-settings", "kind": "workflow", "name": "Edit settings", "location": "/settings"},
            {"id": "save-transition", "kind": "transition", "name": "Save settings", "location": "/settings#save", "from_id": "settings", "to_id": "saved", "workflow_id": "edit-settings", "trigger": "Activate save-button", "preconditions": "A valid changed name exists",
             "api": {"kind": "write", "operation": "PATCH /settings", "scope": "Current user's settings", "outcomes": "Success persists; rejection retains input and permits retry", "persistence": "Reload returns the accepted value"}},
        ],
        "contexts": [{"id": "member-desktop", "name": "Only role and supported shell in this synthetic UI",
                      "dimensions": {"role": "member", "scope": "own profile; no tenant model", "state": "changed valid name", "layout": "desktop", "input": "keyboard"},
                      "coverage_reason": "Synthetic contract contains one role, no tenants or flags, and one shell; real apps must enumerate their actual other classes."}],
        "evidence": [{"id": "ev." + method, "method": method, "reference": "synthetic-evidence/" + method + ".md", "revision": "fixture-2", "environment": "synthetic-local", "target": "application", "context_ids": ["member-desktop"]} for method in ("source", "rendered", "interaction", "api-observation")],
        "plan": {"reconciled": True, "reconciliation_evidence_ids": ["ev.source"], "entity_contexts": [], "obligations": []},
        "checks": [], "findings": [],
    }
    for entity in data["entities"]:
        add_plan(data, entity["id"])
    return data


def add_plan(data, entity_id, context_id="member-desktop"):
    entity = next(e for e in data["entities"] if e["id"] == entity_id)
    kind = entity["kind"]
    methods = ["source"] if kind == "component-family" else ["interaction"] if kind in ("workflow", "transition") else ["rendered"]
    if kind == "transition" and entity["api"]["kind"] != "none":
        methods.append("api-observation")
    existing = next((e for e in data["plan"]["entity_contexts"] if e["entity_id"] == entity_id), None)
    if existing:
        existing["context_ids"].append(context_id)
    else:
        data["plan"]["entity_contexts"].append({"entity_id": entity_id, "context_ids": [context_id], "reason": "All implemented behavior classes for this synthetic entity."})
    oid = entity_id + "." + context_id
    data["plan"]["obligations"].append({"id": oid, "entity_id": entity_id, "context_id": context_id, "question": "Does the declared synthetic contract hold?", "required_methods": methods})
    data["checks"].append({"id": "check." + oid, "obligation_id": oid, "status": "pass", "evidence_ids": ["ev." + method for method in methods]})


class CoverageTests(unittest.TestCase):
    def test_complete_synthetic_runtime_plan(self):
        result = MODULE.validate_and_summarize(ledger())
        self.assertTrue(result["valid"], result["errors"])
        self.assertTrue(result["original_full_scope_reviewed"], result["completion_gaps"])
        self.assertTrue(result["all_planned_applicable_checks_pass"])
        self.assertEqual(result["planned_check_coverage_percent"], 100)
        self.assertEqual(result["entities_by_kind"]["transition"], {"included": 1, "reviewed": 1, "excluded": 0})

    def test_v1_cannot_keep_its_green_claim(self):
        data = ledger()
        data["schema_version"] = 1
        self.assertFalse(MODULE.validate_and_summarize(data)["valid"])

    def test_investigated_failure_is_coverage_not_success(self):
        data = ledger()
        check = data["checks"][0]
        check.update(status="fail", finding_ids=["UX-1"])
        data["findings"] = [{"id": "UX-1", "title": "Save fails", "severity": "high", "check_ids": [check["id"]], "impact": "Task blocked", "recommendation": "Repair save", "acceptance": "Save succeeds"}]
        result = MODULE.validate_and_summarize(data)
        self.assertTrue(result["valid"])
        self.assertTrue(result["original_full_scope_reviewed"])
        self.assertFalse(result["all_planned_applicable_checks_pass"])

    def test_blocked_and_missing_results_never_complete(self):
        for status in ("blocked", "not-tested", "missing"):
            with self.subTest(status=status):
                data = ledger()
                if status == "missing":
                    data["checks"].pop()
                else:
                    data["checks"][-1].update(status=status, reason="Role unavailable")
                result = MODULE.validate_and_summarize(data)
                self.assertTrue(result["valid"], result["errors"])
                self.assertFalse(result["original_full_scope_reviewed"])
                self.assertEqual(result["checks_by_status"]["blocked" if status == "blocked" else "not-tested"], 1)

    def test_new_surface_usage_or_transition_stays_open(self):
        for kind in ("surface", "component-usage", "widget", "transition"):
            with self.subTest(kind=kind):
                data = ledger()
                new = copy.deepcopy(next(e for e in data["entities"] if e["kind"] == kind))
                new["id"] = "new-branch"
                data["entities"].append(new)
                result = MODULE.validate_and_summarize(data)
                self.assertTrue(result["valid"], result["errors"])
                self.assertIn("new-branch", result["entities_without_context_plan"])
                self.assertFalse(result["original_full_scope_reviewed"])

    def test_plan_reconciliation_required(self):
        data = ledger()
        data["plan"]["reconciled"] = False
        self.assertFalse(MODULE.validate_and_summarize(data)["agreed_scope_reviewed"])
        data["plan"]["reconciled"] = True
        data["plan"]["reconciliation_evidence_ids"] = []
        self.assertFalse(MODULE.validate_and_summarize(data)["valid"])

    def test_discovery_gaps_and_runtime_inventory_block_completion(self):
        for mutate in (
            lambda d: d["scope"].update(inventory_complete=False),
            lambda d: d["scope"].update(discovery_gaps=["Unknown administrator navigation"]),
            lambda d: d["scope"]["inventory_sources"]["runtime"].update(status="blocked", reason="No browser"),
            lambda d: d["scope"]["inventory_sources"]["runtime"].update(evidence_ids=["ev.source"]),
        ):
            data = ledger()
            mutate(data)
            result = MODULE.validate_and_summarize(data)
            self.assertFalse(result["original_full_scope_reviewed"])

    def test_source_cannot_satisfy_rendered_interaction_or_api(self):
        for kind in ("surface", "transition"):
            data = ledger()
            eid = next(e["id"] for e in data["entities"] if e["kind"] == kind)
            check = next(c for c in data["checks"] if c["obligation_id"].startswith(eid + "."))
            check["evidence_ids"] = ["ev.source"]
            result = MODULE.validate_and_summarize(data)
            self.assertFalse(result["valid"])
            self.assertFalse(result["original_full_scope_reviewed"])
            self.assertIsNone(result["planned_check_coverage_percent"])

    def test_source_only_scope_is_distinct_from_full_runtime(self):
        data = ledger()
        data["scope"].update(evidence_level="source", requested_mode="scoped", audit_mode="scoped")
        data["scope"]["inventory_sources"]["runtime"] = {"status": "not-applicable", "reason": "The requested deliverable is source review only", "evidence_ids": ["ev.source"]}
        for obligation in data["plan"]["obligations"]:
            obligation["required_methods"] = ["source"]
        for check in data["checks"]:
            check["evidence_ids"] = ["ev.source"]
        result = MODULE.validate_and_summarize(data)
        self.assertTrue(result["agreed_scope_reviewed"], result)
        self.assertFalse(result["original_full_scope_reviewed"])
        data["scope"].update(requested_mode="full", audit_mode="full")
        self.assertFalse(MODULE.validate_and_summarize(data)["agreed_scope_reviewed"])

    def test_sample_never_completes_original_full_request(self):
        data = ledger()
        data["scope"].update(audit_mode="sample", scope_change_approval="User agreed to sample in recorded conversation")
        result = MODULE.validate_and_summarize(data)
        self.assertTrue(result["valid"])
        self.assertTrue(result["agreed_scope_reviewed"])
        self.assertFalse(result["original_full_scope_reviewed"])
        self.assertFalse(result["original_request_reviewed"])
        del data["scope"]["scope_change_approval"]
        self.assertFalse(MODULE.validate_and_summarize(data)["valid"])

    def test_missing_credentials_are_not_a_na_basis(self):
        data = ledger()
        data["checks"][0].update(status="not-applicable", reason="No admin credentials", na_basis="missing-access")
        result = MODULE.validate_and_summarize(data)
        self.assertFalse(result["valid"])
        self.assertFalse(result["original_full_scope_reviewed"])

    def test_all_na_entity_stays_visible_and_incomplete(self):
        data = ledger()
        data["checks"][0].update(status="not-applicable", reason="Feature absent", na_basis="feature-absent")
        result = MODULE.validate_and_summarize(data)
        self.assertTrue(result["valid"])
        self.assertFalse(result["agreed_scope_reviewed"])
        self.assertEqual(result["entities_by_kind"]["surface"]["reviewed"], 0)
        self.assertIn({"entity_id": "settings", "context_id": "member-desktop"}, result["unresolved_entity_contexts"])

    def test_actual_optional_na_does_not_block_other_obligations(self):
        data = ledger()
        optional = copy.deepcopy(data["plan"]["obligations"][0])
        optional.update(id="optional-motion", question="Does conditional animation respect reduced motion?")
        data["plan"]["obligations"].append(optional)
        data["checks"].append({"id": "no-motion", "obligation_id": "optional-motion", "status": "not-applicable", "na_basis": "feature-absent", "reason": "No animation in this implementation", "evidence_ids": ["ev.source"]})
        result = MODULE.validate_and_summarize(data)
        self.assertTrue(result["original_full_scope_reviewed"], result)
        self.assertEqual(result["checks_by_status"]["not-applicable"], 1)

    def test_exclusions_require_agreement_and_remain_reported(self):
        data = ledger()
        data["scope"].update(audit_mode="scoped", scope_change_approval="User agreed narrower scope")
        data["entities"].append({"id": "admin", "kind": "surface", "name": "Admin", "location": "/admin", "exclusion": {"reason": "User deferred admin audit", "approval_ref": "Conversation decision A"}})
        result = MODULE.validate_and_summarize(data)
        self.assertTrue(result["agreed_scope_reviewed"], result)
        self.assertIn("admin", result["excluded_entities"])
        self.assertFalse(result["original_full_scope_reviewed"])
        data["scope"]["audit_mode"] = "full"
        self.assertFalse(MODULE.validate_and_summarize(data)["valid"])

    def test_new_context_requires_planned_obligations(self):
        data = ledger()
        context = copy.deepcopy(data["contexts"][0])
        context.update(id="admin-mobile", name="Admin mobile")
        context["dimensions"].update(role="administrator", layout="compact", scope="foreign tenant")
        data["contexts"].append(context)
        data["plan"]["entity_contexts"][0]["context_ids"].append("admin-mobile")
        result = MODULE.validate_and_summarize(data)
        self.assertTrue(result["valid"])
        self.assertFalse(result["original_full_scope_reviewed"])
        self.assertIn({"entity_id": "settings", "context_id": "admin-mobile"}, result["unresolved_entity_contexts"])

    def test_no_global_cartesian_product_required(self):
        data = ledger()
        context = copy.deepcopy(data["contexts"][0])
        context.update(id="compact", name="Compact layout of settings only")
        context["dimensions"].update(layout="compact")
        data["contexts"].append(context)
        for evidence in data["evidence"]:
            evidence["context_ids"].append("compact")
        add_plan(data, "settings", "compact")
        self.assertTrue(MODULE.validate_and_summarize(data)["original_full_scope_reviewed"])

    def test_api_contract_and_observation_are_required(self):
        for field in ("operation", "scope", "outcomes", "persistence"):
            data = ledger()
            del data["entities"][-1]["api"][field]
            self.assertFalse(MODULE.validate_and_summarize(data)["valid"])
        data = ledger()
        data["plan"]["obligations"][-1]["required_methods"] = ["interaction"]
        self.assertFalse(MODULE.validate_and_summarize(data)["original_full_scope_reviewed"])
        data = ledger()
        data["checks"][-1]["evidence_ids"] = ["ev.interaction"]
        self.assertFalse(MODULE.validate_and_summarize(data)["valid"])

    def test_check_without_planned_obligation_is_invalid(self):
        data = ledger()
        data["checks"][0]["obligation_id"] = "invented-after-review"
        self.assertFalse(MODULE.validate_and_summarize(data)["valid"])

    def test_stale_wrong_context_and_mock_evidence_are_not_runtime_proof(self):
        for field, value in (("revision", "old"), ("environment", "other"), ("context_ids", []), ("target", "mock")):
            with self.subTest(field=field):
                data = ledger()
                next(e for e in data["evidence"] if e["method"] == "rendered")[field] = value
                result = MODULE.validate_and_summarize(data)
                self.assertFalse(result["valid"])
                self.assertFalse(result["original_full_scope_reviewed"])

    def test_relational_graph_links_are_checked(self):
        for index, field in ((2, "surface_id"), (2, "family_id"), (-1, "from_id"), (-1, "to_id"), (-1, "workflow_id")):
            data = ledger()
            data["entities"][index][field] = "unknown"
            self.assertFalse(MODULE.validate_and_summarize(data)["valid"])

    def test_duplicate_ids_results_and_unknown_evidence_are_invalid(self):
        for mutate in (
            lambda d: d["checks"].append(copy.deepcopy(d["checks"][0])),
            lambda d: d["checks"].append(dict(d["checks"][0], id="other-result")),
            lambda d: d["evidence"].append(copy.deepcopy(d["evidence"][0])),
            lambda d: d["checks"][0].update(evidence_ids=["unknown"]),
        ):
            data = ledger()
            mutate(data)
            self.assertFalse(MODULE.validate_and_summarize(data)["valid"])

    def test_empty_plan_cannot_complete(self):
        data = ledger()
        data["plan"].update(entity_contexts=[], obligations=[])
        data["checks"] = []
        result = MODULE.validate_and_summarize(data)
        self.assertIsNone(result["planned_check_coverage_percent"])
        self.assertFalse(result["agreed_scope_reviewed"])

    def test_malformed_types_report_errors_not_exceptions(self):
        mutations = [
            lambda d: d.update(scope=[]), lambda d: d.update(entities=[None]),
            lambda d: d["entities"][0].update(kind=[]), lambda d: d["entities"][-1].update(api=[]),
            lambda d: d["entities"][2].update(surface_id={}),
            lambda d: d["checks"][0].update(status=[]), lambda d: d["checks"][0].update(obligation_id={}),
            lambda d: d["checks"][0].update(evidence_ids=[{}]),
            lambda d: d.update(findings=[{"id": "F", "severity": [], "check_ids": {}}]),
            lambda d: d.update(schema_version=True), lambda d: d.update(contexts={}),
            lambda d: d["contexts"][0].update(dimensions=[]), lambda d: d.update(plan=[]),
            lambda d: d["plan"].update(entity_contexts=[None]),
            lambda d: d["plan"]["obligations"][0].update(entity_id={}),
            lambda d: d["plan"]["obligations"][0].update(required_methods={}),
            lambda d: d["evidence"][0].update(method=[]),
            lambda d: d["scope"].update(inventory_sources=[]),
            lambda d: d["scope"]["inventory_sources"]["runtime"].update(status=[]),
        ]
        for index, mutate in enumerate(mutations):
            with self.subTest(index=index):
                data = ledger()
                mutate(data)
                self.assertFalse(MODULE.validate_and_summarize(data)["valid"])
        self.assertFalse(MODULE.validate_and_summarize([])["valid"])

    def test_cli_distinguishes_validity_and_original_scope_completion(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.json"
            for mode, expected in (("full", 0), ("sample", 2)):
                data = ledger()
                data["scope"].update(audit_mode=mode, scope_change_approval="Recorded approval")
                path.write_text(json.dumps(data))
                with redirect_stdout(io.StringIO()):
                    code = MODULE.main([str(path), "--require-complete"])
                self.assertEqual(code, expected)
            path.write_text('{"schema_version": 1}')
            with redirect_stdout(io.StringIO()):
                self.assertEqual(MODULE.main([str(path), "--require-complete"]), 1)


if __name__ == "__main__":
    unittest.main()
