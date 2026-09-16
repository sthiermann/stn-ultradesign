# Requirement register

Keep this record in the target project, or use its fields in an existing project record. Follow [requirements-conformance.md](../references/requirements-conformance.md). This is the authoritative requirement-to-result trace; link detailed decisions and evidence where they already live. For a focused fix, keep only the needed rows. Recording a proposal, exception or gap does not authorize it or satisfy it.

## Boundary and current basis

- Original request / source references and scope:
- Current authorized scope / exact change or deferral references:
- Register / contract revision and current artifact revision:
- Linked brief, design contract, capability map and audit ledger, where present:
- Known discovery gaps and unresolved dependencies:

## Requirements

Use stable IDs. Preserve source IDs for requests, answers and discovered constraints. Link several sources to one requirement where their meaning is identical; split independently changeable outcomes. Keep historical IDs and exact replacements rather than rewriting the past.

| Requirement ID | Origin type / source ID, reference and version | Authority / decision or delegation scope | Observed basis versus inference | Concrete requirement and intended artifact effect | Decision state / exact replacement and authority if superseded | Affected capability and usage IDs / scope | Acceptance obligation IDs |
| --- | --- | --- | --- | --- | --- | --- | --- |

Decision states: `confirmed`, `delegated`, `proposed`, `unresolved`, `superseded`. Record proposed/rejected disposition where relevant. Preserve the source's important qualifiers, current interpretation and any delegated choice's rationale. Decision state is separate from delivery progress.

## Applicable contexts and obligations

When an audit ledger already holds these records, link its existing entity, context and obligation IDs here. Keep their definitions and results there. Otherwise use the following small tables for the affected scope.

| Context ID / affected usage IDs | Relevant conditions and reachable combinations | Behavior-class or boundary rationale / evidence for equivalence | Inapplicability basis or unresolved gap |
| --- | --- | --- | --- |

| Obligation ID / requirement and decision IDs | Capability/usage IDs and applicable context IDs | Observable result / counterexample that would fail | Due stage and required evidence methods |
| --- | --- | --- | --- |

## Stage evidence

Link existing results rather than copying them. Each evidence reference identifies the artifact, revision, target (concept/prototype/application), environment, context and observed result. Separate observed evidence from inference. Check results use `pass`, `fail`, `blocked` or `not-tested`; inapplicability requires a factual basis in the agreed support/product contract and evidence. A missing required implementation or defect that makes a state unreachable is a failure, not an inapplicable check.

| Requirement / obligation IDs | Concept: artifact, revision, demonstrated scope / gap | Implementation: destination, revision, actual behavior / gap | Verification: current result and evidence per required context/method / gap | Owner assessment or approval reference / exact scope |
| --- | --- | --- | --- | --- |

## Decisions and changes

Link the existing decision queue and change record when they contain these fields. Reuse answers and authorization. A question affects only dependent work; keep independent authorized work moving.

| Requirement / decision ID | Material unknown or change / concrete alternatives and effect | Existing answer or authority; remaining question if needed | Dependent work / independent work | Resolution, exact replacement and retained scope |
| --- | --- | --- | --- | --- |

| Changed requirement, component, context or new usage | Affected usage and obligation IDs / impact boundary | Invalidated results and prior revision | Required correction / fresh evidence and current revision | Remaining gap |
| --- | --- | --- | --- | --- |

| Requirement/capability IDs | Exception, removal, exclusion or deferral / exact usage and context | Consequence and alternative | Actual authority reference and limits / proposal if unavailable | Replacement decision or outstanding obligation IDs |
| --- | --- | --- | --- | --- |

## Reconciliation and readiness

- Source-to-result reconciliation: sources checked, requirements mapped, missing answers/qualifiers/usages and unresolved obligations:
- Artifact-to-source reconciliation: material choices and additions accounted for, unsupported scope or departures:
- Current claim and exact scope: mapped / concept demonstrated / implemented / verified / accepted:
- Required checks due now: supported passes, failures, blocked, untested or stale results, with IDs:
- Original requested work deferred or excluded, with actual authorization and remaining obligations:
- Evidence limitations and newly discovered work:

Completion is bounded to the stated stage, scope and reconciled model. All active in-scope requirements and their due obligations must be supported before claiming conformance. An audit may complete its investigation while reporting evidenced defects. Neither complete records nor a percentage guarantees exhaustive discovery or a flawless product.
