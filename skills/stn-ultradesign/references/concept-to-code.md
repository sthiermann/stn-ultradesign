# Concept, refinement, approval, implementation

This is the owner's preferred process for substantial new designs and redesigns. It is a workflow chosen for this skill, not an international standard. Use it when requested or as the default stated in `SKILL.md`; honor explicit authorization to implement directly.

## The reviewable concept

Start a substantial concept with a **visual thesis tied to the product's work**: what the person needs to recognize, compare or control, and how the composition will make that relationship visible. Name the organizing object or activity, the dominant region, the supporting context, the intended density, and the visual character. “Modern, clean, premium” is not a thesis. “An exception-focused dispatch workspace with a stable activity spine and an adjacent object inspector” makes structural choices that can be challenged. This example is a candidate for that task, not a template for other products.

Before polishing a substantial new direction, sketch materially different structural options where the existing composition is in question. Compare the location of the work, information relationships, navigation model, density and movement from overview to detail under the same real task and content. A new accent color on the same sidebar/card grid is not a structural alternative. Select and explain the strongest direction; present alternatives when the remaining choice needs the user's judgment. Keep familiar controls where they help, while giving the overall composition a reason to belong to this product.

Deliver a coherent recommended direction. Offer a small number of alternatives only when there is a meaningful unresolved strategic choice: for example, a compact analyst workspace versus an approachable guided workflow. Changing only colors is not a useful alternative concept.

Make the concept concrete enough that the user can judge it before application code is changed:

| Artifact | What the user should be able to judge |
| --- | --- |
| Product brief | Audience, primary task, scope, assumptions, success criteria |
| Visual thesis and composition choice | Which domain relationships shape this design; why this structure fits better than the considered alternatives |
| Information architecture | Main destinations, route relationships, naming, wayfinding |
| Workflow diagram | Actor, entry, decisions, back/cancel, progress, success and recovery |
| Annotated wireframes | Information hierarchy, grouping, density, primary actions, structural behavior |
| Rendered visual concept | Actual layout, fonts, type hierarchy, palette, spacing, icon treatment, surfaces |
| Responsive concept | Desktop, tablet and phone views plus rules between sample widths |
| Component/state sheet | Relevant input, focus, selection, validation, loading and error treatments |
| Interaction prototype | Material behavior that a still image cannot express |
| Decision summary | Proposed choices, reasons, tradeoffs, unresolved questions, next review decision |

Scale the artifacts to the project. For a single dialog, provide that dialog's small/large layouts and its meaningful states. For a whole product, show representative screen families and explicitly list pages not yet designed. Approval of a sample dashboard does not imply approval of an unseen administration or checkout flow.

Prefer real product content. Label illustrative or synthetic data. Include long labels, empty datasets, an error, and a dense example where these can materially change layout. Do not build the concept around a perfect sample that conceals failures.

A visual concept should be an inspectable image, rendered HTML/React preview, accessible document, or design-tool artifact, according to available tools. A prose-only description is a specification draft, not a completed visual concept. A rendered prototype is a design artifact; it can use isolated local files and fake data before production implementation is approved. Clearly mark what is simulated. Image mockups cannot prove keyboard behavior, interaction, or production feasibility.

## Render, critique and refine before presenting a finished concept

For a multi-device concept, inspect actual renders for every target class: desktop, tablet and phone when all three are in scope, plus widths around structural changes. Record the real rendering environment, loaded fonts, content fixture and viewport; preserve reviewable evidence. Check a meaningful dense or difficult state as well as the ideal opening state. A desktop render with CSS breakpoints declared in source is not responsive proof. If rendering is unavailable, deliver a labeled draft with that limitation; do not call the visual concept finished or its craft verified.

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

Ask for feedback on the most consequential open choices. Resolve routine implementation details yourself within the approved rules. Never convert optional questions into an unnecessary approval gate.

Use `assets/design-contract.template.md` to turn discussion into one current source of truth. Keep an approval record tied to the actual user message, date, scope and artifact version. A proposal written by the agent is not approval. Silence and elapsed time are not approval.

## Approval boundary

Before requesting concept approval, finish the design work needed to make the proposal reviewable. Clearly state the exact version and scope awaiting approval. Continue already authorized research and prototype verification while feedback is pending. Wait to implement the affected production design until the user's approval arrives.

Approval can be scoped: “Use variant B for the dashboard; keep exploring settings.” Implement the approved dashboard independently; leave settings in concept status. “Looks good, implement this version” is sufficient approval when the referred artifact is unambiguous. Do not ask again.

Material open questions are resolved or explicitly excluded before dependent implementation: navigation structure, destructive workflows, permission scope, critical content, and identity flows. Small details can have agreed discretion, such as optical icon alignment within the established component specification.

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

Define agreed freedom: fluid spacing ranges, text wrapping rules, permitted density variants and component substitutions. State fixed acceptance environments (browser, viewport in CSS pixels, zoom, fonts, data fixture, theme, locale) for screenshot comparison. Use local visual-diff tolerances justified by rendering noise; a universal pixel-difference percentage cannot establish equivalence.

Changes to technical internals are within implementation discretion when the observable contract is preserved. Changes to approved information order, navigation, color meanings, wording, interactions, or component behavior are design changes and require the relevant concept revision. Do not silently substitute fonts or icons because they were inconvenient to obtain.

If a font lacks a suitable license, a control cannot support the required access mode, or the real backend contradicts a proposed flow, record the conflict. Show the smallest viable alternatives with impact. Seek approval for the affected decision only, and continue unrelated approved work.

## Implement from the contract

1. Link each acceptance ID to its source decision, affected route/component and verification method.
2. Implement shared tokens and primitives, then a real vertical slice of a critical journey.
3. Render the slice with the agreed fixture and compare it with the approved artifact.
4. Resolve deviations before expanding the pattern across the application.
5. Complete remaining agreed surfaces and states, keeping the traceability table current.

Reference images are comparison evidence, not a reason to hardcode all coordinates. Use resilient web layout that follows the agreed constraints. Preserve semantics and usable order when adapting the visual design.

## Finish with a conformance report

For each acceptance ID record `pass`, `fail`, `blocked`, or `not-tested`, with evidence. Include approved deviations, the implementation revision, tested environments and outstanding dependencies. Report semantic/behavioral equivalence separately from visual fidelity.

Completion means the agreed scope is implemented and verified to the available evidence. A limitation such as unavailable screen-reader testing remains explicit; neither a good screenshot nor a broad approval retroactively establishes a missing test.

When discussing the result, show a short before/concept/implemented comparison where useful. Describe material differences rather than making the user infer them from images.
