"""Behavioral checks for declared delivery readiness and local evidence integrity."""

import copy
import hashlib
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/stn-ultradesign/scripts/delivery_check.py"
SPEC = importlib.util.spec_from_file_location("delivery_check", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
AUDIT_SPEC = importlib.util.spec_from_file_location("audit_fixture", ROOT / "tests/test_audit_coverage.py")
AUDIT_FIXTURE = importlib.util.module_from_spec(AUDIT_SPEC)
AUDIT_SPEC.loader.exec_module(AUDIT_FIXTURE)


def record():
    """One synthetic keyboard save action, with explicit observed evidence."""
    data = {
        "schema_version": 1,
        "scope": {"boundary": "The settings save action only", "stage": "verification",
                  "contract_revision": "contract-3", "reconciled": True,
                  "open_questions": [], "audit_gate": "none"},
        "requirements": [{"id": "REQ-1", "revision": "r1", "source_ref": "synthetic-request:1",
                          "outcome": "Saving the changed name persists it and confirms the result",
                          "status": "active", "decision_id": "DEC-1", "required_stages": ["verification"]}],
        "decisions": [{"id": "DEC-1", "revision": "d1", "source_ref": "synthetic-answer:1",
                       "interpretation": "Explicit save confirms after persistence", "state": "confirmed"}],
        "artifacts": [{"id": "app", "revision": "build-7", "reference": "synthetic:/settings",
                       "environment": "synthetic-local", "kind": "application"}],
        "obligations": [{"id": "save-keyboard", "requirement_id": "REQ-1", "decision_id": "DEC-1",
                         "artifact_id": "app", "stage": "verification", "context": "member-desktop-keyboard",
                         "expected": "Submit saves the name and announces confirmation",
                         "failure_example": "Success is announced while reload loses the change",
                         "required_methods": ["interaction"]}],
        "runs": [{"id": "run-1", "artifact_id": "app", "artifact_revision": "build-7",
                  "environment": "synthetic-local", "context": "member-desktop-keyboard", "method": "interaction",
                  "observed": "Synthetic fixture saved the name; reload retained it", "reference": "synthetic-report:1",
                  "obligation_bindings": {}, "files": []}],
        "checks": [{"id": "check-1", "obligation_id": "save-keyboard", "status": "pass",
                    "observed": "The synthetic expected outcome was recorded", "run_ids": ["run-1"],
                    "binding_sha256": "0" * 64}],
    }
    bind(data)
    return data


def bind(data, audit=None):
    """Fixture-only simulation of recording bindings BEFORE a new execution."""
    hashes = MODULE.validate_and_summarize(data, audit=audit)["binding_fingerprints"]
    for check in data["checks"]:
        oid = check["obligation_id"]
        check["binding_sha256"] = hashes[oid]
        for rid in check["run_ids"]:
            run = next(r for r in data["runs"] if r["id"] == rid)
            run["obligation_bindings"][oid] = hashes[oid]


def linked_record():
    audit = AUDIT_FIXTURE.ledger()
    data = record()
    oid = "settings.member-desktop"
    data["scope"]["audit_gate"] = "passed"
    data["artifacts"][0]["revision"] = "fixture-2"
    data["obligations"][0].update(id=oid, audit_obligation_id=oid, context="member-desktop", required_methods=["rendered"])
    data["runs"][0].update(artifact_revision="fixture-2", context="member-desktop", method="rendered",
                           audit_evidence_ids=["ev.rendered"], obligation_bindings={})
    data["checks"][0]["obligation_id"] = oid
    bind(data, audit)
    return data, audit


def mixed_record():
    """Independent current outcomes, plus one changed obligation and one absent check."""
    data = record()
    for status in ("fail", "blocked", "not-tested", "stale", "missing"):
        oid = f"save-{status}"
        data["obligations"].append(dict(data["obligations"][0], id=oid))
        if status == "missing":
            continue
        executed = status in ("fail", "stale")
        rid = f"run-{status}"
        if executed:
            run = copy.deepcopy(data["runs"][0])
            run.update(id=rid, obligation_bindings={})
            data["runs"].append(run)
        data["checks"].append(dict(data["checks"][0], id=f"check-{status}", obligation_id=oid,
                                   status="pass" if status == "stale" else status,
                                   observed=f"Synthetic {status} observation", run_ids=[rid] if executed else []))
    bind(data)
    data["obligations"][-2]["expected"] = "A newly changed acceptance outcome"
    return data


class DeliveryTests(unittest.TestCase):
    def test_obligation_progress_preserves_distinct_outcomes_and_next_actions(self):
        data = mixed_record()
        before = copy.deepcopy(data)
        result = MODULE.validate_and_summarize(data)
        self.assertEqual(data, before, "Reporting must not rewrite checks or create execution records")
        self.assertTrue(result["valid"], result["errors"])
        self.assertFalse(result["ready"])
        rows = {row["id"]: row for row in result["obligation_results"]}
        for oid, state, action in (("save-keyboard", "pass", None),
                                    ("save-fail", "fail", "correct-outcome"),
                                    ("save-blocked", "blocked", "resolve-blocker"),
                                    ("save-not-tested", "not-tested", "execute"),
                                    ("save-stale", "stale", "renew-evidence"),
                                    ("save-missing", "missing", "execute")):
            with self.subTest(oid=oid):
                row = rows[oid]
                self.assertEqual(row["effective_state"], state)
                self.assertTrue(row["due"])
                self.assertTrue(row["current_stage"])
                self.assertEqual(row["next_action"]["kind"] if action else row["next_action"], action)
                self.assertEqual(result["progress"]["due"]["states"][state], 1)
        self.assertEqual(result["progress"]["due"]["total"], 6)
        self.assertEqual(rows["save-stale"]["recorded_state"], "pass")
        self.assertIsNone(rows["save-missing"]["recorded_state"])
        self.assertIsNone(rows["save-missing"]["observed"])
        self.assertEqual(rows["save-missing"]["methods"]["missing"], ["interaction"])
        self.assertEqual(rows["save-keyboard"]["expected"], data["obligations"][0]["expected"])
        self.assertEqual(rows["save-keyboard"]["observed"], data["checks"][0]["observed"])
        self.assertEqual(rows["save-keyboard"]["artifact"], data["artifacts"][0])
        self.assertEqual(rows["save-keyboard"]["context"], data["obligations"][0]["context"])
        self.assertEqual(rows["save-keyboard"]["evidence"][0]["reference"], data["runs"][0]["reference"])

    def test_missing_method_does_not_become_an_effective_pass(self):
        data = record()
        data["obligations"][0]["required_methods"].append("rendered")
        bind(data)
        result = MODULE.validate_and_summarize(data)
        row = result["obligation_results"][0]
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(row["recorded_state"], "pass")
        self.assertEqual(row["effective_state"], "blocked")
        self.assertEqual(row["methods"], {"required": ["interaction", "rendered"],
                                         "matched": ["interaction"], "missing": ["rendered"]})
        self.assertIn(row["next_action"]["gap"], result["readiness_gaps"])

    def test_shared_run_keeps_stale_bindings_specific_to_the_changed_obligation(self):
        data = record()
        data["obligations"].append(dict(data["obligations"][0], id="save-second"))
        data["checks"].append(dict(data["checks"][0], id="check-second", obligation_id="save-second"))
        bind(data)
        data["obligations"][1]["expected"] = "A changed second outcome"
        result = MODULE.validate_and_summarize(data)
        rows = {row["id"]: row for row in result["obligation_results"]}
        self.assertFalse(result["ready"])
        self.assertEqual(rows["save-keyboard"]["effective_state"], "pass")
        self.assertEqual(rows["save-keyboard"]["evidence_gaps"], [])
        self.assertEqual(rows["save-second"]["effective_state"], "stale")

    def test_invalid_evidence_fails_closed_in_progress(self):
        for mutation in (lambda d: d["runs"][0].update(method="imagined"),
                         lambda d: d["runs"][0].update(files=[{"path": "../unsafe", "sha256": "0" * 64}]),
                         lambda d: d["checks"][0].update(run_ids=["absent"])):
            data = record()
            mutation(data)
            result = MODULE.validate_and_summarize(data)
            self.assertFalse(result["valid"])
            row = result["obligation_results"][0]
            self.assertEqual(row["recorded_state"], "pass")
            self.assertEqual(row["effective_state"], "invalid")
            self.assertEqual(row["next_action"]["kind"], "repair-record")
            self.assertEqual(result["progress"]["due"]["states"]["pass"], 0)

    def test_complete_declared_record_is_ready_with_unavailable_files_disclosed(self):
        result = MODULE.validate_and_summarize(record())
        self.assertTrue(result["valid"], result["errors"])
        self.assertTrue(result["ready"], result["readiness_gaps"])
        self.assertFalse(result["file_integrity"]["requested"])
        self.assertEqual(result["file_integrity"]["runs_without_files"], ["run-1"])

    def test_empty_register_is_valid_but_not_ready(self):
        data = record()
        for key in ("requirements", "decisions", "artifacts", "obligations", "runs", "checks"):
            data[key] = []
        result = MODULE.validate_and_summarize(data)
        self.assertTrue(result["valid"])
        self.assertFalse(result["ready"])

    def test_unplanned_new_requirement_or_required_stage_reopens_readiness(self):
        for mutation in (
            lambda d: d["requirements"].append(dict(d["requirements"][0], id="REQ-2")),
            lambda d: d["requirements"][0]["required_stages"].append("implementation"),
        ):
            data = record()
            mutation(data)
            self.assertFalse(MODULE.validate_and_summarize(data)["ready"])

    def test_unresolved_decisions_and_unreconciled_scope_remain_open(self):
        for mutation in (
            lambda d: d["scope"].update(reconciled=False),
            lambda d: d["scope"].update(open_questions=["Who sees the save result?"]),
            lambda d: d["decisions"][0].update(state="proposed"),
            lambda d: d["decisions"][0].update(state="unresolved"),
        ):
            data = record()
            mutation(data)
            bind(data)
            result = MODULE.validate_and_summarize(data)
            self.assertTrue(result["valid"], result["errors"])
            self.assertFalse(result["ready"])

    def test_missing_failed_blocked_and_untested_checks_stay_open(self):
        for status in ("missing", "fail", "blocked", "not-tested"):
            data = record()
            if status == "missing":
                data["checks"] = []
            else:
                data["checks"][0]["status"] = status
            result = MODULE.validate_and_summarize(data)
            self.assertTrue(result["valid"], result["errors"])
            self.assertFalse(result["ready"])

    def test_future_stage_is_planned_without_requiring_future_execution(self):
        data = record()
        data["scope"]["stage"] = "concept"
        data["requirements"][0]["required_stages"] = ["concept", "verification"]
        data["artifacts"].append(dict(data["artifacts"][0], id="proposal", kind="prototype"))
        data["obligations"].append(dict(data["obligations"][0], id="concept-save", stage="concept", artifact_id="proposal"))
        data["runs"][0].update(artifact_id="proposal", obligation_bindings={})
        data["checks"][0].update(obligation_id="concept-save")
        bind(data)
        result = MODULE.validate_and_summarize(data)
        self.assertTrue(result["ready"], result)
        rows = {row["id"]: row for row in result["obligation_results"]}
        self.assertEqual(rows["save-keyboard"]["effective_state"], "missing")
        self.assertFalse(rows["save-keyboard"]["due"])
        self.assertEqual(rows["save-keyboard"]["next_action"]["timing"], "not-due")
        self.assertEqual(result["progress"]["all"]["total"], 2)
        self.assertEqual(result["progress"]["due"]["total"], 1)
        self.assertEqual(result["progress"]["due"]["states"]["pass"], 1)
        data["scope"]["stage"] = "verification"
        result = MODULE.validate_and_summarize(data)
        self.assertFalse(result["ready"])
        self.assertIn("save-keyboard", result["due_obligations"])

    def test_concept_only_evidence_cannot_claim_a_later_delivery_stage(self):
        data = record()
        data["requirements"][0]["required_stages"] = ["concept"]
        data["obligations"][0]["stage"] = "concept"
        data["artifacts"][0]["kind"] = "prototype"
        bind(data)
        for stage in ("implementation", "verification"):
            data["scope"]["stage"] = stage
            result = MODULE.validate_and_summarize(data)
            self.assertTrue(result["valid"], result["errors"])
            self.assertFalse(result["ready"])
            self.assertEqual(result["current_stage_obligations"], [])
        data["scope"]["stage"] = "concept"
        self.assertTrue(MODULE.validate_and_summarize(data)["ready"])

    def test_legitimate_earlier_requirement_does_not_need_repeated_later_stages(self):
        data = record()
        data["requirements"].append(dict(data["requirements"][0], id="concept-direction", required_stages=["concept"]))
        data["artifacts"].append(dict(data["artifacts"][0], id="proposal", kind="prototype"))
        data["obligations"].append(dict(data["obligations"][0], id="concept-proof", requirement_id="concept-direction",
                                          stage="concept", artifact_id="proposal"))
        data["runs"].append(dict(data["runs"][0], id="run-concept", artifact_id="proposal", obligation_bindings={}))
        data["checks"].append(dict(data["checks"][0], id="check-concept", obligation_id="concept-proof", run_ids=["run-concept"]))
        bind(data)
        result = MODULE.validate_and_summarize(data)
        self.assertTrue(result["ready"], result)
        self.assertEqual(result["current_stage_obligations"], ["save-keyboard"])

    def test_changed_requirement_decision_contract_artifact_or_obligation_stales_receipts(self):
        mutations = (
            lambda d: d["requirements"][0].update(revision="r2"),
            lambda d: d["requirements"][0].update(outcome="A changed meaning without a revision bump"),
            lambda d: d["decisions"][0].update(revision="d2"),
            lambda d: d["decisions"][0].update(interpretation="Save a different resource"),
            lambda d: d["scope"].update(contract_revision="contract-4"),
            lambda d: d["artifacts"][0].update(revision="build-8"),
            lambda d: d["obligations"][0].update(expected="A different assertion"),
        )
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                data = record()
                mutation(data)
                result = MODULE.validate_and_summarize(data)
                self.assertTrue(result["valid"], result["errors"])
                self.assertFalse(result["ready"])
                self.assertTrue(any("stale" in gap for gap in result["readiness_gaps"]))

    def test_refreshing_only_check_binding_cannot_launder_an_old_run(self):
        data = record()
        data["requirements"][0]["outcome"] = "Another required effect"
        data["checks"][0]["binding_sha256"] = MODULE.validate_and_summarize(data)["binding_fingerprints"]["save-keyboard"]
        self.assertFalse(MODULE.validate_and_summarize(data)["ready"])

    def test_changed_run_revision_context_or_environment_cannot_close_an_obligation(self):
        for field in ("artifact_revision", "environment", "context"):
            data = record()
            data["runs"][0][field] = "different"
            self.assertFalse(MODULE.validate_and_summarize(data)["ready"])

    def test_prototype_cannot_verify_production_and_source_cannot_prove_interaction(self):
        data = record()
        data["artifacts"][0]["kind"] = "prototype"
        self.assertFalse(MODULE.validate_and_summarize(data)["valid"])
        data = record()
        data["runs"][0]["method"] = "source"
        self.assertFalse(MODULE.validate_and_summarize(data)["ready"])
        data["obligations"][0]["required_methods"] = ["source"]
        self.assertFalse(MODULE.validate_and_summarize(data)["valid"])

    def test_unknown_references_and_duplicate_current_records_are_invalid(self):
        mutations = (
            lambda d: d["requirements"][0].update(decision_id="unknown"),
            lambda d: d["obligations"][0].update(requirement_id="unknown"),
            lambda d: d["obligations"][0].update(artifact_id="unknown"),
            lambda d: d["checks"][0].update(run_ids=["unknown"]),
            lambda d: d["runs"][0].update(artifact_id="unknown"),
            lambda d: d["checks"].append(dict(d["checks"][0], id="check-2")),
            lambda d: d["requirements"].append(copy.deepcopy(d["requirements"][0])),
        )
        for mutation in mutations:
            data = record()
            mutation(data)
            result = MODULE.validate_and_summarize(data)
            self.assertFalse(result["valid"], result)
            self.assertFalse(result["ready"])

    def test_retirement_requires_source_and_consequences_and_is_not_new_evidence(self):
        data = record()
        data["requirements"][0]["status"] = "retired"
        self.assertFalse(MODULE.validate_and_summarize(data)["valid"])
        data["requirements"][0].update(retirement_ref="synthetic-owner:2", consequences="Save is removed at explicit request")
        data["runs"], data["checks"] = [], []
        result = MODULE.validate_and_summarize(data)
        self.assertTrue(result["valid"], result["errors"])
        self.assertFalse(result["ready"])

    def test_fingerprint_is_stable_across_object_key_order(self):
        data = record()
        reordered = json.loads(json.dumps(data, sort_keys=True))
        self.assertEqual(MODULE.validate_and_summarize(data)["binding_fingerprints"],
                         MODULE.validate_and_summarize(reordered)["binding_fingerprints"])

    def test_proposed_retirement_cannot_hide_another_requested_outcome(self):
        data = record()
        data["decisions"].append(dict(data["decisions"][0], id="DEC-2", state="proposed"))
        data["requirements"].append(dict(data["requirements"][0], id="REQ-2", status="retired",
                                          decision_id="DEC-2", required_stages=[],
                                          retirement_ref="Unaccepted proposal", consequences="Outcome removed"))
        result = MODULE.validate_and_summarize(data)
        self.assertTrue(result["valid"], result["errors"])
        self.assertFalse(result["ready"])

    def test_local_files_checked_changed_missing_and_unchecked_are_distinct(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            evidence = root / "result.txt"
            evidence.write_text("observed", encoding="utf-8")
            data = record()
            data["runs"][0]["files"] = [{"path": "result.txt", "sha256": hashlib.sha256(evidence.read_bytes()).hexdigest()}]
            unchecked = MODULE.validate_and_summarize(data)
            self.assertTrue(unchecked["ready"])
            self.assertEqual(unchecked["file_integrity"]["unchecked"], ["run-1:result.txt"])
            checked = MODULE.validate_and_summarize(data, evidence_root=root)
            self.assertTrue(checked["ready"], checked)
            self.assertEqual(checked["file_integrity"]["checked"], ["run-1:result.txt"])
            self.assertEqual(unchecked["obligation_results"][0]["effective_state"], "pass")
            self.assertEqual(checked["obligation_results"][0]["effective_state"], "pass")
            evidence.write_text("changed", encoding="utf-8")
            changed = MODULE.validate_and_summarize(data, evidence_root=root)
            self.assertFalse(changed["ready"])
            self.assertEqual(changed["obligation_results"][0]["effective_state"], "blocked")
            self.assertIn("SHA-256 mismatch", changed["obligation_results"][0]["next_action"]["gap"])
            evidence.unlink()
            missing = MODULE.validate_and_summarize(data, evidence_root=root)
            self.assertFalse(missing["ready"])
            self.assertEqual(missing["obligation_results"][0]["effective_state"], "blocked")
            self.assertIn("unavailable or unsafe", missing["obligation_results"][0]["next_action"]["gap"])

    def test_requested_integrity_requires_files_for_used_runs(self):
        with tempfile.TemporaryDirectory() as directory:
            result = MODULE.validate_and_summarize(record(), evidence_root=directory)
            self.assertTrue(result["valid"])
            self.assertFalse(result["ready"])
            self.assertEqual(result["obligation_results"][0]["effective_state"], "blocked")

    def test_zero_byte_evidence_cannot_satisfy_requested_capture_integrity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "empty.txt").write_bytes(b"")
            data = record()
            data["runs"][0]["files"] = [{"path": "empty.txt", "sha256": hashlib.sha256(b"").hexdigest()}]
            result = MODULE.validate_and_summarize(data, evidence_root=root)
            self.assertTrue(result["valid"], result["errors"])
            self.assertFalse(result["ready"])
            self.assertEqual(result["file_integrity"]["checked"], [])
            self.assertTrue(any("empty" in gap for gap in result["readiness_gaps"]))
            self.assertEqual(result["obligation_results"][0]["effective_state"], "blocked")

    def test_unsafe_paths_rejected_and_symlink_escape_never_read(self):
        for path in ("../secret", "/absolute", "a/../../b", "a\\b", "C:/file", "https://site/a", "a//b", "./a", "*.log"):
            data = record()
            data["runs"][0]["files"] = [{"path": path, "sha256": "0" * 64}]
            self.assertFalse(MODULE.validate_and_summarize(data)["valid"], path)
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            root = parent / "root"
            root.mkdir()
            target = parent / "outside.txt"
            target.write_text("outside", encoding="utf-8")
            (root / "link").symlink_to(target)
            data = record()
            data["runs"][0]["files"] = [{"path": "link", "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}]
            result = MODULE.validate_and_summarize(data, evidence_root=root)
            self.assertFalse(result["ready"])
            self.assertEqual(result["file_integrity"]["checked"], [])

    def test_existing_audit_ids_and_results_are_reused_and_cannot_be_weakened(self):
        data, audit = linked_record()
        result = MODULE.validate_and_summarize(data, audit=audit)
        self.assertTrue(result["valid"], result["errors"])
        self.assertTrue(result["ready"], result["readiness_gaps"])
        self.assertFalse(MODULE.validate_and_summarize(data)["ready"])
        data["runs"][0]["audit_evidence_ids"] = ["ev.interaction"]
        self.assertFalse(MODULE.validate_and_summarize(data, audit=audit)["valid"])

    def test_obligation_progress_retains_audit_binding_and_result_gaps(self):
        data, audit = linked_record()
        row = MODULE.validate_and_summarize(data, audit=audit)["obligation_results"][0]
        self.assertEqual(row["audit_obligation_id"], "settings.member-desktop")
        self.assertEqual(row["effective_state"], "pass")
        absent = MODULE.validate_and_summarize(data)["obligation_results"][0]
        self.assertEqual(absent["effective_state"], "blocked")
        self.assertIn("--audit", absent["next_action"]["gap"])
        audit["checks"][0]["status"] = "not-tested"
        mismatched = MODULE.validate_and_summarize(data, audit=audit)["obligation_results"][0]
        self.assertEqual(mismatched["effective_state"], "blocked")
        self.assertIn("disagrees", mismatched["next_action"]["gap"])
        audit["checks"][0]["status"] = "pass"
        audit["evidence"][1]["reference"] = "another-report.md"
        stale = MODULE.validate_and_summarize(data, audit=audit)["obligation_results"][0]
        self.assertEqual(stale["effective_state"], "stale")

    def test_selected_details_cannot_narrow_readiness_counts_gaps_or_fingerprints(self):
        data = mixed_record()
        full = MODULE.validate_and_summarize(data)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "delivery.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with redirect_stdout(io.StringIO()) as output:
                code = MODULE.main([str(path), "--obligation", "save-keyboard", "--require-ready"])
            selected = json.loads(output.getvalue())
            self.assertEqual(code, 2)
            self.assertEqual([row["id"] for row in selected["obligation_results"]], ["save-keyboard"])
            self.assertEqual(selected["obligation_results"][0]["effective_state"], "pass")
            for key in ("valid", "ready", "progress", "errors", "readiness_gaps", "due_obligations",
                        "current_stage_obligations", "binding_fingerprints", "file_integrity", "audit"):
                self.assertEqual(selected[key], full[key], key)
            with redirect_stdout(io.StringIO()) as output:
                code = MODULE.main([str(path), "--obligation", "save-keyboard", "--obligation", "save-fail",
                                    "--obligation", "save-keyboard"])
            self.assertEqual(code, 0)
            self.assertEqual(len(json.loads(output.getvalue())["obligation_results"]), 2)

    def test_unknown_selection_fails_even_in_fingerprint_mode(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "delivery.json"
            path.write_text(json.dumps(record()), encoding="utf-8")
            for flags in ([], ["--require-ready"], ["--fingerprints"]):
                with redirect_stdout(io.StringIO()) as output:
                    code = MODULE.main([str(path), "--obligation", "absent", *flags])
                result = json.loads(output.getvalue())
                self.assertEqual(code, 1)
                self.assertFalse(result["valid"])
                self.assertIn("Unknown obligation id(s): absent", result["errors"][-1])

    def test_selection_still_checks_unselected_evidence_file_integrity(self):
        data = record()
        data["obligations"].append(dict(data["obligations"][0], id="save-second"))
        data["runs"].append(dict(data["runs"][0], id="run-second", obligation_bindings={}))
        data["checks"].append(dict(data["checks"][0], id="check-second", obligation_id="save-second",
                                   run_ids=["run-second"]))
        bind(data)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = b"Captured observation"
            for index, name in enumerate(("first.txt", "second.txt")):
                (root / name).write_bytes(original)
                data["runs"][index]["files"] = [{"path": name, "sha256": hashlib.sha256(original).hexdigest()}]
            (root / "second.txt").write_text("Changed after capture", encoding="utf-8")
            path = root / "delivery.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with redirect_stdout(io.StringIO()) as output:
                code = MODULE.main([str(path), "--evidence-root", str(root), "--obligation", "save-keyboard", "--require-ready"])
            result = json.loads(output.getvalue())
            self.assertEqual(code, 2)
            self.assertEqual(result["obligation_results"][0]["effective_state"], "pass")
            self.assertEqual(result["progress"]["due"]["states"]["blocked"], 1)
            self.assertTrue(any("run-second:second.txt has changed" in gap for gap in result["readiness_gaps"]))

    def test_audit_meaning_and_evidence_edits_invalidate_bindings_without_revision_bump(self):
        mutations = (
            lambda a: a["plan"]["obligations"][0].update(question="A different outcome"),
            lambda a: a["contexts"][0]["dimensions"].update(role="administrator"),
            lambda a: a["entities"][0].update(name="Another domain object"),
            lambda a: a["evidence"][1].update(reference="different-report.md"),
            lambda a: a["checks"][0].update(id="another-receipt"),
        )
        for mutation in mutations:
            data, audit = linked_record()
            before = MODULE.validate_and_summarize(data, audit=audit)["binding_fingerprints"]
            mutation(audit)
            result = MODULE.validate_and_summarize(data, audit=audit)
            self.assertTrue(result["valid"], result["errors"])
            self.assertFalse(result["ready"])
            self.assertNotEqual(result["binding_fingerprints"], before)

    def test_unrelated_audit_entity_does_not_stale_the_affected_binding(self):
        data, audit = linked_record()
        before = MODULE.validate_and_summarize(data, audit=audit)["binding_fingerprints"]
        audit["entities"][1]["name"] = "Renamed unrelated family"
        result = MODULE.validate_and_summarize(data, audit=audit)
        self.assertTrue(result["ready"], result)
        self.assertEqual(result["binding_fingerprints"], before)

    def test_audit_result_completion_preserves_pre_registered_binding(self):
        data, audit = linked_record()
        before = MODULE.validate_and_summarize(data, audit=audit)["binding_fingerprints"]
        audit["checks"][0]["status"] = "not-tested"
        pending = MODULE.validate_and_summarize(data, audit=audit)
        self.assertFalse(pending["ready"])
        self.assertEqual(pending["binding_fingerprints"], before)
        audit["checks"][0]["status"] = "pass"
        self.assertTrue(MODULE.validate_and_summarize(data, audit=audit)["ready"])

    def test_linked_fingerprint_generation_requires_the_current_audit(self):
        data, audit = linked_record()
        without_audit = MODULE.validate_and_summarize(data)
        self.assertFalse(without_audit["ready"])
        self.assertEqual(without_audit["binding_fingerprints"], {})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "delivery.json"
            audit_path = Path(directory) / "audit.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            audit_path.write_text(json.dumps(audit), encoding="utf-8")
            with redirect_stdout(io.StringIO()) as output:
                code = MODULE.main([str(path), "--fingerprints", "--audit", str(audit_path)])
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(output.getvalue())["binding_fingerprints"],
                             MODULE.validate_and_summarize(data, audit=audit)["binding_fingerprints"])

    def test_completed_audit_with_findings_does_not_imply_conformant_delivery(self):
        data = record()
        audit = AUDIT_FIXTURE.ledger()
        audit["checks"][0].update(status="fail", finding_ids=["UX-1"])
        audit["findings"] = [{"id": "UX-1", "title": "Misleading success", "severity": "high",
                              "check_ids": [audit["checks"][0]["id"]], "impact": "Task fails",
                              "recommendation": "Repair", "acceptance": "Persistence works"}]
        data["scope"]["audit_gate"] = "reviewed"
        self.assertTrue(MODULE.validate_and_summarize(data, audit=audit)["ready"])
        data["scope"]["audit_gate"] = "passed"
        result = MODULE.validate_and_summarize(data, audit=audit)
        self.assertFalse(result["ready"])
        self.assertTrue(result["audit"]["original_request_reviewed"])
        self.assertFalse(result["audit"]["all_planned_applicable_checks_pass"])

    def test_corrupt_field_types_return_diagnostics_without_exceptions(self):
        for name in ("requirements", "decisions", "artifacts", "obligations", "runs", "checks"):
            for malformed in (None, 7, "invalid", {}, [None], [7]):
                data = record()
                data[name] = malformed
                self.assertFalse(MODULE.validate_and_summarize(data)["valid"])
        for array, field in (("requirements", "decision_id"), ("obligations", "requirement_id"),
                             ("runs", "artifact_id"), ("checks", "obligation_id")):
            data = record()
            data[array][0][field] = []
            self.assertFalse(MODULE.validate_and_summarize(data)["valid"])

    def test_cli_valid_vs_ready_exit_codes_and_fingerprints(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "delivery.json"
            data = record()
            data["checks"][0]["status"] = "blocked"
            path.write_text(json.dumps(data), encoding="utf-8")
            for arguments, expected in (([str(path)], 0), ([str(path), "--require-ready"], 2),
                                        ([str(path), "--fingerprints"], 0)):
                with redirect_stdout(io.StringIO()) as output:
                    code = MODULE.main(arguments)
                self.assertEqual(code, expected)
                self.assertTrue(json.loads(output.getvalue())["valid"])
            for raw in ('{"schema_version": 1, "schema_version": 2}', '{"number": NaN}', "{", "null"):
                path.write_text(raw, encoding="utf-8")
                result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertFalse(json.loads(result.stdout)["valid"])
                self.assertNotIn("Traceback", result.stderr)

    def test_template_is_valid_and_honestly_incomplete(self):
        template = ROOT / "skills/stn-ultradesign/assets/delivery.template.json"
        result = MODULE.validate_and_summarize(json.loads(template.read_text(encoding="utf-8")))
        self.assertTrue(result["valid"], result["errors"])
        self.assertFalse(result["ready"])


if __name__ == "__main__":
    unittest.main()
