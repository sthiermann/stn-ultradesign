# UD-001 — Outcome-oriented title

Use this for a nontrivial local Markdown ticket under [bounded work items](../references/delivery-workflow.md#execute-bounded-work-items). Reuse existing records where appropriate. This file owns work coordination; linked requirements own the requested behavior and linked evidence owns verification results. A focused fix may keep these fields in one compact record.

For a focused fix, requirement and result links may point to sections in this same file; a parent plan and separate registers are unnecessary when there are no coordination dependencies.

## Assignment

- Kind: decision / concept / implementation / verification:
- Status: queued / ready / in progress / in review / done / blocked:
- Owner and independent reviewer, if available; self-review explicitly identified otherwise:
- Parent plan, dependencies and output/file ownership:
- Requirement, acceptance, capability and decision IDs with authoritative links/revisions:
- Required skill references and existing authorization boundary:

## Outcome and readiness

- User problem and bounded outcome this item delivers:
- Existing capabilities, roles and contexts that must be preserved (links):
- Artifact or decision to produce; permitted scope and shared component dependencies:
- For a decision: material uncertainty, recommendation/basis/tradeoff and actual decision authority:
- For construction: agreed behavior and specification links; meaningful unresolved inputs:
- For verification: integrated artifact/revision and acceptance obligations to exercise:
- Ready to start because / blocked by / independent work that may continue:
- Concrete closure condition for this increment; parent outcomes that stay open:

## Acceptance and execution

Link the precise acceptance definitions rather than inventing a second specification. Each must state the starting condition, action, observable expected outcome and verification method. Cover relevant preservation, error and recovery cases. Identify the stage and applicable contexts; concept simulation does not establish production behavior.

- Acceptance IDs due for this item and where their definitions/results live:
- Work performed and resulting decision or artifact revision:
- Integration and affected consumer checks, including actual component paths and justified variants where relevant:
- Existing evidence/result record, with expected versus observed outcomes, context and discrepancies:

If no verification record exists, use the following small table here; otherwise link the existing one.

| Acceptance ID / current definition link | Artifact revision / context | Expected result reference and actual observation | Evidence / method / reviewer | Pass / fail / blocked / not-tested | Discrepancy and correction / fresh recheck |
| --- | --- | --- | --- | --- | --- |

## Closure or handoff

- Every due acceptance ID accounted for; unresolved, failed or stale checks:
- Decision authority or owner acceptance where actually required:
- Current result: decision resolved / concept demonstrated / implemented / verified, with exact scope:
- Remaining parent obligations, affected dependent items and next action; authoritative index updated:

Close only the evidenced scope. A worker's completion message, a written requirement or an unchanged old screenshot is not verification. Changed requirements or artifacts reopen the affected checks.
