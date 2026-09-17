# Component anatomy, states and visual finish

Use when inspecting or refining buttons, fields, selectors, checkboxes, radios, switches, menus, badges, messages, icons and dialog or drawer families. This module connects their visual details to behavior and the user's brand contract. It supplements [visual systems](visual-systems.md), [accessibility](accessibility.md), [workflows](workflows.md) and [web engineering](web-engineering.md); it does not replace their requirements. Procedures and decision tables below are original working methods. Research the requested design language and applicable implementation before applying its treatment; no appearance or surface placement is universal.

## Bind the brand to the control

A contemporary page can still contain unfinished controls. Inventory each component family, its actual variants and consuming contexts. Include native controls, library wrappers and local overrides. A narrow fix covers affected uses; a full audit covers every discovered usage and applicable state, following [audit-method.md](audit-method.md).

Translate confirmed brand preferences into a component contract before polishing isolated screenshots. Carry forward approved decisions; do not reopen the interview or introduce a new approval gate for a focused repair.

Link the active requirement and reference-rule IDs from [requirements-conformance.md](requirements-conformance.md) and [project-research.md](project-research.md). Compare a demanding real usage, its open states and relevant transitions with those rules before propagating the family. Reuse this evidence in the state board; an inherited library style or working handler does not establish visual fidelity.

Record the applicable contract parts:

| Contract part | Concrete decision |
| --- | --- |
| Identity and role | Family, variant, task, accessible role, permission context and contract ID |
| Geometry | Height behavior, density, hit area, corner profile, inset, label/icon gap and popup attachment |
| Visual anatomy | Label/value/help, optional icon, surface, boundary, selection mark, focus indicator and progress slot |
| State mapping | For each applicable state: foreground, surface, border, shadow/highlight, icon, motion and semantic state |
| Environment | Theme, contrast/transparency alternatives, input methods, locale and container-width behavior |
| Traceability | Relevant user preference, resolved token values, approved reference and evidence per changed use |

Names such as `control.primary.pressed.surface` are a possible vocabulary, not required tokens. Resolve them to actual project values and rendered examples. “Modern,” “subtle” or “glassy” alone cannot close a contract row. Distinguish a control's visible shape from its hit area; enlarge the latter without overlapping neighboring actions.

Apply the user's chosen material, shape and motion language to the agreed families and states, including justified exceptions and accessible alternatives. No glass, flat treatment, spring motion, capsule shape or palette is a default. See [navigation and materials](navigation-and-materials.md) for the surface contract.

### One agreed contract across the component family

First classify the actions below; then apply shared behavior within each resulting family. When the user chooses a shared interaction pattern, persist its exact family and scope before changing individual usages. For an editing surface, define placement and attachment, modal or nonmodal behavior, width and responsive transformation, header and close placement, action order, save/cancel and dirty-state behavior, opening/closing motion, reduced-motion alternative, initial focus and focus return. A drawer, centered dialog or inline editor can each be appropriate; the user's agreed choice governs the affected product, not future unrelated projects.

Enumerate every affected opening path, including local implementations, newly added modules, portals and conditional role/state branches. Follow the actual rendered path: two buttons named “Edit” may open different implementations. Include the selected family contract in delegated work and use one shared primitive or a deliberate adapter where practical. Multiple libraries or local wrappers must not silently create competing behavior. If separate implementations are necessary, verify each against the same observable contract.

Record exceptions with their task reason, affected usages and decision status. Apply already approved exceptions without asking again. An exception that changes an approved family rule remains a proposal until the relevant user decision is obtained; routine corrections that fulfill the rule need no new approval. Keep unfinished usages as gaps rather than treating their old behavior as an implicit exception. Use the [design contract](../assets/design-contract.template.md) and repeat the [integration verification](verification.md#verify-component-families-after-integration) after affected modules change.

## Choose behavior before styling its shell

“Dropdown” describes an appearance, not a complete interaction contract. Before implementing or propagating a surface, record **verb → target → owning workspace → immediate result → surface → dismissal/return** for each affected action in the [design contract](../assets/design-contract.template.md). Inspect what its handler actually does; a button label alone is insufficient.

| Intent | Surface decision | Failure to reject |
| --- | --- | --- |
| Perform a reversible, fully specified command | Execute directly and show scoped feedback | An intermediate panel containing only another button for the same command |
| Reveal a short set of commands | Anchored action menu with the established menu keyboard contract | Treating the command list as an object editor or a chain of navigation panels |
| Adjust a small set of independent display choices | Anchored checkable menu or compact settings popover, according to the contents and save semantics | A full editor for every visibility toggle, or merging independent choices into one option |
| Choose a value | Select, listbox or combobox as specified below | A command menu whose rows silently behave like form values |
| Edit a data object or inspect substantial detail | The agreed editor or inspector family, scoped to its workspace | Opening it merely because every button was assigned the same visual shell |
| Resolve a consequential decision | A proportionate confirmation surface when the consequence warrants it | Applying a confirmation step to ordinary reversible choices for consistency |

These are task criteria, not an absolute ban on a surface type. Content, input and the approved product contract may justify another choice; record the reason. Direct routes and visible frequent controls can avoid an overflow entirely. For a menu containing form controls, use appropriate popover/form semantics instead of claiming an application-menu role for arbitrary content. Do not add a generic menu → panel → action chain when one reveal and one choice can complete the same work. Define dismissal by intent: a chosen command normally closes its menu and exposes the result; a group of independent display choices can remain open so several options can be adjusted together. Preserve feedback, Escape/outside dismissal and focus return without forcing repeated reopening. Verify the chosen primitive's actual keyboard and selection contract.

The owning workspace constrains geometry as well as state. A nested editor or recipient picker inside a docked tool belongs to that tool's usable region; it must not become an application-wide overlay merely because a global drawer component is available. Define its docked, expanded and compact transformations, including insufficient-space fallback, focus, drafts and return. A deliberate task-context change can use a wider surface, but is a separate decision. Verify every supported container mode; viewport width alone does not establish available space.

| Task | Candidate | Preserve or verify |
| --- | --- | --- |
| Choose one value from a fixed set; compact presentation matters | Native select when suitable | Label, selected value, platform picker, keyboard, validation and form behavior |
| Compare a short set of mutually exclusive choices | Radio group | Group question, option descriptions, one selection, arrow-key behavior and no misleading multi-select appearance |
| Keep choices visible; select one or several | Listbox | Explicit selection model, focus versus selection, type-ahead and scrolling; use a different pattern for options containing independent controls |
| Search a long set or optionally enter a value | Editable combobox | Whether free text is accepted, query versus committed value, suggestions, no results, async loading/failure, clearing and Escape |
| Invoke commands or choose a related action | Menu button or split button | Named trigger, expanded state, command keyboard behavior and focus return; route links are not automatically an application menu |
| Choose independent options, consent or batch membership | Checkbox/group | Checked, unchecked and meaningful mixed state; label target, group scope and validation |
| Toggle a setting with immediate effect | Switch where the saving contract fits | On/off meaning, pending result, failed change and rollback; a staged checkbox may fit a Save-based form better |
| Toggle a tool or mode | Toggle button | Persistent on/off indication and semantic state, separate from transient press feedback |

Distinguish choosing a form value, activating a command and entering a searchable value. A native select, command menu, listbox and combobox have different keyboard and focus contracts; select the semantic pattern before styling it.

Do not replace native behavior simply to remove an unfamiliar browser outline or match a mockup. Style supported parts or use the existing proven primitive first. A custom selector needs a complete keyboard, focus, assistive-technology, touch, form and state contract, tested in its actual portals/dialogs and supported browsers. A beautiful closed trigger with an untested popup is unfinished. Platform-owned picker appearance can be an intentional exception, recorded in the brand contract.

## State and context matrix

Not every row applies to every family. These are intersecting states and contexts, not a flat enum or an instruction to generate every possible combination. Plan the reachable cases and meaningful intersections; preserve finite coverage obligations and explicit gaps.

| State/context | Observable visual treatment | Behavior and evidence |
| --- | --- | --- |
| Rest | Discoverable affordance; stable label, value and boundary | Can the user identify the action without first hovering? |
| Hover | Local, legible emphasis consistent with the brand | No layout jump, accidental activation or exclusive access to an action/help |
| Keyboard focus | Distinct indicator surviving selection, error and overlays | Visible location, correct order and keys; no removed browser outline without an adequate replacement |
| Press/active | Immediate feedback distinct from selection | Pointer/touch/keyboard activation and cancellation follow the control contract; release outside does not accidentally commit |
| Selected/checked | Durable mark or state cue plus correct value | Survives focus moving away; programmatic state agrees with the visible state |
| Mixed/indeterminate | Recognizable partial-selection mark | Reflects the actual child set and defined next action; not a decorative third switch position |
| Expanded/open | Trigger state and attached popup remain intelligible | Opening focus, dismissal, return, collision, scroll and clipping work in the real container |
| Disabled/unavailable | Availability differs from enabled and read-only | No activation; reason remains reachable without hover. Choose native disabled or a correctly enforced focusable unavailable pattern deliberately |
| Read-only | Value remains legible and inspectable | Editing is unavailable without falsely suggesting missing data; do not invent unsupported native read-only attributes |
| Pending/loading | Stable footprint, bounded progress feedback | Avoid duplicate intent and focus loss; expose pending status and eventual success/failure without claiming early success |
| Error/invalid | Field or action scope, textual issue and recovery | Error coexists with focus and retained input; destructive styling alone does not mean validation failed |
| Forced colors/high contrast | State marks and focus remain identifiable if fills/shadows disappear | Test actual mode; do not make box-shadow or translucency the only boundary/state cue |
| Touch/no hover | Clear labels, usable targets and direct access | All essential actions work without hover, precision pointing or a mandatory long press |
| Reduced motion/transparency | Equivalent state feedback and readable surfaces | Removing motion/blur does not remove meaning, controls or completion feedback |

Test selected+focused, invalid+focused, selected+disabled, pending after activation and an open popup near the viewport edge where reachable. These counterexamples often expose conflicting token layers. Preserve independent indicators instead of making the last CSS rule erase selection or focus. Include permitted and restricted role contexts with safe fixtures; visual visibility never proves backend authorization.

Model press, release, cancellation, hover, focus, selected, mixed and pending states explicitly when relevant. Pending is not automatically disabled: preserve focus and give meaningful progress feedback without allowing duplicate work.

Match action affordance to activation. When an enabled row, card or disclosure is presented as one action, its visible control surface and internal padding must activate that action. Otherwise, confine action feedback to the actual controls and distinguish separate actions. Preserve native semantics, required text interaction and independent child controls; avoid nested buttons/links or enlarged targets that intercept secondary actions. Decorative shadows and glows do not define a larger target. Use the [interaction probes](verification.md#minimum-useful-interaction-pass) to verify the apparent boundary.

## Make the small visual decisions deliberate

**Buttons.** Establish hierarchy within each action group: emphasis follows task importance, not the number of colors. Set label weight, icon balance, surface, boundary and press response together. Keep the footprint stable during progress and long translations. Distinguish ordinary, toggle, menu and split-button behavior; destructive intent needs explicit meaning rather than a recolored primary button.

**Fields and selectors.** Make editable value, placeholder, helper text, required/optional cue and error distinguishable. Align the trigger's chevron, clear action and status icon without creating overlapping hit regions. The open list needs the same level of finish as the closed field: option spacing, selected mark, focus, descriptions, dividers, empty result and loading treatment. Keep selection visible when filtering changes the result set.

**Checkboxes and radios.** Coordinate marker weight with adjacent text rather than scaling an icon to fill its square. Inspect unchecked boundaries, checked/mixed marks, disabled selection and wrapped-label alignment. The label should provide a useful target without swallowing unrelated links. A radio dot and a checkbox checkmark communicate different choice models; retain that distinction when changing shape and material.

**Borders, shadows and transparency.** Give each boundary a job: input affordance, group separation, selection or foreground separation. Avoid stacking an outline, dark shadow and highlight at equal strength around every object. Inspect nested corners at normal scale. Use elevation to explain layering, not as a universal modernity effect.

**Icons.** Use a coherent family, optical size, stroke/fill weight, cap/join language and baseline relationship. Compare narrow, wide, circular and asymmetric glyphs beside actual labels. Equal SVG boxes do not guarantee equal apparent size. Distinguish selection fill from decorative fill, and retain meaningful labels where the symbol is ambiguous. A chevron, warning mark and action icon have different jobs; avoid using one merely to fill an empty slot. Decoration must not create duplicate announcements.

**Motion.** Specify cause, affected layer, cancellation and reduced alternative. Press feedback should acknowledge input immediately; a spring or morph must not delay the action, move a target away or obscure the resulting state. Do not animate every streamed value or every item on ordinary rerender. Research the chosen system's actual motion behavior; a web approximation still requires independent state and performance verification.

## Relate corners instead of copying one radius

Choose whether each corner is independently fixed, a capsule end, or related to a nearby enclosing corner under the approved shape system. A button does not need the same numerical radius as its box. Concentricity concerns shared corner centers, not allegiance to a particular design language.

For **circular corners with a uniform inset**, use the geometric relationship `inner radius = outer radius − inset` while the result is positive. Original example: an outer radius of 24 CSS pixels and an 8-pixel edge-to-edge inset give a 16-pixel inner radius. These illustrate geometry, not recommended brand tokens. At zero or below, exact rounded concentricity is no longer possible; a square corner or deliberate minimum/fallback radius changes the relationship.

- Measure between corresponding rendered edges in the same coordinate system. If the reference is the parent's outer border edge, include its border thickness and all intervening padding/margin in the actual offset to the child's outer border edge. Do not subtract only CSS padding from an outer-border radius by habit.
- Apply the relationship only to nearby paired corners. A small button centered inside a large dialog does not inherit all four dialog corners. Top and bottom corners may have different roles; specify per-corner relationships and intentional minimum radii where needed.
- With unequal insets, elliptical corners, continuous curves or asymmetric shapes, one scalar subtraction does not prove a constant-width gap. Inspect each corner's horizontal/vertical relationship and silhouette. Record an optical adjustment as intentional rather than calling it exact concentricity.
- A horizontal capsule relates its end radius to half its own height; an independent control can retain that shape without matching the container. Recheck after wrapping, density changes and text enlargement. Do not force fixed height or truncate a label merely to preserve a preferred silhouette.
- In CSS, distinguish outer border, padding and content edges. Oversized radii can be proportionally reduced by the browser; the declared value is not always the used geometry.

Render the full composition and a corner close-up at supported zoom, widths and densities, with long labels and open overlays. Inspect even spacing, pinched/flared corners, clipping, focus-ring clearance and hit areas. CSS circular/elliptical radii approximate an intended relationship; they do not automatically reproduce a native continuous curve or container-shape algorithm. Preserve explicit brand departures and approved shape choices.

## Assign surfaces by role before choosing colors

Define semantic surface roles from the product's work and chosen system. Grouping and elevation describe different relationships; neither requires brightening every nested card. Research the relevant platform or corporate guidance instead of treating a sampled screenshot color as a cross-platform palette.

| Surface role | Contract and rendered check |
| --- | --- |
| Base workspace/document | Set the reading/media context; inspect large-area tone in both themes without assuming pure black, white or a brand-colored wash |
| Grouped content | Distinguish related groups through spacing and an appropriate surface relationship; do not simulate elevation for every subdivision |
| Elevated sheet/popover | Preserve separation from the actual underlying surface; verify foreground contrast, modality and inactive/background context where applicable |
| Content treatment | Supply contextual separation with legibility suited to text/detail density |
| Navigation/control layer | Define separation from content and the allowed surface response; if translucent, inspect its actual changing backdrop |
| Selected/pressed/semantic state | Keep state and brand accent separate from the base surface; selection must remain recognizable when focus or error coexists |
| Reduced-effect/contrast fallback | Retain grouping, state, labels and focus when transparency or shadows disappear |

Check how adjacent and overlapping surface treatments interact. A selected control may need a state fill rather than another material layer. Derive that choice from the approved language and rendered result, not a universal ban or mandate for an effect.

Specify foreground, fill, backdrop, edge and shadow together. Use an outline or shadow when it supplies necessary recognition or layering, not on every surface automatically. Inspect static and scrolling states over light, dark, saturated and busy content, plus disabled/pending/open states. Record CSS values and their source or product rationale; neither a hex palette nor effect parameters alone establish reference fidelity.

Verify which surface is actually painted. Inspect the primary content region and its ancestor backgrounds, not only a token declaration: a transparent region may inherit a different backdrop from the intended role. Check the relative area, tone and contrast of content, grouping and chrome in every supported theme. The skill supplies no white, black or tinted background default. Research the user-selected reference for this project and verify the derived surface rules in actual usage; previous project examples are not production defaults.

## Separate signals from decoration

Reserve semantic roles for information, success, warning, error and destructive intent independently of brand accent. A red brand does not make every primary action destructive; a green selected filter does not prove an operation succeeded. Verify meaning with labels/icons and actual outcome, not hue alone.

A badge needs a reason: count, unread indication, status or a meaningful attribute. Define zero, unknown, stale and capped-count behavior; a cap must not imply an exact value. Distinguish numeric counts from compact descriptive labels. A noninteractive marker should not look actionable; editable status needs an explicit trigger and states.

| Message purpose | Candidate presentation | Required distinction |
| --- | --- | --- |
| Local explanation | Helper text or inline information | Useful context without urgency or forced interruption |
| Correctable field error | Persistent field message, summary when useful | What failed, where and how to correct it |
| Section failure | Message attached to affected region | Retained data, unavailable work and a specific recovery action |
| Background success | Quiet status or appropriate transient confirmation | Actual completion; important result remains retrievable |
| System-wide problem | Prominent shared message | Real scope and consequences, rather than a generic page decoration |
| Immediate consequential decision | Dialog only when the workflow needs it | Decision, consequences, alternatives and focus/return contract |

Compose icon, title, explanation, action and dismissal as one hierarchy. Disclose lengthy technical detail separately while keeping the actionable message visible. Visual prominence does not automatically justify `role="alert"`; match announcement urgency to the actual change. Dismissal must not imply resolution. Use [accessibility.md](accessibility.md) for semantic verification.

## Prove the finish in context

Create a small rendered state sheet with actual labels and approved tokens, then exercise those controls in their consuming tasks. Compare resting, selected, focused, unavailable and error treatments side by side. Test meaningful compound states, supported themes, density changes, long labels, touch and keyboard. Use the actual container and background; an effect over an empty canvas does not demonstrate legibility over changing content.

Record each defect as family/use/state, observed symptom, violated contract, proposed change and reproduction. Propagate a shared fix, then verify every affected usage in the declared audit scope. A gallery, source inspection or passing CI cannot close missing runtime obligations. Follow [verification.md](verification.md) for actual delivery-surface inspection and distinguish functional correctness, visual acceptance and user approval.

Source limitation: vendor design pages can require client rendering or indexed primary text. Implementation documents establish behavior for their named libraries, not shared APIs or the newest appearance across systems. Recheck the requested system, installed version and relevant primary documentation before adopting its behavior. No source assets or component implementations are copied here.
