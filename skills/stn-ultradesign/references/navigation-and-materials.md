# Navigation and materials

Read for app shells, overloaded settings, adaptive navigation, contextual panes, floating controls, translucent materials, or motion that changes perceived hierarchy. Apply this module within the current audit, concept, or implementation scope. An audit diagnoses; it does not authorize a redesign. Follow [discovery-and-preferences.md](discovery-and-preferences.md), [feature-parity.md](feature-parity.md), and [concept-to-code.md](concept-to-code.md) when proposing substantial changes.

Primary sources below were accessed on **2026-09-16**. Apple video evidence means published transcripts were reviewed, not that every video frame was inspected. Several HIG pages required their indexed text because their ordinary page response was a JavaScript shell. The decision tables and review procedures are original operational synthesis, not quotations or universal vendor requirements.

## 1. Separate the authority of each decision

| Evidence class | What it establishes | What it does not establish |
|---|---|---|
| Platform guidance | Familiar behavior and native framework conventions for the stated platform | A universal layout rule for every browser app |
| WCAG requirement | A testable accessibility requirement at a specified conformance level | A preferred brand, material, or navigation architecture |
| CSS specification | Defined web behavior and syntax, subject to specification status | Uniform browser support or a native rendering equivalent |
| Product decision | A justified arrangement for this domain, audience, and task | A worldwide standard merely because the result looks current |

Do not freeze the Apple reference at its 2025 launch. Apple's WWDC26 presentation describes further diffusion of complex backgrounds, stronger edge separation, user-controlled tinting, sidebar changes, and scroll-edge treatments. These are refinements to native systems; verify availability against the actual OS and SDK being targeted. Their implication for this skill is to recheck readability and adaptation as materials evolve, not to reproduce a screenshot from one OS release. [Apple, Platforms State of the Union, WWDC26](https://developer.apple.com/videos/play/wwdc2026/102/)

For a web application, describe a translucent treatment as the product's own material. CSS blur does not reproduce Apple's complete optical, input, accessibility, and window-management behavior. Choose the product's identity with the user; a platform reference does not override the approved concept.

## 2. Define the navigation model before the shell

Inventory destinations and commands separately. For each item, record its scope, frequency, parent, authorized roles, state to preserve, and return destination. Classify it as one of these:

- **App destination:** a stable area such as Projects or Reports.
- **Collection or object:** an entity and its detail, history, or relationships.
- **Local view:** an alternative representation of the current subject.
- **Command:** something that changes, creates, exports, or otherwise acts on the subject.
- **Contextual inspector:** secondary information or editing that depends on a selected subject.
- **Preference:** a persistent choice, with its user, workspace, or system scope stated.

An app destination, an open document, and an action can all look like a tab-shaped control while requiring different behavior. Make those differences explicit in labels, semantics, selection, and close behavior. Microsoft's navigation guidance distinguishes flat, hierarchical, and mixed structures; its NavigationView component supports adaptive placement but still requires the application to implement navigation. Selecting a styled item is not sufficient evidence of a working route. [Microsoft navigation basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics), [NavigationView](https://learn.microsoft.com/en-us/windows/apps/design/controls/navigationview)

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

Apple's tab bars represent top-level areas, preserve their navigation context, and are distinct from action toolbars. Keep eligible destinations stable across empty/loading states; role-based availability still follows the product's access model. The HIG's June 2026 tab/sidebar guidance also supports adaptation between forms. This does not imply a universal five-destination limit or that every web app needs iOS-style tabs. [Apple tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)

## 3. Adapt hierarchy, not just component width

Use actual available width and height, text size, input capabilities, window state, and task needs. Android's adaptive navigation guidance changes navigation form with window size and posture while retaining destinations; its default scaffold choices are implementation conventions, not mandatory web breakpoints. [Android adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation)

**Wide workspace:** expose labeled navigation if it improves repeated switching. Keep object actions near their object. Offer deliberate collapse or pinning where the product needs it; retain the user's chosen state at the agreed scope. Avoid tiny icon-only navigation as an automatic synonym for sophistication.

**Intermediate workspace:** allocate space to useful relationships, such as category/detail or collection/selected object. When two panes no longer work with real labels and forms, transition to a sequential flow. Do not preserve desktop columns by squeezing the primary task.

**Compact workspace:** show one main task context with a clear path back. Global destinations and local editing actions must remain distinguishable. Avoid stacking app header, breadcrumbs, section tabs, filter bar, oversized title, and persistent save footer by default. Decide which context must stay visible and which can appear on demand.

Apple's sidebars can expose collections and shallow hierarchy, support hiding, and adapt to available space. Its guidance recommends restrained hierarchy within the sidebar and additional content panes for deeper structures. Its June 2026 update also clarifies meaningful icon colors. On the web, use these as design evidence, not as permission to copy native assets or force a particular icon color. [Apple sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars)

### Decongest settings without losing features

1. Map every existing setting to its scope, role, dependency, current value, and proposed location. Retain themes, languages, density choices, chart preferences, technical controls, and conditional features in that map.
2. Move frequent task-specific controls to the task when this improves access. Keep durable preferences in identifiable categories; put advanced explanations near the relevant choice.
3. In compact layouts, use a category index with useful summaries, then a focused category page. Search may supplement this structure; it must not become the only path to a feature.
4. In wider layouts, the same categories may remain visible beside the active group. Keep section names and settings identity stable across sizes.
5. Distinguish immediately applied personal preferences from staged changes. Where the approved workflow requires Save, show a coherent change review and dirty state; explain scope before committing.
6. Test return navigation after editing, validation failure, cancellation, and resize. A cleaner screen must not hide an unsaved change or remove a supported capability.

Apple distinguishes task-local options from less frequent app preferences and encourages useful defaults. Treat this as evidence for placement and reduced setup effort, not authorization to delete existing choices. Its macOS settings-window conventions are platform-specific. [Apple settings](https://developer.apple.com/design/human-interface-guidelines/settings)

## 4. Give chrome and overlays a measurable budget

For each view, outline the content region and every persistent or temporary layer. Record what each layer helps the user do, how much usable space it consumes, and what triggers its appearance. This skill does not prescribe a universal percentage or maximum layer count. Set the budget against the actual task: can someone read the selected object, compare the required values, and reach the next action without first dismissing unrelated UI?

Use the following review rules:

- One clear primary navigation treatment per active hierarchy level. Deliberate duplicate access for reachability is acceptable; competing selected states are not.
- Keep frequent local actions visible; group secondary commands by purpose in a discoverable overflow. Do not bury the task's defining action to make a toolbar symmetric.
- A supporting panel needs a task reason to occupy space continuously. Otherwise provide a labeled way to open it and a visible way to close it.
- Classify each overlay as modal or nonmodal. Modal background content must not remain an accidental keyboard destination. A nonmodal inspector must not trap focus or imply that the background is blocked.
- Avoid nested modal tasks when the second step can replace the first or become a normal detail page. When nesting is necessary, specify exactly which layer Escape/Back closes and where focus returns.
- Check the worst combination actually permitted: navigation drawer, inspector, keyboard, validation message, and notification. Remove impossible combinations from the state model rather than hoping their overlap will be rare.

Apple groups toolbar actions by function and frequency. Its WWDC26 SwiftUI guidance describes priorities and overflow when space shrinks. The transferable design decision is an explicit action-priority model; the native API names and runtime behavior do not apply to React automatically. [Apple toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [What's new in SwiftUI, WWDC26](https://developer.apple.com/videos/play/wwdc2026/269/)

## 5. Write a scroll, Back, and focus contract

Define behavior for entering, selecting, drilling down, opening an inspector, resizing, returning, and refreshing. Track selected object, active group, query, filters, scroll anchor, draft, focus target, and relevant navigation history. Preserve only meaningful state, with an explicit rule for reset.

For list/detail, decide whether Back returns through prior objects or through structural levels. Android documents both approaches and warns that pane-dependent history can become surprising after a size change. Do not accept a library default without testing the product's expected return path. [Android list/detail, updated 2026-09-11](https://developer.android.com/develop/adaptive-apps/guides/list-detail)

In a web app, distinguish browser history from a parent-location control and from closing a temporary surface. Deep links, refresh, and opening a destination in a new tab must behave consistently with the router's contract. A back-shaped button must not silently mean discard-and-go-home. Windows guidance similarly ties Back to navigation history rather than decorative placement alone. [Microsoft backward navigation, updated 2026-02-19](https://learn.microsoft.com/en-us/windows/apps/develop/ui/navigation/navigation-history-and-backwards-navigation)

Test sticky chrome with keyboard focus, in-page links, error jumps, text enlargement, a short landscape window, and a visible virtual keyboard. Specify which region scrolls; avoid multiple nested regions without a clear task benefit. When navigation minimizes on scroll, retain a discoverable return and avoid changing controls under a stationary pointer or finger. A collapsing header must not remove a focused control unexpectedly.

Native edge-to-edge backgrounds can continue behind bars while actionable content respects usable areas. Do not infer that every web field or chart label should scroll beneath floating controls. [Apple layout](https://developer.apple.com/design/human-interface-guidelines/layout)

## 6. Specify materials by role and failure behavior

Apple places Liquid Glass primarily in the functional layer above content. Its regular variant manages background luminance and is suitable for text-heavy controls; clear glass is intended for rich media contexts. Standard materials serve other content-layer roles. The choice responds to system appearance and accessibility preferences. These distinctions argue against making every panel a translucent card. [Apple materials](https://developer.apple.com/design/human-interface-guidelines/materials)

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

Avoid glass stacked on glass and unexplained mixtures of material treatments. Apple's original Liquid Glass presentation explicitly discusses these problems. Use an opaque surface whenever it communicates the same hierarchy more clearly; novelty is not evidence of task benefit. [Meet Liquid Glass, WWDC25](https://developer.apple.com/videos/play/wwdc2025/219/)

For custom web materials, test computed foreground/background combinations and rendered contrast over the darkest, brightest, busiest, and moving backgrounds that can occur. A screenshot over a convenient wallpaper is insufficient. Do not assume blur guarantees contrast or that a single fixed opacity works across both themes.

WCAG 2.2 AA includes minimum text contrast, non-text contrast where required to identify controls or graphical information, visible keyboard focus, and focus not entirely hidden by author-created content. Enhanced unobscured focus and the specific Focus Appearance criterion are AAA. State the criterion and level being checked; do not label a material WCAG-compliant based only on its base color tokens. [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Focus Not Obscured explanation](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum)

CSS Media Queries Level 5 defines reduced-motion, reduced-transparency, contrast, color-scheme, and forced-colors preference features; the retrieved document is a Working Draft dated 2026-06-29. Feature support and operating-system integration still need checking in the project's browsers. Provide a readable default and fallback even when a preference query is unavailable. Do not claim the web automatically inherits all native accessibility adaptations. [CSS Media Queries Level 5](https://drafts.csswg.org/mediaqueries-5/)

## 7. Make shape, elevation, and motion explain relationships

Choose shapes by role: an enclosing surface, an interactive control, a status marker, and a chart mark should not become indistinguishable capsules. Compare nested corners and spacing as a system. Apple's WWDC26 AppKit presentation introduces container-related corner behavior; it illustrates relational geometry, not a universal web radius formula. [Modernize your AppKit app, WWDC26](https://developer.apple.com/videos/play/wwdc2026/289/)

Use elevation to identify overlap, temporary context, or active interaction. Do not add a shadow to every section when spacing and typography already explain grouping. Check edges in light, dark, and contrast modes; a soft shadow alone may fail to separate important regions.

For each animation, state the information it conveys: where an inspector came from, what changed, which object remained selected, or whether an action succeeded. Keep the final state understandable without watching the transition. A command must not require waiting through ornamental motion. Gesture-based interaction needs an equivalent discoverable control appropriate to its task.

Apple's motion guidance treats system motion as responsive to platform context and input. Its reduced-motion evaluation specifically addresses movement such as zooming, spinning, parallax, and animated blur. Supply calmer feedback where needed while retaining state communication; simply deleting every animation can remove useful feedback. [Apple motion](https://developer.apple.com/design/human-interface-guidelines/motion), [Reduced Motion evaluation](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria)

## 8. Translate control behavior without imposing a brand

Read this section when the user chooses an Apple-informed material direction or when auditing controls inspired by it. It is an optional reference, not this skill's default appearance. Record inheritance separately for color, shapes, materials, typography, icons, layout, and motion in [brand-discovery.md](brand-discovery.md). A preference for Liquid Glass does not authorize replacing the product's navigation, removing controls, or copying Apple assets.

### Keep material, color, and state separate

Distinguish four decisions: the material's role and variant; a control's semantic accent; the user's appearance/accessibility preference; and its current interaction state. Apple's HIG describes restrained color emphasis on glass, including prominent actions and selected navigation. This is not a rule to tint every surface with the brand color. [Apple color](https://developer.apple.com/design/human-interface-guidelines/color)

For a custom control, specify the surface fill or tint, foreground, edge, shadow, shape, focus indicator, and transition independently. Keep measurements reviewable in the project's tokens; do not present invented opacity, blur, radius, or animation values as Apple's specification. Inspect the material in its actual content relationship, including scroll and overlapping panels.

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

Specify simultaneous states as well: selected plus focus, invalid plus focus, expanded plus hover, and pending after activation. These are independent facts, not mutually exclusive CSS classes. Native focus and pointing systems vary by platform; their visual effects are not interchangeable with DOM focus. [Apple focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection/)

Apple's iPad pointing guidance considers highlight, lift, and hover effects and warns against scaling elements that crowd adjacent content, such as table rows. For custom web UI, retain the ordinary pointer and a stable hit region unless a supported task requires otherwise. Never make pointer effects a prerequisite for touch or keyboard access. [Apple pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)

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

Apple distinguishes action buttons, binary controls, mutually exclusive selections, and menus. Its macOS guidance retains a role for checkboxes and radio buttons; turning every choice into a switch is not modernization. Its pop-up and pull-down terminology also distinguishes choosing a value from issuing a command. Preserve these semantic differences when selecting HTML controls or established accessible components. [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons), [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles), [Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons), [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)

Use selection marks separately from the temporary active menu row. For each menu group, decide whether icons improve recognition; avoid ornamental glyphs that compete with labels. A menu's material must preserve readable labels over its complete allowed backdrop. [Apple menus, updated 2026-06-08](https://developer.apple.com/design/human-interface-guidelines/menus)

An information message does not become an interrupting alert because its container looks polished. Likewise, app-icon notification badging is a platform-specific mechanism, not a universal rule for every in-product status chip. Define the product's count, severity, acknowledgement, and freshness semantics independently. [Apple alerts](https://developer.apple.com/design/human-interface-guidelines/alerts), [Apple notifications](https://developer.apple.com/design/human-interface-guidelines/notifications/)

### Implement the web contract, not a native screenshot

Start from usable semantic controls. A custom menu requires its complete keyboard, focus, selection, and dismissal behavior; a visually similar collection of links does not automatically need ARIA menu semantics. Use the relevant [WAI-ARIA Authoring Practices pattern](https://www.w3.org/WAI/ARIA/apg/patterns/) when a custom composite widget is necessary, and verify actual assistive-technology behavior. APG is implementation guidance; its examples are not certification or ready-made product code.

Treat `backdrop-filter` as a rendering enhancement over a readable surface. Its backdrop boundary and ancestor effects influence what is filtered. Native Liquid Glass additionally coordinates input response, optical effects, system appearance, and window state. CSS blur alone cannot substantiate a claim of native-equivalent behavior. [MDN backdrop-filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter), [Apple custom Liquid Glass views](https://developer.apple.com/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views)

Before approving this direction, render a compact control specimen in its real layout: buttons, independent and exclusive choices, open menu, selected row, badge, inline message, and alert when the product has them. Include light/dark, dense/comfortable arrangements where supported, keyboard focus, pending/error states, and a nontransparent/reduced-motion variant. Then test the interactions in consuming screens; the specimen supplements the full usage audit rather than replacing it. The detailed source distinctions and a proposed experiment protocol are documented in [Liquid Glass controls research](../../../docs/research/liquid-glass-controls.md).

## 9. Evidence required for review

For concepts, render the proposed hierarchy at compact, intermediate, and wide sizes with realistic content; include an open detail or settings group, not just the landing screen. Compare a structural alternative before polishing materials. Review both themes and the relevant density choices. Record what improved and what remains unresolved; visual taste still requires the user's review.

For audits and verification, follow [audit-method.md](audit-method.md). A full audit checks every in-scope navigation usage and its defined relevant contexts, not one representative screen. A scoped fix checks its affected usages. Record evidence separately for:

- Navigation correctness: current location, labels, links, role visibility, empty states, Back, refresh, and deep links.
- Task continuity: edit, resize, hide/reopen pane, change destination, return, cancel, and save/review where applicable.
- Space and reachability: long labels, localization, text enlargement, short windows, keyboard appearance, and every supported input method.
- Material reliability: both themes, actual background extremes, overlapping layers, readable fallback, contrast and accessibility preferences.
- Craft: compositional clarity, purposeful hierarchy, coherent geometry, restrained material use, and a distinctive relationship to the product's domain.

Deliver the navigation map, adaptive transformations, overlay rules, material recipes, motion alternatives, and observed failures with their context. A functioning route does not prove aesthetic quality; an attractive image does not prove a complete workflow. Report unavailable runtime or device checks as gaps. Continue the implementation and accessibility detail in [web-engineering.md](web-engineering.md), [platform-adaptation.md](platform-adaptation.md), and [accessibility.md](accessibility.md).
