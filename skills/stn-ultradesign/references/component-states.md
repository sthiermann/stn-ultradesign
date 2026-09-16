# Component anatomy, states and visual finish

Use when inspecting or refining buttons, fields, selectors, checkboxes, radios, switches, menus, badges, messages and icons. This module connects their visual details to behavior and the user's brand contract. It supplements [visual systems](visual-systems.md), [accessibility](accessibility.md), [workflows](workflows.md) and [web engineering](web-engineering.md); it does not replace their requirements. Procedures and decision tables below are original synthesis. Vendor examples describe particular systems, not universal standards. Primary sources checked 2026-09-16.

## Bind the brand to the control

A contemporary page can still contain unfinished controls. Inventory each component family, its actual variants and consuming contexts. Include native controls, library wrappers and local overrides. A narrow fix covers affected uses; a full audit covers every discovered usage and applicable state, following [audit-method.md](audit-method.md).

Translate confirmed brand preferences into a component contract before polishing isolated screenshots. Carry forward approved decisions; do not reopen the interview or introduce a new approval gate for a focused repair. Record:

| Contract part | Concrete decision |
| --- | --- |
| Identity and role | Family, variant, task, accessible role, permission context and contract ID |
| Geometry | Height behavior, density, hit area, corner profile, inset, label/icon gap and popup attachment |
| Visual anatomy | Label/value/help, optional icon, surface, boundary, selection mark, focus indicator and progress slot |
| State mapping | For each applicable state: foreground, surface, border, shadow/highlight, icon, motion and semantic state |
| Environment | Theme, contrast/transparency alternatives, input methods, locale and container-width behavior |
| Traceability | Relevant user preference, resolved token values, approved reference and evidence per changed use |

Names such as `control.primary.pressed.surface` are a possible vocabulary, not required tokens. Resolve them to actual project values and rendered examples. “Modern,” “subtle” or “glassy” alone cannot close a contract row. Distinguish a control's visible shape from its hit area; enlarge the latter without overlapping neighboring actions.

A user's request for prominent glass is a product preference. Apply it to the agreed families and states with readable content backing and an opaque alternative; do not spread it automatically to all products or every control. Conversely, an approved restrained brand should not acquire glass, spring motion or capsule shapes through incidental implementation choices. See [navigation and materials](navigation-and-materials.md) for the surface contract.

## Choose behavior before styling its shell

“Dropdown” describes an appearance, not a complete interaction contract.

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

Fluent distinguishes a form select from a custom dropdown and an input-enabled combobox. Use that distinction, without importing its library-specific props as a cross-platform rule. [Fluent dropdown](https://fluent2.microsoft.design/components/web/react/core/dropdown/usage), [Fluent combobox](https://fluent2.microsoft.design/components/web/react/core/combobox/usage). WAI's informative patterns describe [listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/) and [combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) behavior; they are not automatic certification.

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

Google's Compose guidance treats press, release, cancellation, hover and focus as interactions whose visual response can be customized. Adobe's current Spectrum 2 Button distinguishes pending from ordinary disabled state while retaining focusability and exposing pending feedback. These illustrate why state behavior must survive restyling. [Compose interactions](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/handling-interactions), [Spectrum 2 Button](https://react-spectrum.adobe.com/Button). Spectrum 2 also exposes distinct checkbox selection/mixed state and radio-group behavior. [Checkbox](https://react-spectrum.adobe.com/Checkbox), [RadioGroup](https://react-spectrum.adobe.com/RadioGroup).

## Make the small visual decisions deliberate

**Buttons.** Establish hierarchy within each action group: emphasis follows task importance, not the number of available colors. Set label weight, icon balance, surface, boundary and press response together. Keep the footprint stable during progress and long translations. Destructive intent needs its own semantic treatment and explicit wording; it is not merely the primary brand button tinted differently. Fluent provides useful distinctions among ordinary, toggle, menu and split buttons. [Fluent Button](https://fluent2.microsoft.design/components/web/react/core/button/usage).

**Fields and selectors.** Make editable value, placeholder, helper text, required/optional cue and error distinguishable. Align the trigger's chevron, clear action and status icon without creating overlapping hit regions. The open list needs the same level of finish as the closed field: option spacing, selected mark, focus, descriptions, dividers, empty result and loading treatment. Keep selection visible when filtering changes the result set.

**Checkboxes and radios.** Coordinate marker weight with adjacent text rather than scaling an icon to fill its square. Inspect unchecked boundaries, checked/mixed marks, disabled selection and wrapped-label alignment. The label should provide a useful target without swallowing unrelated links. A radio dot and a checkbox checkmark communicate different choice models; retain that distinction when changing shape and material.

**Borders, shadows and transparency.** Give a boundary a job: input affordance, group separation, selection or foreground separation. Avoid stacking outline, dark shadow and highlight at equal strength around every object. Inspect nested radii and corners at normal scale. Use shadows where layering needs explanation, not as a universal modernity effect. Material Web's M3 buttons expose several emphasis treatments and reserve elevation for useful separation; its theming API is an implementation example, not a requirement to adopt that library or its default shapes. [Material Web buttons](https://material-web.dev/components/button/).

**Icons.** Use a coherent family, optical size, stroke/fill weight, cap/join language and baseline relationship. Compare narrow, wide, circular and asymmetric glyphs beside actual labels. Equal SVG boxes do not guarantee equal apparent size. Distinguish selection fill from decorative fill, and retain meaningful labels where the symbol is ambiguous. A chevron, warning mark and action icon have different jobs; avoid using one merely to fill an empty slot. Decoration must not create duplicate announcements.

**Motion.** Specify cause, affected layer, cancellation and reduced alternative. Press feedback should acknowledge input immediately; a spring or morph must not delay the action, move a target away or obscure the resulting state. Do not animate every streamed value or every item on ordinary rerender. Apple's Liquid Glass guidance describes responsive material behavior, while its WWDC26 discussion recommends appropriate native button styles instead of applying a raw glass effect indiscriminately. A web approximation still requires independent state and performance verification. [Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/), [SwiftUI Group Lab, 7:21](https://developer.apple.com/videos/play/wwdc2026/8120/).

## Relate corners instead of copying one radius

Choose whether each corner is independent, a capsule end, or related to a nearby enclosing corner. A button does not need the same numerical radius as its box. Apple distinguishes fixed, capsule and concentric shapes, including compact rounded rectangles on macOS. Concentricity concerns shared corner centers. [Design system, WWDC25](https://developer.apple.com/videos/play/wwdc2025/356/), [SwiftUI design, WWDC25](https://developer.apple.com/videos/play/wwdc2025/323/)

For **circular corners with a uniform inset**, use the geometric relationship `inner radius = outer radius − inset` while the result is positive. Original example: an outer radius of 24 CSS pixels and an 8-pixel edge-to-edge inset give a 16-pixel inner radius. These are illustrative values, not Apple tokens. At zero or below, exact rounded concentricity is no longer possible; a square corner or deliberate minimum/fallback radius changes the relationship.

- Measure between corresponding rendered edges in the same coordinate system. If the reference is the parent's outer border edge, include its border thickness and all intervening padding/margin in the actual offset to the child's outer border edge. Do not subtract only CSS padding from an outer-border radius by habit.
- Apply the relationship only to nearby paired corners. A small button centered inside a large dialog does not inherit all four dialog corners. Top and bottom corners may have different roles; Apple's configurable shapes explicitly support per-corner choices and minimum radii. [ConcentricRectangle](https://developer.apple.com/documentation/swiftui/concentricrectangle)
- With unequal insets, elliptical corners, continuous curves or asymmetric shapes, one scalar subtraction does not prove a constant-width gap. Inspect each corner's horizontal/vertical relationship and silhouette. Record an optical adjustment as intentional rather than calling it exact concentricity.
- A horizontal capsule relates its end radius to half its own height; an independent control can retain that shape without matching the container. Recheck after wrapping, density changes and text enlargement. Do not force fixed height or truncate a label merely to preserve a preferred silhouette.
- In CSS, distinguish outer border, padding and content edges. Oversized radii can be proportionally reduced by the browser; the declared value is not always the used geometry. [CSS corner shaping and overlap](https://www.w3.org/TR/css-backgrounds-3/#corners)

Render the full composition and a corner close-up at supported zoom, widths and densities, with long labels and open overlays. Inspect even spacing, pinched/flared corners, clipping, focus-ring clearance and hit areas. CSS circular/elliptical radii approximate an intended relationship; they do not automatically reproduce a native continuous curve or container-shape algorithm. Preserve explicit brand departures and approved shape choices.

## Assign surfaces by role before choosing colors

Apple's semantic colors distinguish system and grouped backgrounds; iOS/iPadOS Dark Mode additionally distinguishes base and elevated presentation. These are different dimensions, not a rule to brighten every nested card. macOS has its own semantic roles. A sampled screenshot color is not a cross-platform palette. [Apple color](https://developer.apple.com/design/human-interface-guidelines/color), [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)

| Surface role | Contract and rendered check |
| --- | --- |
| Base workspace/document | Set the reading/media context; inspect large-area tone in both themes without assuming pure black, white or a brand-colored wash |
| Grouped content | Distinguish related groups through spacing and an appropriate surface relationship; do not simulate elevation for every subdivision |
| Elevated sheet/popover | Preserve separation from the actual underlying surface; verify foreground contrast, modality and inactive/background context where applicable |
| Standard material | Supply contextual separation within content with legibility suited to text/detail density |
| Liquid Glass/chrome | Define the functional layer, actual backdrop and allowed material response; a translucent fill over a flat canvas proves little about moving content |
| Selected/pressed/semantic state | Keep state and brand accent separate from the base surface; selection must remain recognizable when focus or error coexists |
| Reduced-effect/contrast fallback | Retain grouping, state, labels and focus when transparency or shadows disappear |

Apple's material guidance separates standard content materials from functional glass. For an Apple-aligned baseline, avoid independent glass effects stacked on each other; controls within a glass group can use state fills rather than another glass sheet. User-approved departures remain product choices. [Materials](https://developer.apple.com/design/human-interface-guidelines/materials)

Specify foreground, fill, backdrop, edge and shadow together. Use an outline or shadow when it supplies necessary recognition or layering, not on every surface automatically. Inspect static and scrolling states over light, dark, saturated and busy content, plus disabled/pending/open states. Record exact CSS values as project approximations with evidence; neither a hex palette nor blur parameters establish native Apple fidelity.

Verify which surface is actually painted. Inspect the rendered primary content region and its ancestor backgrounds, not only a token declaration: a white content token cannot help if transparent content inherits a gray canvas. For an Apple-led light appearance, distinguish ordinary white content from grouped backgrounds; Apple's `systemBackground` explicitly covers white-primary light interfaces, while grouped colors serve a different composition. Do not turn that distinction into an all-white rule for every brand or map a UIKit token literally onto macOS or CSS. Check the relative area and contrast of content, grouping and chrome in the actual light and dark layouts. [System background](https://developer.apple.com/documentation/uikit/uicolor/systembackground), [Grouped background](https://developer.apple.com/documentation/uikit/uicolor/systemgroupedbackground)

## Separate signals from decoration

Reserve semantic roles for information, success, warning, error and destructive intent independently of brand accent. A red brand does not make every primary action destructive; a green selected filter does not prove an operation succeeded. Verify meaning with labels/icons and actual outcome, not hue alone.

A badge needs a reason: count, unread indication, status or a meaningful attribute. Define zero, unknown, stale and capped-count behavior; a cap must not imply an exact value. Do not add decorative “active,” “new” or “premium” pills to every row. A noninteractive marker should not appear to be a button. If a status can be changed, give its trigger explicit interactive semantics and states. Atlassian distinguishes numeric badges from meaningful compact labels; its exact appearances remain vendor choices. [Badge](https://atlassian.design/components/badge), [Lozenge](https://atlassian.design/components/lozenge).

| Message purpose | Candidate presentation | Required distinction |
| --- | --- | --- |
| Local explanation | Helper text or inline information | Useful context without urgency or forced interruption |
| Correctable field error | Persistent field message, summary when useful | What failed, where and how to correct it |
| Section failure | Message attached to affected region | Retained data, unavailable work and a specific recovery action |
| Background success | Quiet status or appropriate transient confirmation | Actual completion; important result remains retrievable |
| System-wide problem | Prominent shared message | Real scope and consequences, rather than a generic page decoration |
| Immediate consequential decision | Dialog only when the workflow needs it | Decision, consequences, alternatives and focus/return contract |

Compose icon, title, explanation, action and dismissal as one hierarchy. Give lengthy technical detail a secondary disclosure while keeping the actionable message visible. A visually prominent alert container does not automatically require `role="alert"`; use announcement urgency appropriate to the actual change. Dismissing a message must not imply resolving the fault. [Atlassian message guidance](https://atlassian.design/foundations/content/designing-messages) supplies vendor examples; [accessibility.md](accessibility.md) governs the evidence and standards distinction.

## Prove the finish in context

Create a small rendered state sheet with actual labels and approved tokens, then exercise those controls in their consuming tasks. Compare resting, selected, focused, unavailable and error treatments side by side. Test meaningful compound states, both supported themes, density changes, long labels, touch and keyboard. Use the actual container and background; glass over an empty canvas does not demonstrate legibility over moving content.

Record each defect as family/use/state, observed symptom, violated contract, proposed change and reproduction. Propagate a shared fix, then verify every affected usage in the declared audit scope. A gallery, source inspection or passing CI cannot close missing runtime obligations. Follow [verification.md](verification.md) for actual delivery-surface inspection and distinguish functional correctness, visual acceptance and user approval.

Source limitation: several Apple HIG, Material 3 and Spectrum design pages require client rendering in this research tool. The linked Apple transcripts, Material Web/Compose and current Spectrum 2 implementation documents supplied readable primary evidence; they do not establish that every platform shares the same API or latest visual revision. Some Atlassian component summaries were available through indexed primary pages. Recheck the installed system and relevant release documentation before adopting library-specific behavior. No source assets or component implementations are copied here.
