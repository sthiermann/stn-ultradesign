# Visual systems and craft

Read for visual audits, redesigns, design-system work, components, widgets, typography, color, shape, layout, density, or motion. Read [platform-adaptation.md](platform-adaptation.md) as well when surfaces resize or span desktop, tablet, and phone. For concept-first design, follow [concept-to-code.md](concept-to-code.md): present a concrete concept, refine it, obtain approval, then implement and verify the contract. Use the mode selected in `SKILL.md`; preserve already approved scope and explicit direct-implementation authorization. Use the workflow and accessibility references for behavioral requirements; visual polish never substitutes for them.

**Evidence policy.** Vendor guidance is authoritative about that vendor's intentions, not a universal rule. Source notes below identify borrowed principles. Everything labeled an audit procedure, decision table, candidate, or acceptance check is this skill's synthesis: use it to form and test product-specific decisions. Do not claim a new aesthetic improves performance without evidence. Reviewed 2026-09-16; verify implementation versions before changing dependencies.

## 1. Establish the visual contract

Before editing, write a short visual contract using observations from the actual application:

| Contract field | Required evidence | Decision it controls |
|---|---|---|
| Audience and task | Representative roles, frequency, critical work | Density, complexity, disclosure |
| Product identity | Existing brand guidance, screenshots, asset licenses | Typography, color, geometry, tone |
| Surface | Web, native shell, embedded host, device capabilities | Platform conventions, input, integration |
| Information priorities | Most important question and action per view | Hierarchy, layout, emphasis |
| Constraints | Current components, themes, localization, performance | Reuse and migration cost |
| Success | Baseline task results and observable failure | What counts as improvement |

Completion: every field has an observation or explicitly labeled assumption. For an audit-only request, propose the contract rather than silently imposing a new brand. For a redesign, preserve recognizable useful conventions and record intentional departures in the concept presented for approval. Approval applies to the specified concept version, including its desktop, tablet, and phone behavior, rather than to unspecified visual improvisation.

After approval, map each implemented token role, layout family, component variant, and relevant state back to that contract. Resolve minor engineering details within its boundaries. If implementation exposes a necessary change to the agreed appearance or interaction, document the reason and revised concrete proposal for approval before applying that deviation. Conformance includes real content, transitions, and responsive states, not merely the initial screenshot.

Choose the project’s established system or propose one coherent base. Borrow a solution only with a task reason, then reconcile its tokens, terminology, interaction states and geometry with the product’s own contract.

Treat “luxurious,” “technical,” “calm,” or “playful” as hypotheses until translated into decisions. For example, “calm” may mean fewer competing emphasis areas, stable layouts, and quieter motion. It does not automatically mean pale text, hidden borders, or missing controls. Write the decision and the user consequence together.

### Define an authored direction for substantial design work

Derive a visual thesis from domain evidence before choosing components. Identify the product's essential objects, rhythms and decisions: an editor's document, an operator's incident, a researcher's comparison, or a curator's collection require different compositions. Translate the thesis into a few visible commitments: where the work sits, what remains alongside it, how overview connects to detail, how much information is visible, and what receives emphasis. The commitments must be observable in the concept, not confined to its explanation.

Use reusable components as material for that direction. A correct library assembly is a starting point; it does not decide the page's information relationships or create a distinctive product identity. Inspect whether a brand-name swap would leave a generic shell with no visible relation to the work. If so, revisit the composition, content hierarchy and interaction sequence before changing decorative details. Reuse and visual authorship can coexist; do not replace proven control behavior merely to be different.

Compare structural alternatives with the same content when changing a major screen family. Examples include queue-plus-inspector versus overview-plus-drilldown, or a document-centered canvas versus a sequence of form sections. Assess what each keeps visible, what it hides and how it affects the next decision. Sidebars, cards, tables and grids are valid choices when their relationships fit; none should become the default shape of every unrelated surface.

## 2. Inventory before judging

Build a route-by-state inventory. Include primary pages, nested routes, authentication gates, menus, dialogs, drawers, popovers, empty/loading/error states, success feedback, permission differences, read-only modes, and embedded surfaces. Record which instances share components so a global repair can be distinguished from a page exception.

For each inspected state, retain the route, viewport, theme, locale, input mode, selected record, data volume, and screenshot or reproducible steps. Mark unavailable states as untested. A component gallery cannot prove that the composed application is usable, and a route list cannot prove that overlays or transitions were reviewed.

Audit in three passes:

1. **Structure:** identify competing priorities, missing relationships, unsuitable page architecture, and broken adaptation.
2. **System:** identify inconsistent roles, tokens, component variants, states, and cross-page patterns.
3. **Craft:** inspect typography, optical alignment, rhythm, shape nesting, icon balance, assets, and motion.

Completion: every issue includes an observable symptom, affected task, evidence, proposed change, confidence, and a verification condition. Label a visual preference as a preference. Escalate an actual task blocker above decorative inconsistency.

## 3. Choose composition from the task

The following table generates candidates; it is not a prescribed global template.

| Task | Candidate structure | Main tradeoff | Acceptance check |
|---|---|---|---|
| Read and understand | Bounded reading column, clear section rhythm | Comprehension versus simultaneous breadth | Long realistic text remains easy to follow |
| Compare many records | Table, stable headers, useful filters, detail access | Density versus target size | Relevant differences stay aligned and discoverable |
| Browse heterogeneous items | List or meaningful card collection | Visual richness versus scan efficiency | Item differences are visible without opening everything |
| Operate a complex tool | Persistent workspace and contextual inspector | Concurrent context versus crowded controls | The active object and tool scope remain unambiguous |
| Complete a bounded form | Clear sequence, grouped fields, visible action area | Progress visibility versus unnecessary fragmentation | Users can review and correct before commitment |
| Monitor and act | Prioritized status, exceptions, actionable details | Overview versus unsupported summary | A user can move from signal to relevant action |
| Explore media | Content-led canvas with restrained controls | Immersion versus discoverability | Controls remain locatable across varied backgrounds |

Separate application, page and section layout responsibilities. A reading page and an interactive console need not share one width rule.

Give each view an explicit reading order. Identify its subject, current scope, state, decision, and next action. Place necessary context before consequential actions. Use existing task priority to decide emphasis; do not promote every metric, action, and headline equally. In an expert workspace, several persistent actions may be appropriate; resolve their scope and grouping rather than demanding one global primary button everywhere.

Check repeated vertical and horizontal anchors across real content. Distinguish container alignment from text alignment. A field label, field value, heading, and neighboring table should form deliberate relationships even when borders occupy different positions. Inspect short and long titles together. Aim for a rhythm that survives content variation rather than a single perfectly balanced fixture.

Give the composition a clear distribution of emphasis. A dominant working region can be balanced by a narrow context rail, an aligned comparison band, a quiet index or a focused inspection surface when the task justifies it. Vary region size by importance and information, not to manufacture asymmetry. Resolve repeated container framing: if every section has the same card, padding, title and icon treatment, inspect whether the design has flattened different levels of meaning. Sometimes the correct repair is shared alignment and direct adjacency rather than another wrapper.

## 4. Make spacing and density intentional

Use the existing spacing system where coherent. Otherwise propose a small named scale, map its uses, and test dense and sparse views. A four-unit or eight-unit grid is a system choice, not a universal law.

| Input and work | Candidate density | Protect first | Typical failure to investigate |
|---|---|---|---|
| Touch, occasional task | Comfortable | Tappable areas, labels, separation | Desktop controls compressed onto phone |
| Pointer, repeated comparison | Compact option where useful | Readable values, alignment, navigation | Oversized cards hide comparative context |
| Keyboard, extended editing | Task-specific workspace | Focus, shortcuts, stable tool positions | Actions discoverable only on hover |
| Mixed input, tablet | Comfortable baseline with contextual efficiency | Touch access plus keyboard functionality | Width incorrectly treated as proof of mouse use |
| Magnification or large text | Flexible reflow | Content and operation at chosen size | Fixed heights clip or overlap text |

Apply density to the surfaces and tasks that need it. A compact data view must still retain readable labels, usable controls and clear group boundaries.

Run a grouping test: inspect the view without borders or shadows, then without color emphasis. Can related items still be recognized through position and proximity? If not, repair grouping before adding decoration. This is an audit technique, not a requirement to remove all containers.

Measure visible placement, actual interaction area and distance to adjacent targets separately. Compact visuals can coexist with larger hit areas only when those areas remain unambiguous; record overlap or unexpected activation.

## 5. Build a semantic token system

Inventory raw values and their actual roles before consolidation. Similar values may be intentional; identical values can serve different roles that need to diverge in another theme. Model primitive values, semantic roles, and justified component exceptions separately.

Suggested audit vocabulary, adapted to the project:

| Family | Roles to distinguish | Evidence of a defect |
|---|---|---|
| Color | Canvas, surface, text, border, action, status, selection, focus | One role changes arbitrarily or multiple meanings collide |
| Type | Body, label, heading, metric, code, annotation | Same function has accidental sizing or weight drift |
| Space | Related-item gap, group gap, region gap, page inset | Semantic groups become indistinguishable |
| Shape | Control, container, overlay, pill, media crop | Corners conflict without a functional or brand reason |
| Depth | Base, raised, overlay, modal background | Z-order contradicts what blocks interaction |
| Motion | Feedback, entrance, exit, continuity, reduction | Similar operations behave inconsistently |

Document supported theme and density combinations. Resolve hover, pressed, focus-visible, selected, disabled, loading, invalid, and read-only states by role rather than scattered component overrides. For a scoped token change, inspect affected consumers in both content-heavy and interaction-heavy views. In a full audit, inspect every usage and relevant configuration. A token change can make one screen look better while degrading another.

Separate component structure from permitted visual customization. Define which tokens and composition slots can vary without breaking behavior, semantics or shared consistency.

## 6. Audit typography as a working system

List each text role with family, size, weight, line height, tracking, width behavior, and fallback. Inspect actual rendered glyphs, not only CSS values. Include numerals, diacritics, punctuation, currency, dates, long names, identifiers, and required scripts. Confirm asset licensing before adding fonts.

Separate semantic structure from visual styling: a small section title can still be a heading, and a large metric is not automatically a heading. Define type roles as coherent property sets and distinguish product work from promotional display.

Typography acceptance checks:

- The most important reading content remains comfortable under the product's required viewing conditions.
- Labels remain distinguishable from values, hints, validation, and disabled content.
- Increased text size preserves the intended hierarchy and exposes complete actions.
- Text wrapping creates usable component heights; critical labels are not lost behind ellipses.
- Numeric comparisons align sensibly; use tabular numerals when the chosen font and task benefit.
- Fallback rendering remains legible and does not conceal controls before or after font loading.
- Code and identifiers remain copyable; their typography matches their need for precise discrimination.

Test readable weights, a purposeful range of type roles and user text enlargement. Do not assume native system text adaptation carries over to a web layout automatically.

Choose exact sizes through the existing system and rendered validation. There is no universal desktop body size, mathematically optimal scale, or “premium” font that fits every audience and application. Avoid replacing a functioning typography system merely to make a redesign visibly different.

Judge the typographic composition, not just token consistency. Establish deliberate contrast among page identity, section landmarks, working labels, values and annotations. Match line length and line height to the reading task; match numeral width and baseline alignment to comparison. Inspect whether large headings consume attention needed for work, or whether uniform small text has removed all landmarks. A system font can support excellent craft through weight, proportion, measure and placement; a distinctive typeface cannot rescue weak hierarchy.

## 7. Use color to communicate

Prepare a role map for each theme before judging the palette. Review actual foreground/background pairs, including translucent surfaces over moving content. Keep action, selection, focus, status, and brand identifiable as separate jobs even when they share a base hue. Test combinations in actual states rather than declaring a palette accessible from isolated swatches.

Assign colors semantic roles and verify them in each supported appearance. Test labels and context in target locales; a color’s meaning is not universally fixed.

Audit procedure:

1. Identify every use of color carrying meaning.
2. Find its accompanying text, icon, shape, pattern, position, or other interpretable cue.
3. Test the actual rendered contrast and the relevant accessibility requirement.
4. Check error, selection, focus, and hover combinations, including simultaneous states.
5. Verify dark and high-contrast presentations with real assets and background content.
6. Verify charts independently; a successful UI accent palette does not establish a usable categorical or quantitative scale.

Completion: meaningful colors have documented roles and validated combinations. Keep measured failures separate from aesthetic preferences about warmth, saturation, or fashionable palettes. Use a restrained accent strategy where it helps priority, but let a content-rich brand use expressive color when the evidence supports it.

Evaluate the distribution of color across the entire rendered page: which regions recede, which signals attract attention, and whether competing accents make ordinary information look urgent. Choose warmth, neutrality, saturation and light/dark relationships as a coherent direction grounded in product and brand. Do not apply a preferred dark theme, vivid gradient, accent hue or desaturated palette to every project. A safe palette is not automatically a compelling composition; inspect what its placement actually emphasizes.

## 8. Give shape, surfaces, and depth a purpose

Inspect radius, border weight, shadow, clipping, icon stroke, and nested geometry together. First determine whether an element is content, a control, a grouping surface, or an overlay. Then select its treatment. A pill can communicate a compact control; applying it to every object may erase useful distinctions. This is a hypothesis to check in the actual interface.

| Surface | Candidate visual treatment | Required check |
|---|---|---|
| Long-lived content | Quiet stable background, meaningful grouping | Reading and comparison remain clear |
| Clickable control | Recognizable affordance and state feedback | Resting state is discoverable |
| Raised contextual surface | Clear attachment or relationship to trigger | Scope and dismissal are understandable |
| Blocking dialog | Distinct foreground and background relationship | Visual blocking matches actual focus/interaction |
| Media overlay | Treatment validated over variable media | Labels remain readable at every relevant frame |

Research the material system actually selected for this project. Determine how it distinguishes content, controls, navigation and temporary surfaces across the relevant platform, theme and state; record observations in the [reference translation record](../assets/reference-translation.template.md). A native material and a browser approximation may behave differently. Explain applicable limits, inspect variable backdrops, and provide readable fallbacks. No named material system is a default for unrelated projects.

Craft check: inspect nested corners at normal scale, icon/text optical centering, mixed icon families, image crop intent, edge collisions, and visible click boundaries. A mechanically correct bounding box can still look misaligned. Correct a genuine visual imbalance with a documented local adjustment; keep the system understandable afterward.

Use shape and material to differentiate roles. A persistent work surface, editable control, temporary inspector and status marker need not share one radius, border and elevation. Specify their relationship before tuning values. Inspect whether repeated rounded panels make an expert workspace feel fragmented, or whether removing all boundaries makes a dense screen indistinct. Resolve the concrete failure; neither flatness nor depth is a universal sign of quality.

## 9. Compose components and widgets deliberately

For control anatomy, selectors, checkbox/radio behavior, complete interaction states, badges, messages and icon finish, read [component-states.md](component-states.md). Bind each applicable component state to the confirmed user brand contract; neither native defaults nor fashionable glass treatment automatically satisfy that contract.

For each repeated component, create a compact specification: purpose, inputs, variants, states, action scope, content rules, keyboard behavior, responsive behavior, and failure cases. Share behavior and meaning before forcing unlike tasks into one visual component.

Choose a list when items mainly need scanning, a table when aligned attributes support comparison, and cards when distinct content or media benefits from independent grouping. Treat this as a task hypothesis. Review nested cards, repeated badges, unlabeled icons, decorative charts, and redundant separators for whether they add information or merely compete for attention.

For a dashboard widget, identify its decision, time period, units, freshness, source and path to detail. Keep unavailable or stale data distinct from zero. Show partial failure at the affected scope. Offer layout configuration when work differs meaningfully between users, and preserve existing configuration capabilities.

A library’s accessibility support still needs correct composition, labels, headings, content and keyboard behavior. Verify the installed components in their actual host context.

## 10. Make motion explain change

Assign every animation a job: acknowledge input, connect origin and destination, expose a change, preserve spatial understanding, or communicate progress. If no job can be stated, classify it as decorative and decide whether it earns its visual and performance cost.

Test interruption, reversal, repeated input, slow hardware, asynchronous completion and reduced motion. A transition must not hide current state or delay the next useful action. Preserve meaningful state changes without requiring depth effects or movement.

Use expressive color, shape, scale and motion to direct attention only when they support the task. Preserve recognizable structure and useful labels; verify the result rather than transferring success claims from another product.

## 11. Finish with evidence, not a style score

For substantial concepts, require rendered review at all targeted device classes and inspect intermediate changes in composition. Keep the evidence for the selected direction together with its visual thesis, meaningful alternatives and self-critique. Missing rendering remains an open craft check. Functional evidence and visual assessment must be reported separately: an implementation can work correctly while its layout, rhythm, palette, forms and workflow presentation still fail the design brief.

Review at two scales. At page scale, judge hierarchy, balance, information density, grouping and the path through the task. At detail scale, judge typography, optical alignment, color relationships, component geometry, icons and state treatment. Correct the most consequential visible weaknesses and rerender before requesting approval. Record the owner's response without turning a taste judgment into a universal law. If the direction is rejected, reopen the affected composition and visual decisions; technical conformance does not overturn that rejection.

For each changed pattern, retain before/after evidence under matching content and conditions. Verify the affected component states and consuming routes; full audits inspect every documented usage and relevant configuration. Record remaining coverage gaps explicitly. An overall numerical score must never hide a critical unresolved issue.

Completion requires a coherent visual contract, accounted-for states, resolved or prioritized defects, proportional regression checks and an honest separation of measured outcomes from expert judgment.
