# Requirements that survive delivery

Use this method when discovering requirements, translating answers into a concept, handing work to contributors, or checking conformance after a change. Its purpose is to prevent known requirements from disappearing between discussion and the delivered artifact. It supports a bounded completion claim; it cannot guarantee exhaustive discovery, perfect interpretation or defect-free results.

Maintain one authoritative requirement register in the target project using [requirements.template.md](../assets/requirements.template.md), or an equivalent section of an existing project record. For a focused fix, a few rows are sufficient. Link the brief, design contract, feature map and evidence through stable IDs. Keep detailed decisions in their existing authoritative records; the register owns their requirement-to-result trace. Reuse an existing audit ledger's entities, contexts, obligations and evidence instead of creating a second inventory or copying its results.

## 1. Preserve the source and its authority

Read the existing request, answers, approved artifacts, project constraints and observed product behavior before asking new questions. Give every consequential explicit request, answer and discovered constraint a stable requirement ID, preserving its source reference and origin type. Reuse existing question, decision and capability IDs as links. Several sources may support one requirement; split independently changeable outcomes into separate requirements. Preserve all source references when consolidating duplicates.

For each requirement, record:

- **Origin and authority:** request or answer reference, supplied document/version, applicable obligation or observed baseline; who can decide it and the scope of any existing authorization.
- **Basis:** what was observed, where and at which revision, versus what was inferred. Source code can establish a declared branch without establishing its runtime behavior. A preference establishes the owner's intent, not evidence that every user shares it. Verify applicability before treating external guidance as binding.
- **Interpretation:** the concrete outcome to preserve or change, affected task and intended artifact effect. Keep the user's meaning alongside the interpretation when paraphrasing could lose a qualifier.
- **Scope:** original requested boundary, affected capability/usage IDs, supported conditions and any authorized deferral or exclusion. A temporarily omitted prototype surface remains an obligation of a broader request.

Separate these decision states from delivery progress:

| State | Meaning |
| --- | --- |
| `confirmed` | An explicit instruction, answer, approved decision or evidenced binding constraint establishes this requirement; record its actual authority. |
| `delegated` | The user explicitly delegated this choice within recorded limits; the agent records its selected interpretation and rationale. |
| `proposed` | A recommendation or inferred preference remains a proposal; it is not user approval. |
| `unresolved` | Material meaning, conflict or authority is missing; name the dependent work and the question or evidence needed. |
| `superseded` | A later authorized decision replaces this requirement; name the exact replacement ID and source, including retained and changed scope. |

Confirmed and delegated requirements remain active until an authorized change replaces them. Rejected proposals retain their disposition without becoming requirements. An unresolved user request still belongs to the requested scope. Do not erase it, downgrade it to optional taste or mark it superseded merely because a substitute is easier to implement.

## 2. Turn meaning into an observable obligation

Establish understanding through concrete task examples before substantial direction work depends on it. Describe what the person must recognize, compare, complete or recover, and show the artifact consequence under real content and states. Replace adjectives such as “clear” or “modern” with inspectable decisions. For a request to keep a comparison visible while editing, demonstrate opening the editor, the visible comparison, the supported narrow-layout behavior and the restored context on return. A caption repeating the request is not its implementation.

Ask about material ambiguity early, following [discovery-and-preferences.md](discovery-and-preferences.md). Ground the question in the known source, competing interpretations and their different outcomes. Record the answer once and propagate it within its scope. Revisit it only when new evidence or changed instructions affect that decision, naming what changed. Continue independent authorized work while a genuine dependency waits. Resolve routine, reversible details within existing discretion; explicit delegation does not require another approval ceremony. Optional proposals can be explored without treating silence as confirmation.

For each active requirement, define independently verifiable acceptance obligations before claiming it is satisfied. Each obligation identifies:

- its requirement and existing decision IDs;
- affected capability/usage IDs and finite applicable context IDs;
- observable expected result, including relevant failure, recovery or preservation behavior;
- the stage when that result is due: concept, implementation or verification;
- required evidence method and the result that would demonstrate a failure.

Use existing acceptance or audit obligation IDs where they already express the check. One broad obligation such as “all controls look consistent” cannot replace separate checks for different observable behaviors. Conversely, link one demonstrated outcome to several requirements when the evidence actually supports each.

Plan contexts from behavior: state, role and resource scope, input, content, size, theme, locale or supported preference can create materially different cases. Name only applicable dimensions, boundaries and combinations, and justify equivalence. Repeated data instances using the same behavior may share a class; a new local implementation, role rule or responsive replacement needs its own consideration. Retain relevant checks for every distinct affected usage: equivalence groups repeated instances or context classes, not uninspected consuming surfaces. Shared-component correctness does not establish correctness in every consuming usage. Use [audit-method.md](audit-method.md) for the ledger's finite context plan when one exists; otherwise keep a small affected-usage/context plan in the register. Avoid a global Cartesian product and retain inaccessible required contexts as gaps.

### Mechanically reconcile substantial delivery

For substantial work with changing requirements or contributor handoffs, use [delivery-ledger.md](delivery-ledger.md) and its binding record alongside the authoritative requirements. Reuse IDs and existing audit obligations. Bind current content and revisions before execution; validate required stages, current decisions and actual linked files before a readiness claim. The helper detects structural gaps and changed bytes, not missing real-world requirements or truthful observation. Keep review of meaning and actual acceptance separate.

## 3. Keep concept, implementation and verification separate

Link every obligation to its actual artifact and revision. Record these independently:

| Stage record | Evidence establishes | Open work remains when |
| --- | --- | --- |
| Concept | The requirement is depicted or demonstrated in an identified concept artifact, with simulation limits | A label, placeholder, unseen page or unexercised interaction substitutes for the outcome |
| Implementation | The required destination and behavior exist in the implementation at the named revision | Only a specimen, source intention or simulated result exists |
| Verification | Required checks were executed in applicable contexts against the correct artifact and revision | Evidence is absent, stale, inferred, from another context, or lacks the needed method |

Use `pass`, `fail`, `blocked` and `not-tested` for checks, with evidence or a specific gap. A concept approval is a decision record, not a passed implementation test. A rendered image can establish appearance but not a focus sequence; source inspection can discover a handler but not prove its actual effect. Apply [verification.md](verification.md) to match the claim to its evidence. Keep the owner's assessment distinct from technical and visual observations.

An inapplicable obligation needs a factual basis in the agreed product/support contract and supporting evidence. A state excluded by that contract may be inapplicable; required behavior that is missing, or a state made unreachable by a defect, is a failure rather than an exclusion. Missing tools, access, fixtures, time or authorization to execute a required check mean blocked. A documented failure or limitation makes the result accountable; it does not make the requirement satisfied.

## 4. Reopen only what the change affects

Record a requirement/contract revision and the integrated artifact revision with each handoff and result. When an answer, scope, baseline capability, component, token, behavior or supported context changes:

1. Resolve the changed requirement to its decisions, obligations and consuming usages, including wrappers and local variants.
2. Identify new usages or branches and add their applicable obligations. Reconcile the affected set before accepting a shared change.
3. Mark affected prior results stale and reopen their checks. Preserve old evidence as history, not proof of the changed result.
4. Update the artifact and inspect the changed path and affected usages with fresh evidence before closing them.

Do not rerun unrelated checks solely because a version number changed. Explain the impact boundary and establish that any reused evidence still supports the current claim. An existing audit ledger retains its exact revision/environment rules; do not bypass those rules with a register status. A newly discovered usage reopens reconciliation even if the primitive itself is unchanged.

An **exception** names the requirement, exact usage/context, reason, permitted alternative and authority allowing that variation. Apply already authorized discretion without re-asking; keep a variation outside that authority proposed. An exception cannot silently remove the underlying task or supported capability. **Removal or reduced scope** records the affected requirement/capability IDs, consequences and actual user authorization; broad visual approval, scheduling pressure and a narrowed sample do not supply it. Preserve the original request and link the exact replacement or authorized retirement decision. An authorized deferral is unfinished work, not evidence of conformance.

## 5. Reconcile in both directions before a readiness claim

First follow every known request, answer and discovered constraint through its requirement, decision, affected usages, obligations and current evidence. Identify missing mappings, qualifiers lost in translation, undiscovered consequences, contradictions and overdue work. Reconcile source references as well as the already written rows: a complete-looking register can omit an answer from the conversation.

Then work back from the actual artifact, changed capability map and contributor outputs. Every material addition, omission, behavior and design departure must trace to an active requirement, justified supporting choice within delegated discretion, or clearly labeled proposal. Identify invented scope and dependencies rather than laundering them into “requirements.” Check whether a global rule was applied where its task or authority does not extend. A contributor's completion message is not evidence that the integrated result conforms.

Resolve contradictions with the authority and conflict rules in [SKILL.md](../SKILL.md#establish-the-product-contract). Carry forward unaffected decisions. If the available instructions do not resolve a material conflict, ask only about that conflict and continue independent work. Record the source of the resolution and exact replacements so two contradictory interpretations cannot remain active.

## 6. Bound completion to what was established

A stage is complete for its stated scope only when every active in-scope requirement is accounted for, its obligations due at that stage are supported by the required current evidence, and no required applicable check or material decision remains missing, stale, failed, blocked or untested. Accounted for and satisfied are different: listing unfinished work does not close it. Report an interim or narrower authorized deliverable honestly while retaining the original request's remaining obligations.

For audit-only work, completing the investigation may include evidenced failures reported as findings; it does not establish that the product conforms. Retain the audit ledger's separate reviewed-coverage and checks-passed claims. For concept or implementation work, preserve the distinction between requirements mapped, concept demonstrated, implemented, verified and accepted. Approval covers only the actual authorized scope and cannot supply missing evidence.

Report open requirement IDs, affected scope, failures, missing decisions and unavailable checks alongside the supported completion claim. Any counts concern the declared, reconciled model; no score or percentage can hide an unresolved requirement or promise total discovery, flawless design or proven user benefit. Newly discovered requirements and effects reopen the affected work.
