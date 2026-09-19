# Concept, refinement, approval, implementation

Use [delivery-workflow.md](delivery-workflow.md) for stage order, responsibilities, handoffs and readiness. This reference defines the concept artifacts, refinement and implementation contract within that workflow. It is the skill's chosen method, not an international standard; honor existing approval and explicit authorization to implement directly.

Carry the current [requirement register](requirements-conformance.md) through concept and implementation. It records what must be satisfied; the design contract records how and what was approved. Link these records rather than maintaining competing interpretations. A selected reference additionally needs the applicable [research and translation](project-research.md) before the affected direction is treated as settled.

## The reviewable concept

Start a substantial concept with a **visual thesis tied to the product's work**: what the person needs to recognize, compare or control, and how the composition will make that relationship visible. Name the organizing object or activity, the dominant region, the supporting context, the intended density, and the visual character. “Modern, clean, premium” is not a thesis. “An exception-focused dispatch workspace with a stable activity spine and an adjacent object inspector” makes structural choices that can be challenged. This example is a candidate for that task, not a template for other products.

Before polishing a substantial new direction, sketch materially different structural options where the existing composition is in question. Compare the location of the work, information relationships, navigation model, density and movement from overview to detail under the same real task and content. A new accent color on the same sidebar/card grid is not a structural alternative. Select and explain the strongest direction; present alternatives when the remaining choice needs the user's judgment. Keep familiar controls where they help, while giving the overall composition a reason to belong to this product.

Make the concept concrete enough that the user can judge it before application code is changed:

| Artifact | What the user should be able to judge |
| --- | --- |
| Product brief | Audience, primary task, scope, assumptions, success criteria |
| Requirement and reference interpretation | What consequential requests mean in observable terms; which reference rules apply; what remains a proposal or unverified approximation |
| Visual thesis and composition choice | Which domain relationships shape this design; why this structure fits better than the considered alternatives |
| Information architecture | Main destinations, route relationships, naming, wayfinding |
| Workflow diagram | Actor, entry, decisions, back/cancel, progress, success and recovery |
| Annotated wireframes | Information hierarchy, grouping, density, primary actions, structural behavior |
| Rendered visual concept | Actual layout, fonts, type hierarchy, palette, spacing, icon treatment, surfaces |
| Responsive concept | Desktop, tablet and phone views plus rules between sample widths |
| Component/state sheet | Relevant input, focus, selection, validation, loading and error treatments |
| Interaction prototype | Material behavior that a still image cannot express |
| Decision summary | Proposed choices, reasons, tradeoffs, unresolved questions, next review decision |
| Capability-preservation summary | What stays, where moved functions are now reached, what remains undesigned, and which specific changes need a decision; linked to the feature map and applicable roles |

Scale the artifacts to the project. For a single dialog, provide that dialog's small/large layouts and its meaningful states. For a whole product, show representative screen families and explicitly list pages not yet designed. Approval of a sample dashboard does not imply approval of an unseen administration or checkout flow.

Prefer realistic product terminology and safe, non-sensitive content. Disclose illustrative or synthetic data in the external review context described below. Include long labels, empty datasets, an error, and a dense example where these can materially change layout. Do not build the concept around a perfect sample that conceals failures.

A visual concept should be an inspectable image, rendered HTML/React preview, accessible document, or design-tool artifact, according to available tools. A prose-only description is a specification draft, not a completed visual concept. A rendered prototype is a design artifact; it can use isolated local files and fake data before production implementation is approved. Clearly mark what is simulated. Image mockups cannot prove keyboard behavior, interaction, or production feasibility.

### Keep the product experience realistic and the simulation honest

Use production-appropriate labels, instructions, validation, errors and confirmation copy inside the product canvas. Do not insert implementation commentary such as “this draft creates no real API token” into a token-creation form, or repeat prototype disclaimers in every widget. Keep review status, coverage gaps, missing backend connections and implementation notes in an unmistakable review frame outside the product canvas and in the accompanying documentation. Disclose the simulation clearly once in that context; do not remove the disclosure entirely or present an unimplemented branch as a genuine permission denial, outage or empty product state.

Simulate state changes with inert fixtures. A production-like success screen is appropriate only when the enclosing review context unambiguously establishes that actions and results are simulated. It is not evidence of backend execution. Never use real credentials or private customer content, issue working tokens, send messages or trigger real external effects merely to make a concept convincing. Keep missing interactions in the external coverage record and task map; do not invent working behavior or count a placeholder as complete.

When exporting or sharing a standalone screenshot, recording or prototype, carry its concept identity and simulation status in an outer caption, review frame or accompanying metadata that recipients can actually access. Detached views must not become apparent proof of a real transaction. A watermark on every component is unnecessary.

Retain information the eventual product user needs: units, time ranges, freshness, scope, consequences and genuine workflow explanations. These are product meaning, not engineering leakage. Review every in-scope page, dialog and transient state for leaked implementation notes, repetitive disclaimers and missing product context. This check improves realism without changing the existing approval boundary or hiding unfinished work.

## Render, critique and refine before presenting a finished concept

Review the scoped concept in distinct passes rather than one undifferentiated visual glance:

1. **Work and preservation:** critical entry/outcome/return paths, direct peer switching, necessary effort, existing capabilities, roles and unfinished branches.
2. **Composition and propagation:** hierarchy, geometry, actual painted surfaces, materials, states, movement and every affected usage of confirmed decisions. Follow the brand propagation map; a specimen is not all-product evidence.
3. **Information economy:** repeated or conflicting facts across headings, controls, helpers, badges, summaries and accessible descriptions; use [the content review](workflows.md#information-economy-in-the-actual-task).
4. **Interaction and adaptation:** relevant input, theme, locale, density and viewport contexts, including open/hover/focus/error states and return after interruption.

Record concrete findings, revise the artifact, then perform a separate verification pass on the affected paths and shared usages. Review the latest rendered revision, not screenshots taken before the correction. An independent reviewer can challenge the result where available, but their source review does not substitute for rendering or user observation. These passes organize scoped work; they do not require a whole-product audit for a focused fix or guarantee flawless outcomes.

Before presenting an integrated revision, reconcile newly added modules with every agreed component-family rule that applies to them. A family choice made earlier still governs later editors, settings surfaces and dialogs. Follow the [post-integration verification](verification.md#verify-component-families-after-integration); do not let a locally polished addition bypass the existing contract or inherit a competing library default.

First complete the [critical-task walkthrough](task-flow-design.md) for the scope being presented. Use the [task-flow record](../assets/task-flow.template.md) to connect each critical task to a visible entry, meaningful content, outcome and context-preserving return. Populate existing statistics, event history and other decision-bearing detail with safe fixtures identified in the external review context; a generic placeholder or a label in the feature map leaves that branch unfinished. Show proposed actions in the context where people need them, with pointer, touch and keyboard access appropriate to the product. Do not infer discoverability from knowing your own implementation.

Then reconcile the scoped [capability walkthrough](../assets/capability-walkthrough.template.md): demonstrate where each existing action moved, what it produces and how the user returns. Exercise independent toggles and supported panel combinations instead of showing only the opening screen. A feature group cannot be called concept-complete while required child actions remain absent. Keep unfinished actions visible in the external review record and make the exact reviewable scope clear.

For a multi-device concept, inspect actual renders for each target class and widths around structural changes. Include a meaningful dense or difficult state and retain the [reproducible reference](#preserve-a-reproducible-reference). Declared breakpoints do not prove responsive behavior. Unavailable rendering leaves a labeled draft and the corresponding craft checks open.

Evaluate visual quality separately from functional checks. Syntax validity, semantic HTML, a passed accessibility scan or working save action cannot establish aesthetic excellence. Examine the rendered composition at page scale, then its details:

- Does the intended work dominate, or does chrome, repeated containers or empty space dominate?
- Do size, typography, alignment and proximity reveal the important relationships before color or borders are needed?
- Does each region have a deliberate role and density, or has the same generic card, heading, spacing and rounded surface been repeated regardless of meaning?
- Do navigation, object selection, details and actions form a convincing workflow, including interruption and return?
- Are palette, type, shape, imagery and material a coherent expression of this product rather than unrelated decoration?
- At each target size, does the composition remain intentional instead of merely stacking the desktop boxes?

Write a short self-critique naming the most consequential weaknesses, change the artifact, and inspect it again. Critique must cite visible decisions, not award the design a flattering numerical score. Show the user a coherent result and the important tradeoffs. If the user rejects the appearance, record that judgment as an unresolved design outcome, revisit the thesis and composition, and revise concrete artifacts. A rejection cannot be closed by pointing to successful technical tests or relabeling the same screen as polished.

## Refine without losing decisions

Give the concept a stable identifier and revision, such as `billing-workspace/v0.2`. Record feedback as specific decisions:

- `LAY-03`: Move filters above the result list at compact widths.
- `TYPE-02`: Retain the current product typeface; increase the heading's weight instead of changing family.
- `FLOW-04`: Saving closes the editor only after success; failure preserves values.

A revision records what changed, what stayed, and what still needs a decision. Revise the affected views and contracts together. If the user changes direction, mark replaced decisions superseded; do not retain contradictory instructions as active requirements.

For each consequential criticism, record the affected task, a concrete artifact change, an observable acceptance condition and the new evidence. Recheck the underlying cause across affected usages: a confusing settings hierarchy may also affect mobile navigation, deep links, search and return paths. Changing shadow tokens does not resolve a missing event-investigation workflow. Reconcile the source baseline again when development has continued during concept work; newly added destinations and changed role rules reopen the feature map.

Distinguish a local defect from rejection of the direction. When criticism spans layout, navigation and visual character, revisit the composition and shared component rules before adding more overrides. Prove the replacement with demanding content in a primary workspace, an administrative list/editor and any distinct critical domain component relevant to this scope. Preserve confirmed requirements and still-required capabilities through the restart; “start over” about appearance does not retire product functionality. Use the [presentation checkpoint](delivery-workflow.md#check-the-actual-review-package-before-presenting-it) to make a smaller study and its outstanding scope understandable.

Ask for feedback on the most consequential open choices. Resolve routine implementation details yourself within the approved rules. Never convert optional questions into an unnecessary approval gate.

Use `assets/design-contract.template.md` to turn discussion into one current source of truth. Keep an approval record tied to the actual user message, date, scope and artifact version. A proposal written by the agent is not approval. Silence and elapsed time are not approval.

## Approval boundary

Before requesting concept approval, finish the design work needed to make the proposal reviewable. Clearly state the exact version and scope awaiting approval. Continue already authorized research and prototype verification while feedback is pending. If the user explicitly authorized direct implementation or already approved this scope, proceed within that authorization; otherwise wait to implement the affected production design until approval arrives. Required checks and preservation still apply to directly authorized implementation.

Approval can be scoped: “Use variant B for the dashboard; keep exploring settings.” Implement the approved dashboard independently; leave settings in concept status. “Looks good, implement this version” is sufficient approval when the referred artifact is unambiguous. Do not ask again.

Material open questions are resolved or explicitly excluded before dependent implementation: navigation structure, destructive workflows, permission scope, critical content, and identity flows. Small details can have agreed discretion, such as optical icon alignment within the established component specification.

## Preserve a reproducible reference

Bind the approved scope to a restorable artifact in the [design contract](../assets/design-contract.template.md#reproducible-reference). Preserve the approved version when implementation advances. A mutable preview URL, latest build or screenshot filename alone is insufficient identification.

For executable concepts, record the source/build identity, relevant uncommitted changes or snapshot fingerprint, dependency lock/build and launch recipe, token/component sources and safe fixture version. For static artifacts, retain their original files and revision with the depicted states and interaction limits. Name the applicable browser/OS, CSS viewport and owning-container dimensions, zoom, loaded font files/weights, assets, theme, locale, density and input conditions used for comparison. Freeze clocks, generated IDs or live feeds only where their variation would obscure a meaningful comparison; document the chosen fixture behavior.

For each acceptance state, retain a short restoration recipe: reset/seed, route, actor and resource scope, selection and filters, scroll/focus, then actions needed to reach the state. Include meaningful open states such as an editor with unsaved values or a selector with a highlighted option. State what must survive cancel, save, failure and return. Reference existing task/obligation IDs rather than writing a second behavior contract.

Retain reviewable captures or a reproducible preview; where timing or spatial continuity was approved, retain a recording or reproducible interaction and its motion/reduced-motion conditions. Reopen executable references from their recipes before handoff and compare them with retained review evidence. Record any unavailable dependency or unrecoverable state as a gap; a reconstruction is a candidate reference, not retroactive evidence of what the user approved.

Use existing approval or direct-implementation authority. Restore enough evidence for the affected change without demanding a new concept approval for an already authorized repair. Design approval does not itself authorize backend security changes, production data mutations or deployment; carry those dependencies under their actual task authorization.

## What “exactly as agreed” means

Agree on rules and observable outcomes in addition to pictures. A single screenshot cannot define every viewport, text length, browser, font rendering environment, or state.

| Layer | Contract examples | Verification |
| --- | --- | --- |
| Product behavior | Roles, steps, validation, cancellation, persistence, side effects | Journey tests and user-visible state checks |
| Structure | Navigation, region order, grouping, component selection | Route/DOM review and visual comparison |
| Visual system | Named type roles, color tokens, spacing, shapes, icons | Computed styles and screenshots |
| Adaptation | Collapse rules, minimum content widths, ordering, touch behavior | Target widths and continuous resize |
| Content | Exact labels, units, error copy, locale behavior | Rendered text and content checks |
| Accessibility | Focus path, labels, announcements, reduced motion | Keyboard/AT and relevant automation |
| Data visualization | Encodings, domains, units, filters, empty/missing cases | Fixture-based data and interaction checks |

Define agreed freedom: fluid spacing ranges, text wrapping rules, permitted density variants and component substitutions. Compare in the recorded reference conditions. Use local visual-diff tolerances justified by rendering noise; a universal pixel-difference percentage cannot establish equivalence.

Changes to technical internals are within implementation discretion when the observable contract is preserved. Changes to approved information order, navigation, color meanings, wording, interactions, or component behavior are design changes and require the relevant concept revision. Do not silently substitute fonts or icons because they were inconvenient to obtain.

If a font lacks a suitable license, a control cannot support the required access mode, or the real backend contradicts a proposed flow, record the conflict. Show the smallest viable alternatives with impact. Seek approval for the affected decision only, and continue unrelated approved work.

## Implement from the contract

1. Restore the approved reference and reconcile its active requirements, affected usages and acceptance methods. Keep unavailable reference states explicit.
2. Choose reuse or necessary translation using [web-engineering.md](web-engineering.md#reuse-the-concept-in-the-application). Identify the actual shared tokens, components and data/state boundaries; implement one critical journey against real application state within the authorized test environment.
3. Restore matched concept and implementation states. Compare appearance and applicable save, cancel, failure and return outcomes against their separate expectations. Verify committed state or the authoritative result where applicable; a simulated success is insufficient.
4. Resolve the slice's required discrepancies before propagating its pattern. Keep rendering noise, implementation defects, specification gaps and authorized departures distinct. Regenerating the reference does not resolve a changed layout or outcome.
5. Extend the proven components/adapters to the remaining agreed usages and states. Run the family checks after integration and keep each acceptance result tied to the current artifact revision.

Reference images are comparison evidence, not a reason to hardcode all coordinates. Use resilient web layout that follows the agreed constraints. Preserve semantics and usable order when adapting the visual design.

## Finish with a conformance report

For each acceptance obligation use the statuses and freshness rules in [requirements-conformance.md](requirements-conformance.md). Include approved deviations, the implementation revision, tested environments and outstanding dependencies. Report semantic/behavioral equivalence separately from visual fidelity. Verify both the request-to-concept interpretation and concept-to-implementation result; faithfully implementing a misinterpreted concept does not satisfy the original requirement.

Completion requires every active in-scope requirement to satisfy its required applicable obligations with current evidence. A required check that is failed, blocked or untested prevents a completion claim for that scope. An unavailable optional check remains a disclosed limit; it is not a failed required check or proof of equivalence. An explicitly accepted reduction can complete its smaller scope while the original excluded requirements remain visibly outside that claim. Neither a good screenshot nor broad approval retroactively establishes a missing test.

When discussing the result, show a short before/concept/implemented comparison where useful. Describe material differences rather than making the user infer them from images.
