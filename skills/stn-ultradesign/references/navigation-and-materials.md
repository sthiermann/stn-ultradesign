# Navigation and materials

Read for app shells, overloaded settings, adaptive navigation, contextual panes, floating controls, translucent materials, or motion that changes perceived hierarchy. Apply this module within the current audit, concept, or implementation scope. An audit diagnoses; it does not authorize a redesign. Follow [discovery-and-preferences.md](discovery-and-preferences.md), [feature-parity.md](feature-parity.md), and [concept-to-code.md](concept-to-code.md) when proposing substantial changes.

The decision tables and review procedures are original working methods. Research the user’s requested system and applicable version before deriving its visual contract; the skill does not prescribe a default language or material.

## 1. Separate the authority of each decision

| Evidence class | What it establishes | What it does not establish |
|---|---|---|
| Platform guidance | Familiar behavior and native framework conventions for the stated platform | A universal layout rule for every browser app |
| WCAG requirement | A testable accessibility requirement at a specified conformance level | A preferred brand, material, or navigation architecture |
| CSS specification | Defined web behavior and syntax, subject to specification status | Uniform browser support or a native rendering equivalent |
| Product decision | A justified arrangement for this domain, audience, and task | A worldwide standard merely because the result looks current |

Establish the requested brand or design language first. Research its current primary guidance, relevant actual interfaces, component states and platform constraints; identify the specific expression the user wants, which may differ from the newest release. Translate observations into testable product rules and intentional departures using [brand-discovery.md](brand-discovery.md). Do not silently inherit a style from another project.

For a web application, describe custom materials as the product's implementation. A matching effect does not establish native optical, input, accessibility or window-management equivalence. A platform reference does not override the approved concept.

## 2. Define the navigation model before the shell

Inventory destinations and commands separately. For each item, record its scope, frequency, parent, authorized roles, state to preserve, and return destination. Classify it as one of these:

- **App destination:** a stable area such as Projects or Reports.
- **Collection or object:** an entity and its detail, history, or relationships.
- **Local view:** an alternative representation of the current subject.
- **Command:** something that changes, creates, exports, or otherwise acts on the subject.
- **Contextual inspector:** secondary information or editing that depends on a selected subject.
- **Preference:** a persistent choice, with its user, workspace, or system scope stated.

An app destination, open document and action can all look tab-shaped while requiring different behavior. Make those differences explicit in labels, semantics, selection and close behavior. A styled selected item is not proof of a working route.

| Pattern | Use when | Specify before approving |
|---|---|---|
| Labeled sidebar | Frequent switching across broad areas or collections benefits from a visible map | Current location, grouping, expansion, pin/collapse, overflow, keyboard path |
| Compact rail | Space is constrained and the destinations remain recognizable | Accessible labels, a discoverable expansion path, no hover-only identification |
| Bottom navigation | A compact window needs frequent access to a small stable set of peer destinations | Labels, selected state, per-destination history, keyboard and safe-area behavior |
| Navigation stack | People move from a collection or category to a focused detail | Parent, history, deep link, return position, draft handling |
| List/detail panes | Comparing or selecting objects benefits from concurrent context | Selection, pane widths, empty detail, narrow-window transformation |
| Supporting pane or inspector | Secondary context directly supports the primary task | Object scope, show/hide control, focus, whether the main task stays usable |
| Drawer or sheet | A bounded secondary task benefits from temporary space | Modal or nonmodal behavior, dismiss rules, explicit save semantics where applicable |
| Dialog | A short decision needs an interruption | Why interruption is necessary, consequences, cancel, focus return |

These are candidates, not a hierarchy of fashionable components. A long, independently navigable settings section may need a page even when smaller contextual editors use drawers. Do not force every form into a side panel.

Distinguish navigation between destinations from action toolbars and local views. Keep eligible destinations stable across empty/loading states; role-based availability still follows the product's access model. Preserve per-destination context when navigation changes form. Neither a universal destination count nor a particular tab silhouette follows from these requirements.

## 3. Adapt hierarchy, not just component width

Use actual width and height, text scale, input capabilities, window state and task needs. Navigation may change form while retaining destinations and state; a library default is not a mandatory breakpoint.

**Wide workspace:** expose labeled navigation if it improves repeated switching. Keep object actions near their object. Offer deliberate collapse or pinning where the product needs it; retain the user's chosen state at the agreed scope. Avoid tiny icon-only navigation as an automatic synonym for sophistication.

**Intermediate workspace:** allocate space to useful relationships, such as category/detail or collection/selected object. When two panes no longer work with real labels and forms, transition to a sequential flow. Do not preserve desktop columns by squeezing the primary task.

**Compact workspace:** show one main task context with a clear path back. Global destinations and local editing actions must remain distinguishable. Avoid stacking app header, breadcrumbs, section tabs, filter bar, oversized title, and persistent save footer by default. Decide which context must stay visible and which can appear on demand.

A sidebar can expose peer collections while related panes show deeper context. Evaluate discoverability, selection and available space together. Do not import a vendor's icon colors, floating treatment or dimensions merely because its navigation structure is useful.

### Decongest settings without losing features

Choose the entry and switching pattern from actual work, rather than making every device use the same sequence:

| Pattern | Favor when | Avoid or adapt when |
|---|---|---|
| Persistent local navigation beside selected content | People repeatedly switch among peer settings and the available width supports readable navigation and forms | Long labels, enlargement or narrow windows leave too little usable content space; collapse or change presentation while retaining location |
| Landing-page directory | First visits, unfamiliar categories or infrequent setup benefit from descriptions and orientation | Experienced users must repeatedly return to the directory to change a neighboring setting; retain direct peer access or an agreed resume path |
| Sequential overview → area → detail | Compact space or a genuine parent-child task benefits from one context at a time | The sequence is imposed on a wide workspace despite frequent peer switching; do not add an intermediate page merely for visual consistency |

A global rail and adjacent settings sidebar are valid candidates when their scopes differ. For example, the global selection is Settings, the local selection is Notifications and its content is directly visible. Label both scopes, preserve coherent selections and test realistic forms, translations and text enlargement. Neither a one-sidebar limit nor two permanent rails is universal.

Preserve a working navigation pattern unless a requested change or a demonstrated task benefit justifies replacing it. Before introducing a directory or hiding local navigation, compare task entry to the first meaningful result, then switching from category A to B and C and returning with the relevant draft and position intact. Compare direct peer selection with Back → overview → next category. Minimize unnecessary actions, re-entry and hierarchy travel while checking recognition, content space and correctness. A tidy overview does not compensate automatically for repeated switching costs. Keep an approved compact hierarchy while evaluating the wide layout independently.

1. Map every existing setting to its scope, role, dependency, current value, and proposed location. Retain themes, languages, density choices, chart preferences, technical controls, and conditional features in that map.
2. Move frequent task-specific controls to the task when this improves access. Keep durable preferences in identifiable categories; put advanced explanations near the relevant choice.
3. In compact layouts that need sequential navigation, use a category index with useful summaries, then a focused category page and clear return. Search may supplement this structure; it must not become the only path to a feature.
4. In wider layouts with frequent peer switching, keep the same categories visible beside the selected content when space allows. A separate directory is optional orientation, not a mandatory stop. Keep section names and settings identity stable across sizes.
5. Distinguish immediately applied personal preferences from staged changes. Where the approved workflow requires Save, show a coherent change review and dirty state; explain scope before committing.
6. Test return navigation after editing, validation failure, cancellation, and resize. A cleaner screen must not hide an unsaved change or remove a supported capability.

Useful defaults and task-local options can reduce setup effort, but do not authorize deleting existing choices or importing another platform's settings-window behavior.

## 4. Give chrome and overlays a measurable budget

For each view, outline the content region and every persistent or temporary layer. Record what each layer helps the user do, how much usable space it consumes, and what triggers its appearance. This skill does not prescribe a universal percentage or maximum layer count. Set the budget against the actual task: can someone read the selected object, compare the required values, and reach the next action without first dismissing unrelated UI?

Use the following review rules:

- One clear primary navigation treatment per active hierarchy level. Global and local sidebars may coexist because they represent different levels; do not mistake their coherent selections for duplication. Deliberate duplicate access for reachability is acceptable; contradictory selected states within the same scope are not.
- Keep frequent local actions visible; group secondary commands by purpose in a discoverable overflow. Do not bury the task's defining action to make a toolbar symmetric.
- A supporting panel needs a task reason to occupy space continuously. Otherwise provide a labeled way to open it and a visible way to close it.
- Classify each overlay as modal or nonmodal. Modal background content must not remain an accidental keyboard destination. A nonmodal inspector must not trap focus or imply that the background is blocked.
- Avoid nested modal tasks when the second step can replace the first or become a normal detail page. When nesting is necessary, specify exactly which layer Escape/Back closes and where focus returns.
- Check the worst combination actually permitted: navigation drawer, inspector, keyboard, validation message, and notification. Remove impossible combinations from the state model rather than hoping their overlap will be rare.

Group actions by function and frequency, and specify which remain visible when space shrinks. Verify the chosen component's actual overflow behavior instead of assuming its visual style supplies an action-priority model.

## 5. Write a scroll, Back, and focus contract

Define behavior for entering, selecting, drilling down, opening an inspector, resizing, returning, and refreshing. Track selected object, active group, query, filters, scroll anchor, draft, focus target, and relevant navigation history. Preserve only meaningful state, with an explicit rule for reset.

For list/detail, decide whether Back returns through prior objects or structural levels. Test that history remains understandable after resizing; do not accept a pane-dependent library default without checking the product’s return contract.

Distinguish browser history, a parent-location control and closing a temporary surface. Deep links, refresh and opening another tab must agree with the router. A back-shaped button must not silently discard work and go home.

Test sticky chrome with keyboard focus, in-page links, error jumps, text enlargement, a short landscape window, and a visible virtual keyboard. Specify which region scrolls; avoid multiple nested regions without a clear task benefit. When navigation minimizes on scroll, retain a discoverable return and avoid changing controls under a stationary pointer or finger. A collapsing header must not remove a focused control unexpectedly.

If the chosen composition extends backgrounds behind chrome, keep actionable content and meaningful labels within usable areas. Decorative continuity does not justify obscuring fields or chart labels.

## 6. Specify materials by role and failure behavior

Choose flat, filled, elevated, translucent or other surfaces from the approved design language and each region's role. None is this skill's default. Content, controls, navigation and overlays may need different treatments; define their relationships before choosing effect values.

For each proposed product material, document:

| Property | Required decision |
|---|---|
| Role | Navigation, contextual controls, content surface, backdrop, or temporary feedback |
| Background range | Static surface, dense text, charts, changing imagery, video, or unknown content |
| Readability protection | Opaque base, controlled translucency, scrim, edge, and foreground tokens |
| Layer relationship | What sits above and below it; what establishes separation |
| Theme behavior | Independent light/dark recipes, selected, disabled, focus, and error states |
| Fallback | Opaque readable surface when effects are absent or unsuitable |
| Preferences | Reduced transparency, increased contrast, reduced motion, and product overrides |
| Cost | Observable scrolling, animation, rendering, and device-performance effect |

Inspect interacting layers and unexplained mixtures of treatments. If multiple effects weaken separation or legibility, revise the composition or backing within the approved direction. Novelty is not evidence of task benefit, and an opaque alternative should retain the intended hierarchy when effects are unavailable.

For custom web materials, test computed foreground/background combinations and rendered contrast over the darkest, brightest, busiest, and moving backgrounds that can occur. A screenshot over a convenient wallpaper is insufficient. Do not assume blur guarantees contrast or that a single fixed opacity works across both themes.

WCAG 2.2 AA includes minimum text contrast, non-text contrast where required to identify controls or graphical information, visible keyboard focus, and focus not entirely hidden by author-created content. Enhanced unobscured focus and the specific Focus Appearance criterion are AAA. State the criterion and level being checked; do not label a material WCAG-compliant based only on its base color tokens.

Check support for reduced motion, reduced transparency, contrast, color scheme and forced colors in the target browsers and operating systems. Provide a readable default even when a preference signal is unavailable; the web does not automatically inherit native adaptations.

## 7. Make shape, elevation, and motion explain relationships

Choose shapes by role: enclosing surface, interactive control, status marker and chart mark. Compare independent, capsule and related corner geometry under the approved system; use [component-states.md](component-states.md#relate-corners-instead-of-copying-one-radius) for inset and rendered-edge checks. CSS defines mechanisms, not a preferred brand radius.

Use elevation to identify overlap, temporary context, or active interaction. Do not add a shadow to every section when spacing and typography already explain grouping. Check edges in light, dark, and contrast modes; a soft shadow alone may fail to separate important regions.

For each animation, state the information it conveys: where an inspector came from, what changed, which object remained selected, or whether an action succeeded. Keep the final state understandable without watching the transition. A command must not require waiting through ornamental motion. Gesture-based interaction needs an equivalent discoverable control appropriate to its task.

Supply calmer alternatives to movement such as zooming, spinning, parallax and animated blur where needed, while retaining state communication. Removing an effect must not remove meaningful feedback. Use the project's accessibility target and supported preference mechanisms.

## 8. Translate control behavior without imposing a brand

Record inheritance separately for color, shapes, materials, typography, icons, layout and motion in [brand-discovery.md](brand-discovery.md). A visual reference does not authorize replacing navigation, removing controls or copying assets. Apply these behavioral checks regardless of the chosen appearance.

### Keep material, color, and state separate

Distinguish four decisions: the material's role and variant; a control's semantic accent; the user's appearance/accessibility preference; and its current interaction state. A brand accent does not determine the fill of every surface.

For a custom control, specify the surface fill or tint, foreground, edge, shadow, shape, focus indicator and transition independently. Keep measurements reviewable in the project's tokens; distinguish verified source values from product-specific choices. Inspect the material in its actual content relationship, including scroll and overlapping panels.

| State | What must be distinguishable | Review failure to catch |
|---|---|---|
| Resting | Purpose, available action, current value | A control looks like a decorative badge or content label |
| Hover | Pointer target and optional preview | Hover changes persistent selection or exposes the only usable action |
| Keyboard focus | Where the next keyboard action applies | A faint highlight vanishes on a selected, tinted, or invalid control |
| Pressed | Input was received, before its result | A bounce substitutes for action feedback, or alters the hit area |
| Selected / checked / mixed | A persistent choice and, where relevant, partial group selection | Color alone carries the value; mixed is rendered as off |
| Expanded | An associated surface is open | The trigger looks closed or its menu loses context after repositioning |
| Pending | Work has started and its result is not yet known | Repeated activation creates duplicate work or the label becomes ambiguous |
| Unavailable | The action cannot currently run, with context when needed | Dimming makes a relevant setting impossible to discover or understand |
| Invalid / failed | Which value or action needs attention and how to recover | The error disappears when focus or hover changes |

Specify simultaneous states as well: selected plus focus, invalid plus focus, expanded plus hover, and pending after activation. These are independent facts, not mutually exclusive CSS classes. Native focus and pointing systems vary by platform; their visual effects are not interchangeable with DOM focus.

Keep pointer effects within a stable hit region and prevent enlargement from crowding adjacent content. Never make pointer effects a prerequisite for touch or keyboard access.

### Choose the component before its finish

| Component | Preserve when changing its visual treatment |
|---|---|
| Action button | A clear verb, priority, press response, pending result, and destructive meaning where applicable |
| Toggle button or switch | The controlled subject, persistent on/off state, and when the change takes effect |
| Checkbox | Independent choices, label activation, hierarchy, and genuine mixed state where supported |
| Radio group | Mutually exclusive choices and a stable group label; selected is not the same as focused |
| Value selector | The current value and a predictable set of choices; searchable selection when the task warrants it |
| Command menu | Context, ordering, unavailable items, submenus, dismissal, and focus return |
| Status badge | Named meaning, freshness, and distinction between passive status and an actionable filter |
| Inline information | The relevant subject and useful explanation without unnecessary interruption |
| Alert | The actual consequence, available recovery or cancellation, and appropriate interruption |
| Icon control | A consistent visual language, accessible name, identifiable meaning, and all interaction states |

Preserve the semantic differences between independent choices, mutually exclusive choices, value selection and commands. Turning every choice into a switch is not modernization. Use [component-states.md](component-states.md) for the full behavior and state contract.

Use selection marks separately from the temporary active menu row. For each menu group, decide whether icons improve recognition; avoid ornamental glyphs that compete with labels. A menu's material must preserve readable labels over its complete allowed backdrop.

An information message does not become an interrupting alert because its container looks polished. App-icon notification badging is a platform-specific mechanism, not a universal rule for every in-product status chip. Define count, severity, acknowledgement and freshness semantics independently.

### Implement the web contract, not a native screenshot

Start from usable semantic controls. A custom composite needs its complete keyboard, focus, selection and dismissal behavior; a collection of links does not automatically need menu semantics. Verify the chosen pattern with actual assistive technology where available.

When the approved direction uses `backdrop-filter`, treat it as an enhancement over a readable surface. Backdrop boundaries and ancestor effects change what is filtered. Blur alone cannot establish native-equivalent material behavior.

Render a compact control specimen in its real layout: buttons, independent and exclusive choices, open menu, selected row, badge, inline message and alert when the product has them. Include supported themes/densities, keyboard focus, pending/error states and applicable reduced-effect alternatives. Then test consuming screens; the specimen supplements the full usage audit rather than replacing it.

## 9. Evidence required for review

For concepts, render the proposed hierarchy at compact, intermediate, and wide sizes with realistic content; include an open detail or settings group, not just the landing screen. Compare a structural alternative before polishing materials. Review both themes and the relevant density choices. Record what improved and what remains unresolved; visual taste still requires the user's review.

For audits and verification, follow [audit-method.md](audit-method.md). A full audit checks every in-scope navigation usage and its defined relevant contexts, not one representative screen. A scoped fix checks its affected usages. Record evidence separately for:

- Navigation correctness: current location, labels, links, role visibility, empty states, Back, refresh, and deep links.
- Task continuity: edit, resize, hide/reopen pane, change destination, return, cancel, and save/review where applicable.
- Space and reachability: long labels, localization, text enlargement, short windows, keyboard appearance, and every supported input method.
- Material reliability: both themes, actual background extremes, overlapping layers, readable fallback, contrast and accessibility preferences.
- Craft: compositional clarity, purposeful hierarchy, coherent geometry, restrained material use, and a distinctive relationship to the product's domain.

Deliver the navigation map, adaptive transformations, overlay rules, material recipes, motion alternatives, and observed failures with their context. A functioning route does not prove aesthetic quality; an attractive image does not prove a complete workflow. Report unavailable runtime or device checks as gaps. Continue the implementation and accessibility detail in [web-engineering.md](web-engineering.md), [platform-adaptation.md](platform-adaptation.md), and [accessibility.md](accessibility.md).

## Reject superficial material matches

For a reference-led concept, compare both light and dark renderings with the actual reference. Check the distribution of materials across content, navigation and overlays; background chroma; edge direction and intensity; shadow hierarchy; concentric geometry; selection versus hover; and behavior during opening, scrolling and return. A uniform colored wash, strong border on every nested group, generic blur everywhere or identical elevation across all surfaces can preserve the vocabulary while missing the reference's hierarchy. Diagnose those visible mismatches before adding more effects. Retain any explicitly requested departures as product choices.

Separate the requested expression from the source system’s latest release. Research the user-selected reference for the current project and record implementation constraints. A reference or CSS effect does not prove native equivalence; there is no inherited default material recipe.
