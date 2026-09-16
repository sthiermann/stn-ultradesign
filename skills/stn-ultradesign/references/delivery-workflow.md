# From requirements to a reviewed interface

Use this operating workflow for substantial concepts, redesigns and design-system work. It coordinates the specialist references; it does not replace them. Keep the project brief, decisions, previews and review evidence in the target project's agreed output area, outside this reusable skill package. Use the [delivery record](../assets/delivery-plan.template.md) when several surfaces or contributors need coordination.

## Start at the actual state of the project

Establish the requested outcome, current scope and authorization. Continue from an already approved concept without reopening settled choices. For a focused repair, use only the affected requirements, implementation and review steps. Audit-only work uses [audit-method.md](audit-method.md) and stops at findings unless design work is requested. These are working stages, not eight mandatory approval meetings.

Read the existing framework, components, domain behavior and owner's answers first. Carry a current contract revision through each stage. When new evidence contradicts a decision, reopen only the affected part and its consuming surfaces. A preference cannot be satisfied merely by writing it into a brief: it needs an observable consequence in the artifact.

## Assign responsibilities, not fictional staff

| Responsibility | Produces | Accountable check |
| --- | --- | --- |
| Requirements and UX lead | Product purpose, adaptive interview, current capability map, task and navigation model | Every requested outcome has a visible entry, meaningful result and return; missing domain meaning stays explicit |
| Visual designer | Art direction, composition alternatives, typography, palette, materials, shape, imagery and motion | The work expresses this product and agreed identity across actual content, states and device sizes |
| Design engineer | Shared tokens, accessible primitives, product components, interactive concept and authorized implementation | The actual HTML/CSS/framework code delivers the visual and behavioral contract, including difficult states |
| Independent reviewer | Findings against requirements, task behavior, visual craft and implementation evidence | Observed defects are fixed and rechecked in the integrated revision; acceptance is not inferred from the author's confidence |
| Delivery lead | One current contract, assignments, integration and readiness decision | Contributors use the same approved decisions; the whole requested scope remains accounted for |
| Product owner | Preferences, consequential tradeoffs and scoped concept approval | The approval identifies the artifact and scope; an agent cannot provide it on the owner's behalf |

These are responsibilities. The delivery lead can also perform a design or engineering role; do not create an agent for every table row. When the host supports authorized subagents, delegate bounded independent work and use a reviewer that did not author the artifact. Split UX/preservation and visual/engineering review when complexity warrants it and capacity permits. A reviewer needs the actual brief and acceptance criteria, but not the author's proposed verdict or expected findings.

Use only tools and agent capabilities available in the current host. This skill does not install an autonomous team, start background workers or grant permissions. If independent review is unavailable, perform separate self-review passes, identify them honestly and retain that verification limit. Renaming a single agent's perspective does not create independent review.

## Run the stages with observable exits

| Stage | Work and visible result | Exit condition |
| --- | --- | --- |
| 1. Requirements | Inspect the product and code; discover purpose, tasks, brand inheritance, constraints and preferences; maintain the current capability map | Relevant facts and answers have decision consequences; critical unknowns are resolved or dependent work remains explicitly open |
| 2. Creative direction | Explore materially different compositions when direction is open; render the strongest direction with real task content and a distinctive interaction | The layout and identity are inspectable, connected to the brief, and stronger for a stated reason than the considered alternatives |
| 3. System and components | Choose reuse/native/primitive/custom boundaries; build shared tokens and stateful component specimens | Core controls, their open states and a demanding task component work within one coherent system |
| 4. Concept | Compose the system into complete reviewable journeys and all surfaces of the scope being presented | The user can locate retained capabilities, perform the proposed work and return; missing pages and states prevent a full-scope readiness claim |
| 5. Independent review | Review requirements and workflows separately from composition/craft and implementation; fix material findings | Reviewers inspect the corrected integrated artifact; remaining issues, unavailable checks and judgment disagreements are visible |
| 6. Human acceptance | Present the actual revision, demonstrated scope, key choices and open tradeoffs | The owner's actual approval covers the implementation being started, or explicit prior authorization already permits it |
| 7. Implementation | Build the authorized contract with shared components, then propagate through a verified critical journey | All approved surfaces and relevant states are implemented; deviations are resolved through the affected decision |
| 8. Verification | Compare the result with requirements, concept, feature baseline and target contexts | Claims are backed by the relevant source, rendered, interaction and test evidence; unresolved failures remain open |

Work may loop between stages: a component experiment can reveal a better composition, and a reviewer can reopen a workflow. Research, safe prototypes and unrelated authorized work can continue while a genuine dependent decision waits. An early preview is useful; label its actual scope rather than calling it the finished application. A full-product request remains open until its remaining surfaces and workflows are completed.

### Requirements become acceptance conditions

Follow [discovery-and-preferences.md](discovery-and-preferences.md) and [brand-discovery.md](brand-discovery.md). A substantial concept covers at least twenty relevant preference questions early, including previously answered ones, then adds questions when the product exposes material uncertainty. Ask only what cannot be responsibly established from available evidence or prior decisions. Respect explicit delegation and distinguish optional taste from an unresolved dependency.

Translate each consequential answer into this chain:

**Answer or observed need → scoped decision → affected tasks and component usages → observable acceptance condition → evidence.**

For example, a preference to keep a comparison visible affects panel geometry, narrow-layout return, keyboard focus and whether an editor is modal. “Use a modern panel” captures none of those outcomes. Link to existing brief, feature-map and contract IDs instead of copying competing versions of the same requirement into each worker's notes. Give changes in user direction precedence over older preferences and record which decisions they replace.

### Creative direction is a real work product

Use [visual-systems.md](visual-systems.md) and [concept-to-code.md](concept-to-code.md). Choose visual ambition with the owner and the product's purpose: a campaign, creative tool and high-density operations screen can be equally distinctive through different decisions. Explore structure, typography, image/diagram treatment, material and interaction together. A different accent on the same generic composition is not a distinct proposal.

When the brief leaves a major direction open, compare two or three credible approaches using the same difficult content and task. Recommend one; do not make the user assemble unrelated fragments. An established approved direction needs refinement, not another obligatory round of alternatives. Demonstrate a memorable, task-relevant interaction when it improves the experience; meaningful direct manipulation, animated explanation or spatial inspection may earn its complexity. Follow the requested expressive range rather than defaulting every application to either a quiet dashboard or a decorative showcase.

For a chosen reference language, research its relevant current or explicitly requested generation, inspect examples and translate its mechanisms into project rules. Judge the actual material, geometry, motion and information hierarchy. An adjective, copied screenshot arrangement or library theme name is insufficient. Keep research provenance private to the project; do not import unrelated references into the reusable skill.

### Build one authored component system

The design engineer follows [web-engineering.md](web-engineering.md), or the project's native framework equivalent. Preserve suitable existing foundations. Reuse proven interaction behavior where it fits, with an intentionally designed presentation. Choose custom behavior when the domain requires it and its full input/state contract can be implemented and verified.

Classify actions before selecting their surfaces under [component-states.md](component-states.md). Give shared semantic tokens and composed components clear owners; page authors consume them rather than inventing new palettes, shadows, selectors or dialog rules. The concept and implementation should share those definitions when practical. If different tools require translation, specify the mapping and demonstrate a representative translated component before expanding.

Build a state board with the core button/field/selection/menu/editor families and the product's most demanding domain component. Open the menu and selector; show focus, selection, loading, error, long text and relevant theme/input variants. Judge the components in a real page as well as in isolation. A gallery of attractive closed controls does not finish the system stage.

### Review outcomes separately

The independent reviewer returns concrete findings and evidence, not a flattering score:

| Review lens | Questions that can reject the candidate |
| --- | --- |
| Requirements and preservation | Did any answer, existing action, real role, data meaning or supported combination disappear? Are the remaining pages merely labels? |
| UX and comprehension | Can someone discover and finish the critical task without knowing the implementation? Is the outcome real in the prototype state, and is return/recovery clear? |
| Visual craft | Is the hierarchy deliberate, composition product-specific, typography controlled, material convincing and detail consistent across states and sizes? Does the owner's chosen reference actually come through? |
| Engineering and inclusion | Do shared components, semantics, focus, input modes, draft state, reduced effects and performance support the proposed experience? |
| Contract fidelity | Does the integrated revision match the approved structure, behavior, content and visual rules? Which differences are authorized? |

A serious failure in one lens is not offset by strengths in another. Record reproduction or observed context, affected decision/capability, consequence and correction. The engineer/designer fixes the artifact; the reviewer checks the new revision and affected shared usages. Do not close a finding with revised prose or an old screenshot. Continue until the reviewable scope has no unresolved readiness blockers, or report the specific dependency that prevents closure. User rejection remains unresolved until a concrete new artifact addresses it.

Review [verification.md](verification.md) and its relevant browser/task checks. Source-only review can find a missing handler; it cannot validate glass rendering, movement or pointer/touch behavior. Capture actual previews at the requested desktop/tablet/phone contexts, difficult content and open controls. A code test pass does not establish visual quality, and a visual pass does not establish preserved business behavior.

## Delegate with a complete, bounded handoff

For each worker provide the task, required skill branch, current brief/contract revision, baseline and input artifacts, exact allowed outputs/files, applicable capability IDs, unresolved decisions, tools available and completion evidence. The [delivery record](../assets/delivery-plan.template.md) contains the minimal handoff fields. Preserve existing authorization; do not give a worker broader production or external-action permission than the project has.

Parallelize independent discovery, reference investigation or review. Settle shared navigation, tokens and component contracts before parallel page construction. Assign one owner per shared file or use an explicit integration boundary. Workers return artifacts and concise findings; the lead inspects their actual result and reconciles contradictions. A worker's “done” message is not an integration check.

## Report the next real decision

Distinguish a direction preview, a scoped concept ready for owner review, an approved concept, an implemented result and verified behavior. Name the current stage, demonstrated scope and remaining work. Keep the user's conversation concise; keep detailed traceability with the project artifacts. The method supports ambitious, original work, but awards, virality and superiority require external outcomes and cannot be declared by the skill.
