# From requirements to a reviewed interface

Use this operating workflow for substantial concepts, redesigns and design-system work. It coordinates the specialist references; it does not replace them. Keep the project brief, decisions, previews and review evidence in the target project's agreed output area, outside this reusable skill package. Use the [delivery record](../assets/delivery-plan.template.md) when several surfaces or contributors need coordination.

## Start at the actual state of the project

Establish the requested outcome, current scope and authorization. Continue from an already approved concept without reopening settled choices. For a focused repair, use only the affected requirements, implementation and review steps. Audit-only work uses [audit-method.md](audit-method.md) and stops at findings unless design work is requested. These are working stages, not eight mandatory approval meetings.

Read the existing framework, components, domain behavior and owner's answers first. Carry a current contract revision through each stage. When new evidence contradicts a decision, reopen only the affected part and its consuming surfaces. A preference cannot be satisfied merely by writing it into a brief: it needs an observable consequence in the artifact.

## Assign responsibilities, not fictional staff

| Responsibility | Produces | Accountable check |
| --- | --- | --- |
| Requirements and UX lead | Product purpose, adaptive interview, requirement register, current capability map, task and navigation model | Every active requirement has a scoped interpretation and acceptance obligations; missing meaning and conflicts stay explicit |
| Visual designer | Investigated reference profile when selected, art direction, composition alternatives and visual/interaction rules | Observed mechanisms become explicit project rules; the work expresses the agreed identity across actual content, states and device sizes |
| Design engineer | Shared tokens, accessible primitives, product components, interactive concept and authorized implementation | The actual HTML/CSS/framework code delivers the visual and behavioral contract, including difficult states |
| Independent reviewer | Findings against requirements, task behavior, visual craft and implementation evidence | Observed defects are fixed and rechecked in the integrated revision; acceptance is not inferred from the author's confidence |
| Delivery lead | One current contract, assignments, integration and readiness decision | Contributors use the same approved decisions; the whole requested scope remains accounted for |
| Product owner | Preferences, consequential tradeoffs and scoped concept approval | The approval identifies the artifact and scope; an agent cannot provide it on the owner's behalf |

These are responsibilities. The delivery lead can also perform a design or engineering role; do not create an agent for every table row. When the host supports authorized subagents, delegate bounded independent work and use a reviewer that did not author the artifact. Split UX/preservation and visual/engineering review when complexity warrants it and capacity permits. A reviewer needs the actual brief and acceptance criteria, but not the author's proposed verdict or expected findings.

Use only tools and agent capabilities available in the current host. This skill does not install an autonomous team, start background workers or grant permissions. If independent review is unavailable, perform separate self-review passes, identify them honestly and retain that verification limit. Renaming a single agent's perspective does not create independent review.

## Execute bounded work items

For a redesign spanning sessions, multiple contributors or substantial feedback cycles, turn the existing requirements into executable work items. Default to local Markdown, without asking the user to configure a tracking system. Reuse the current design effort's records and location; honor an explicitly required tracker or repository convention. Otherwise create `.ultradesign/<effort>/` in the target project and briefly tell the user where the records live and how work will proceed. Ask only if ownership, location or conflicting instructions materially change the work. Creating remote issues, publishing private evidence or sending notifications needs the relevant authorization; local records are not automatically publication-ready.

Use `plan.md` from the [delivery record](../assets/delivery-plan.template.md) as the index, `requirements.md` from the [requirement register](../assets/requirements.template.md) as the source of acceptance obligations, `tickets/UD-001-short-title.md` from the [work-item template](../assets/work-item.template.md) for each nontrivial item, and `evidence/` for actual review artifacts. These are defaults, not parallel copies of existing records. Create only what the task needs; a focused repair can use one compact record. Tickets link requirements and evidence rather than restating their changing details.

Distinguish work that **resolves an open decision**, work that **builds a concept or approved implementation**, and work that **verifies an integrated result**. Link them through stable requirement and acceptance IDs. An answered decision does not finish its implementation, and a worker's completed artifact does not finish its review. Record ordinary delegated choices inside their affected item instead of making the owner approve every component detail.

Each item needs a meaningful title, the user outcome/problem, source requirement IDs, current decision revision, preserved capabilities and roles, bounded deliverable/files, dependencies, accountable owner, observable acceptance checks and the evidence needed to close it. Add the scope-specific skill references. A decision item states the uncertainty, supported recommendation and tradeoffs; a construction item states the agreed behavior; a review item states the artifact/revision and checks to exercise. Specify independent outcomes rather than a ticket for every file or visual knob.

Work through items with explicit state:

| State | Meaning and next action |
| --- | --- |
| Queued | Relevant work is recorded, but inputs, ownership or scope are not ready. Keep the uncertainty visible. |
| Ready | The bounded outcome, inputs, authority and acceptance checks are sufficient to start; required dependencies are resolved. |
| In progress | One owner has claimed the item and is producing the decision, artifact or evidence. |
| In review | The result and its revision are linked; the required verification or owner judgment remains open. |
| Done | The item's own acceptance conditions have evidence and any required decision has its actual authority. Name whether this completes a decision, a concept increment, implementation or verification. |
| Blocked | A named missing input or failed dependency prevents progress. Record the next resolving action; independent items can continue. |

Before assigning work, reconcile current state and dependencies, claim one owner per output boundary and select ready items. Default to completing one coherent workflow increment through integration and review before expanding it. Parallelize independent inspection or review; parallel construction is appropriate only when outputs and shared component contracts are settled. Serialize shared navigation/component decisions and the human interview. A waiting owner question does not block unrelated inspection. A worker receiving a stale contract must reconcile affected work before integration. On resumption, read the item and linked current decisions instead of relying on conversational memory.

At closure, link the decision or changed artifact, executed checks and current evidence. Integrate changes and inspect affected consumers before marking an implementation item done; a verification item cannot pass on the author's summary. Record a narrower verified increment without closing the remaining parent scope. New feedback updates affected items, dependencies and acceptance checks, reopening stale results while preserving completed unrelated work. Rejected or superseded proposals retain their disposition; outstanding product capabilities remain in scope unless the user actually changes that scope.

Compare each due acceptance obligation with the actual result, one by one, using the original requirement and latest decision rather than the implementer's paraphrase alone. Record expected behavior, observed behavior, revision/context, evidence and any discrepancy. A missing, failed, stale or unexecuted required check prevents closure of that scope. Correct discrepancies and recheck affected usages; an explicit scope change records what remains outside the claim instead of turning a failed criterion into a pass. Close the parent only after its active in-scope obligations are reconciled. This requires traceability for every known requirement; it does not justify a promise of perfect discovery or error-free execution.

Report progress by outcomes and names, such as “Notification editor: implemented, visual review pending.” Ticket counts measure the planned work only; they do not prove exhaustive discovery, design quality or user acceptance.

## Run the stages with observable exits

| Stage | Work and visible result | Exit condition |
| --- | --- | --- |
| 1. Requirements | Inspect the product and code; discover purpose, tasks, brand inheritance, constraints and preferences; reconcile the requirement register and capability map | Active requests and discovered constraints have scoped interpretations and acceptance obligations; critical unknowns leave dependent work open |
| 2. Creative direction | Investigate the selected reference; explore compositions where direction remains open; render real task content and a meaningful interaction | The reference's applicable families, source conflicts and evidence gaps are accounted for; derived rules and any departures are explicit; composition follows the brief |
| 3. System and components | Choose reuse/native/primitive/custom boundaries; build shared tokens and stateful specimens; compare demanding examples with the intended rules | The representative proof passes its declared visual and interaction checks; unverified native behavior and unresolved interpretations remain open before affected patterns expand |
| 4. Concept | Compose the system into complete reviewable journeys and all surfaces of the scope being presented | The user can locate retained capabilities, perform the proposed work and return; missing pages and states prevent a full-scope readiness claim |
| 5. Independent review | Review requirements and workflows separately from composition/craft and implementation; fix material findings | Reviewers inspect the corrected integrated artifact; remaining issues, unavailable checks and judgment disagreements are visible |
| 6. Human acceptance | Present the actual revision, demonstrated scope, key choices and open tradeoffs | The owner's actual approval covers the implementation being started, or explicit prior authorization already permits it |
| 7. Implementation | Build the authorized contract with shared components, then propagate through a verified critical journey | All approved surfaces and relevant states are implemented; deviations are resolved through the affected decision |
| 8. Verification | Reconcile every active in-scope requirement with the result, concept, feature baseline and target contexts | Required applicable obligations have current evidence; failures, gaps and authorized exclusions are separate from passes; the result has no unexplained consequential additions |

Work may loop between stages: a component experiment can reveal a better composition, and a reviewer can reopen a workflow. Research, safe prototypes and unrelated authorized work can continue while a genuine dependent decision waits. An early preview is useful; label its actual scope rather than calling it the finished application. A full-product request remains open until its remaining surfaces and workflows are completed.

### Requirements become acceptance conditions

Follow [discovery-and-preferences.md](discovery-and-preferences.md) and [brand-discovery.md](brand-discovery.md). A substantial concept covers at least twenty relevant preference questions early, including previously answered ones, then adds questions when the product exposes material uncertainty. Ask only what cannot be responsibly established from available evidence or prior decisions. Respect explicit delegation and distinguish optional taste from an unresolved dependency.

Use [requirements-conformance.md](requirements-conformance.md) for the authoritative request-to-result chain, decision states, acceptance obligations and change handling. Link existing brief, feature-map and contract IDs rather than copying competing records into each worker's notes. For example, keeping a comparison visible affects panel geometry, narrow-layout return, focus and modality; “use a modern panel” does not define those outcomes. Confirm a material interpretation through a concrete example or focused question; proceed within already delegated choices.

Before a critical journey determines the composition, distinguish its existing behavior from the proposed change: entry, object, opening surface, context that stays visible, role-dependent information, outcome and return. Resolve material ambiguity in words such as “beside,” “details” or “fullscreen” through that concrete walkthrough. An overlay and a pane that resizes the workspace are different decisions. A chosen default does not remove an existing user-selectable mode. Carry these outcomes into the shared interaction contract before parallel page construction.

### Creative direction is a real work product

Use [visual-systems.md](visual-systems.md) and [concept-to-code.md](concept-to-code.md). Choose visual ambition with the owner and the product's purpose: a campaign, creative tool and high-density operations screen can be equally distinctive through different decisions. Explore structure, typography, image/diagram treatment, material and interaction together. A different accent on the same generic composition is not a distinct proposal.

When the brief leaves a major direction open, compare two or three credible approaches using the same difficult content and task. Recommend one; do not make the user assemble unrelated fragments. An established approved direction needs refinement, not another obligatory round of alternatives. Demonstrate a memorable, task-relevant interaction when it improves the experience; meaningful direct manipulation, animated explanation or spatial inspection may earn its complexity. Follow the requested expressive range rather than defaulting every application to either a quiet dashboard or a decorative showcase.

For a chosen reference language, complete the applicable study and translation in [project-research.md](project-research.md). Establish the actual generation and platform, inspect relevant subsections and component variants, and distinguish textual, visual and interaction evidence. Give the designer and engineer the same project profile and rule IDs. A prior project's reference, a library's defaults or a source's unexamined appearance must not silently supply missing decisions.

### Build one authored component system

The design engineer follows [web-engineering.md](web-engineering.md), or the project's native framework equivalent. Preserve suitable existing foundations. Reuse proven interaction behavior where it fits, with an intentionally designed presentation. Choose custom behavior when the domain requires it and its full input/state contract can be implemented and verified.

Classify actions before selecting their surfaces under [component-states.md](component-states.md). Give shared semantic tokens and composed components clear owners; page authors consume them rather than inventing new palettes, shadows, selectors or dialog rules. The concept and implementation should share those definitions when practical. If different tools require translation, specify the mapping and demonstrate a representative translated component before expanding.

Build a state board with the core button/field/selection/menu/editor families and the product's most demanding domain component. Open the menu and selector; show focus, selection, loading, error, long text and relevant theme/input variants. Judge the components in a real page as well as in isolation. A gallery of attractive closed controls does not finish the system stage.

Before scaling a reference-led direction, compare this proof with the selected reference under comparable conditions. Check task roles, geometry relationships, foreground/background behavior and actual transition sequences, not just a mood or a closed-state screenshot. If the proof fails, correct the underlying rule or implementation and recheck it before spreading that pattern. This is an internal quality checkpoint, not an extra mandatory owner approval. It establishes only the named specimens; stage 4 still covers the whole requested concept and stage 8 its applicable usages.

### Review outcomes separately

The independent reviewer returns concrete findings and evidence, not a flattering score:

| Review lens | Questions that can reject the candidate |
| --- | --- |
| Requirements and preservation | Does every active requirement reach an actual artifact and current acceptance evidence? Did any answer, existing action, real role, data meaning or supported combination disappear? Are additions within authorized discretion? |
| UX and comprehension | Can someone discover and finish the critical task without knowing the implementation? Is the outcome real in the prototype state, and is return/recovery clear? |
| Visual craft | Is the hierarchy deliberate, composition product-specific, typography controlled, material convincing and detail consistent across states and sizes? Does the owner's chosen reference actually come through? |
| Engineering and inclusion | Do shared components, semantics, focus, input modes, draft state, reduced effects and performance support the proposed experience? |
| Contract fidelity | Does the interpreted reference satisfy the request, does the concept embody those rules, and does the integrated revision match the approved concept? Which differences are authorized, unverified or unresolved? |

A serious failure in one lens is not offset by strengths in another. Record reproduction or observed context, affected decision/capability, consequence and correction. The engineer/designer fixes the artifact; the reviewer checks the new revision and affected shared usages. Do not close a finding with revised prose or an old screenshot. Continue until the reviewable scope has no unresolved readiness blockers, or report the specific dependency that prevents closure. User rejection remains unresolved until a concrete new artifact addresses it.

Review [verification.md](verification.md) and its relevant browser/task checks. Source-only review can find a missing handler; it cannot validate glass rendering, movement or pointer/touch behavior. Capture actual previews at the requested desktop/tablet/phone contexts, difficult content and open controls. A code test pass does not establish visual quality, and a visual pass does not establish preserved business behavior.

## Keep autonomous work grounded and resumable

At each handoff or resumption, recover the current brief, active decisions, artifact revision, completed checks and open dependencies before continuing. Compare the actual files and running state with that record. Carry forward approved preferences and authorizations; reopen only affected decisions. Resolve ordinary implementation details within the agreed direction, and ask focused questions when domain meaning, a consequential tradeoff or authority is missing. An unanswered optional preference remains a proposal, not an approval.

Keep the skill path/version, active stage, unanswered question IDs, unresolved owner feedback and next due checks in the existing delivery record. At a restart, integration or substantial feedback change, recover this state and read the affected skill branch. Re-reading the entrypoint alone is not evidence that its checks ran. Give one lead ownership of the user-facing interview; contributors return suggested questions to that lead instead of starting competing interviews.

Separate observed facts, source-declared behavior, authoritative requirements, design judgments and untested hypotheses. Check applicable current guidance when a recommendation depends on a standard, platform generation or API. Do not convert a plausible convention into a worldwide requirement or invent a business threshold to make a widget look complete. Tie consequential choices and claims to inspectable evidence or a clearly stated limit.

Use distinct review passes: the author checks the task and artifact; a separate reviewer, where available, challenges original requirements, interpretation, failure paths and visual craft; the integrated correction is then rechecked at its new revision. Give reviewers raw inputs and acceptance conditions without the author’s desired verdict. Include a valid counterexample so a rule does not reject useful variation. Repeating the same opinion is not another test. If a defect survives a correction, investigate its cause and dependencies rather than accumulating cosmetic overrides.

Continue authorized work through corrections and affected-usage regression checks until the declared stage exit is supported. Stop dependent work for a concrete missing decision, unavailable capability or authorization boundary, and report the exact unresolved obligation while continuing independent work. Never close a gap merely to finish a turn, meet a time budget or obtain a green score. Present the evidence and remaining choices concisely; keep internal evaluation mechanics out of product-facing copy.

## Delegate with a complete, bounded handoff

For each worker provide the task, required skill branch, current requirement/contract/profile revisions, original request and decision references, baseline and input artifacts, exact allowed outputs/files, complete affected requirement/rule/capability IDs, deferred or blocked obligations, tools available and completion evidence. Reviewers receive the original inputs as well as the author's summary. Require workers to return the revisions they used; stale decisions reopen the affected result before integration. The [delivery record](../assets/delivery-plan.template.md) contains the minimal handoff fields. Preserve existing authorization; do not give a worker broader production or external-action permission than the project has.

Parallelize independent discovery, reference investigation or review. Settle shared navigation, tokens and component contracts before parallel page construction. Assign one owner per shared file or use an explicit integration boundary. Workers return artifacts and concise findings; the lead inspects their actual result and reconciles contradictions. A worker's “done” message is not an integration check.

## Check the actual review package before presenting it

Use the existing delivery record for a short checkpoint, scaled to the next claim. Early direction previews remain useful; they need checks of their depicted tasks, not evidence for every unfinished page. A complete concept needs its full due-stage coverage.

1. **Loaded artifact:** identify the actual preview entrypoint/build and revision. Make the review frame, linked brief, capability summary and launch instructions describe that same artifact; archive or clearly supersede stale entrypoints.
2. **Review scope:** name what the user can exercise now and retain outstanding capabilities by ID, current/proposed location and next work. When replacing a broad concept with a smaller direction study, retain the former artifact as a comparison and give an accessible scope map outside the product canvas. A general promise that other features remain is insufficient.
3. **Requirements and feedback:** trace the relevant original answers and unresolved criticisms to the candidate, including qualifiers and role-dependent behavior. Check the integrated usages, not just shared primitives. Aesthetic rejection is distinct from a technical failure and remains a design outcome to resolve.
4. **Executed checks:** inspect the depicted critical paths and changed component families with demanding content, open controls and applicable device/input contexts. Connect actual results to existing obligation IDs and current evidence; update the delivery bindings when used. Archived test notes with no current result mapping do not complete this step. Keep rendering, source review, interaction checks and owner acceptance distinct.
5. **Next decision:** state the demonstrated scope, remaining gaps and the specific judgment sought. Freeze the compared artifact while that question is active; perform unrelated work separately. If a necessary fix changes what the user is judging, identify the new revision and affected comparison explicitly.

If a due check is unavailable or fails, deliver a bounded draft or report the blocker instead of upgrading the claim. A validator checks the records; it cannot establish that the interface was observed or that its design is good.

## Report the next real decision

Distinguish a direction preview, a scoped concept ready for owner review, an approved concept, an implemented result and verified behavior. Name the current stage, demonstrated scope and remaining work. Keep the user's conversation concise; keep detailed traceability with the project artifacts. The method supports ambitious, original work, but awards, virality and superiority require external outcomes and cannot be declared by the skill.
