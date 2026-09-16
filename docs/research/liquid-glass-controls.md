# Liquid Glass, controls, and an independent product identity

**Reference-specific research archive.** This report records one investigated design language and its retrieval date. It is not a default aesthetic, mandatory operational instruction or a substitute for researching the direction selected by the current user. Use the [project-specific reference method](../../skills/stn-ultradesign/references/brand-discovery.md#research-the-selected-language-for-this-project) for any chosen language or company identity.


**Research date:** 2026-09-16. **Source type:** official Apple guidance and documentation, published WWDC transcripts, W3C implementation guidance, and MDN documentation. **Purpose:** inform a product-specific brand choice with current evidence. This is not a requirement that every STN Ultradesign project adopt Apple's appearance.

The operational synthesis is in [Navigation and materials](../../skills/stn-ultradesign/references/navigation-and-materials.md). Brand adoption belongs in the project's [selective inheritance matrix](../../skills/stn-ultradesign/references/brand-discovery.md). This public note contains no private application data, copied design assets, or third-party skill content.

## What the research establishes

Liquid Glass is more than a translucent fill. Apple's 2025 presentation describes coordinated background response, edge light, changing shadows, input feedback, and transitions that retain the relationship between a control and the surface it reveals. Larger surfaces can use a different material response from small controls. These descriptions establish the native design intent; they do not provide a portable CSS formula. [Meet Liquid Glass, WWDC25, especially 1:29, 6:00, and 10:31](https://developer.apple.com/videos/play/wwdc2025/219/)

The 2026 material refinements place further emphasis on separation and legibility. They should be considered alongside the original presentation, rather than treating every 2025 screenshot as the final design specification. Availability must be checked against the actual target runtime. [Platforms State of the Union, WWDC26](https://developer.apple.com/videos/play/wwdc2026/102/)

Current AppKit guidance describes stronger sidebar selection typography, revised scroll-edge behavior, and a click-responsive glass effect for appropriate interactive elements. It explicitly recommends restraint with the latter. The same session describes geometry that responds to its enclosing container. This supports a distinction between functional interaction feedback and continuous decorative animation. [Modernize your AppKit app, WWDC26, 14:24–16:59](https://developer.apple.com/videos/play/wwdc2026/289/)

The current SwiftUI presentation also distinguishes active and inactive windows and describes responsive custom glass on Mac. These are native state relationships, not a reason to dim an arbitrary web panel merely because the pointer leaves it. [What's new in SwiftUI, WWDC26, 2:12–8:06](https://developer.apple.com/videos/play/wwdc2026/269/)

### Three different meanings of transparency and tint

| Axis | Evidence | Product decision |
|---|---|---|
| Material variant | Apple's regular and clear variants have different intended contexts; text-heavy surfaces and rich media do not have identical requirements | Choose the role and allowed background before judging the appearance |
| Control accent | HIG color uses restrained tint to express prominence or state | Map the brand accent to specific semantic roles, not every container |
| Personal appearance | The retrieved iPhone guide offers Clear/Tinted appearance choices; WWDC26 also describes a tint adjustment | Respect the actual supported preference without confusing it with a control's semantic state |

Sources: [Apple materials](https://developer.apple.com/design/human-interface-guidelines/materials), [Apple color](https://developer.apple.com/design/human-interface-guidelines/color), [iPhone display settings](https://support.apple.com/en-mt/guide/iphone/-iphd6804774e/ios). The support guide and conference material describe different version contexts; this research did not test those OS settings on a device. A user choosing less transparency has not chosen a different primary-action color.

An accessible fallback is a designed state. Apple's SwiftUI reduced-transparency environment documentation calls for opaque rather than semitransparent backgrounds when that preference is enabled. Preserve grouping and hierarchy through surfaces, edges, spacing, and labels; do not make an element disappear when its optical treatment is removed. [Reduce Transparency environment value](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducetransparency)

## Geometry and background roles: a closer check

The [2025 design-system session](https://developer.apple.com/videos/play/wwdc2025/356/) distinguishes fixed, capsule and concentric geometry, with room for optical adjustment. Its dense macOS examples do not impose capsules on all controls. The [SwiftUI implementation session](https://developer.apple.com/videos/play/wwdc2025/323/) describes shared corner centers between a control near a sheet edge and its container. Thus equal numerical radii are not the goal of nested concentric corners.

Our geometric transfer is deliberately conditional: two circular corners with a uniform inset share a center when the smaller radius equals the larger radius minus that inset, provided the result remains positive. Unequal spacing, elliptical or continuous shapes, minimum-radius fallbacks and independent capsule controls need separate treatment. A named “Apple radius” applied everywhere would discard these relationships. [ConcentricRectangle documentation](https://developer.apple.com/documentation/swiftui/concentricrectangle) supports individually configured corners; the [2026 AppKit session](https://developer.apple.com/videos/play/wwdc2026/289/) continues the container-relative approach.

The web has its own box geometry. [CSS Backgrounds and Borders](https://www.w3.org/TR/css-backgrounds-3/#corners) defines outer radii, inner border/content relationships and reduction when neighboring curves overlap. The operational module therefore measures actual edges and checks wrapping, density, zoom, clipping and focus clearance. Its numerical example is original geometry, not an extracted native token. Native corner handling and optical effects were not executed or measured in this research.

Background choice also requires more than two swatches. [HIG color](https://developer.apple.com/design/human-interface-guidelines/color) gives semantic roles and distinguishes system from grouped backgrounds on iOS/iPadOS. [The grouped-background API](https://developer.apple.com/documentation/uikit/uicolor/systemgroupedbackground) describes a main grouped surface and subordinate content layers. [Dark Mode guidance](https://developer.apple.com/design/human-interface-guidelines/dark-mode) describes dimmer base and brighter elevated presentations on iOS/iPadOS. That presentation distinction is separate from content grouping and does not prescribe every macOS or web surface.

The resulting surface matrix distinguishes base, grouped, elevated, standard material, functional glass, interaction state and reduced-effect fallback. It does not invent a universal Apple light/dark hex pair. The actual backdrop, appearance, contrast preferences, platform and release affect the result. Nor does a neutral palette by itself demonstrate Apple fidelity. Opaque reading planes and deliberately translucent chrome can coexist; user-approved content-glass extensions remain explicit departures from Apple's usual layer guidance.

For evidence, compare the whole scene as well as local controls, including scroll, overlap, long text, both themes and relevant display preferences. Test whether edges and shadows clarify a real relationship before adding both to every container. The concrete checks are in [component states](../../skills/stn-ultradesign/references/component-states.md#relate-corners-instead-of-copying-one-radius).

**Additional access limits:** the three 2025 WWDC transcripts and the 2026 AppKit transcript were read; this pass did not watch their motion or measure screenshots. HIG and SwiftUI/UIKit documentation often returned JavaScript shells, so relevant official text was read through the primary pages' search index. The W3C specification body was directly readable. Indexed text and platform examples do not prove a particular browser implementation or current prototype matches Apple's rendered appearance.

## Interaction is a state system

The following distinctions are original review criteria informed by the sources, not measured superiority claims:

- **Hover** previews the pointer's target. It does not confirm a persistent choice. Use it as optional feedback, with no task that depends exclusively on hovering.
- **Keyboard focus** identifies where keyboard input applies. It remains visible on an already selected control, across background changes, and after a menu closes.
- **Press** acknowledges input. The hit region remains stable while decorative geometry changes; an interrupted or cancelled press must not execute an unintended command.
- **Selection** represents the lasting choice. A checked mark, selected radio, or active view remains identifiable after hover ends and after focus moves elsewhere.
- **Pending and result** describe application work. A fluid press animation cannot replace progress, failure, or completion feedback.

Apple's focus guidance is platform-specific, with different treatments for different input systems. Some paragraphs concern tvOS or visionOS; their instructions must not be flattened into general browser rules. [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection/)

Its iPad pointer guidance differentiates effects and their spatial requirements. In particular, enlarging tightly arranged rows can cause overlap. The useful transfer to a dense desktop product is to assess available space before adding lift or scale; a restrained surface change may communicate the target more clearly. [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)

## What each component must retain

| Component family | Apple evidence, in scope | Independent product acceptance check |
|---|---|---|
| Buttons | Custom buttons need press feedback; visual prominence and labels communicate purpose | Can someone identify the primary action, activate it with different inputs, and distinguish pending from complete? |
| Switches and toggle buttons | Binary state has its own semantics | Does the label name the controlled subject, and is the persistence/save behavior explicit? |
| Checkboxes | Independent and mixed selections remain useful, particularly for grouped choices | Can a partially selected group be distinguished from all-on and all-off without relying only on hue? |
| Radio buttons | A set represents mutually exclusive choices | Does focus remain distinct from the selected value, with the correct group relationship? |
| Value selectors | A pop-up selector communicates a mutually exclusive current value | Can users predict the choices and read the current selection without opening it? |
| Command menus | Pull-down actions relate to the trigger; primary work should remain discoverable | Do label, command order, dismissal, and focus return remain correct when the menu moves to avoid clipping? |
| Menu marks and icons | Current menu guidance separates selection marks from optional meaningful icons | Is the active row distinguishable from checked state, and is icon treatment coherent within a group? |
| Inline information and alerts | Alerts interrupt and should be reserved for consequential, actionable situations | Can routine status remain contextual while a consequential decision is unmistakable? |
| Status badges | Apple's app-icon notification badging has a specific purpose | Is this a count, severity, freshness marker, or interactive filter, and does the visual treatment make that clear? |

Sources: [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons), [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles), [Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons), [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons), [Menus](https://developer.apple.com/design/human-interface-guidelines/menus), [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts), [Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications/).

Menu guidance was updated on **2026-06-08**. Do not infer that every menu item should receive an icon because older material shows many symbols. Decorative duplication consumes space and can weaken the useful difference between command meaning, selection, and severity.

An icon system also needs coherent optical weight, detail, alignment, and meaning. Apple discusses those relationships in its symbol guidance. That does not establish a blanket license to extract Apple symbols for a web product. Use assets with documented permission for the intended use or create an original set, and preserve accessible names. [SF Symbols guidance](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)

App icons are a separate surface from interface glyphs. Apple's app-icon guidance addresses layered artwork and appearance variants; it is not an instruction to turn every small toolbar glyph into a three-dimensional glass object. [App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons)

## A reviewable material recipe

For an independently designed web treatment, record these fields per component family. The table deliberately does not assign arbitrary global pixel values or opacity percentages.

| Field | Question the design contract must answer |
|---|---|
| Plane and role | Is this content, chrome, a temporary decision, or a status signal? |
| Background envelope | Which imagery, text, chart marks, scrolling content, and overlapping surfaces can appear beneath it? |
| Fill and translucency | What remains readable before any optional filter effect is applied? |
| Foreground and accent | What communicates meaning, priority, selection, and unavailability? |
| Edge | Which boundary is necessary to recognize the control or separate a layer? |
| Shadow | Does it express actual overlap or interaction, and what replaces it in contrast modes? |
| Shape | How does the shape relate to its container, neighbors, and hit region? |
| State composition | What happens when selection, focus, error, or pending states coexist? |
| Motion | What information is preserved when expansion, bounce, scale, or parallax is reduced? |
| Theme and density | How do equivalent light/dark and compact/comfortable treatments preserve function? |

Compare an opaque baseline with a restrained translucent variant using identical tasks, content, dimensions, and states. If glass improves perceived structure but obscures values, it has not passed the task. If it is attractive but increases distraction, revise the extent or placement before adding more optical detail. This is a proposed experiment, not an observed research result.

## Web implementation boundaries

`backdrop-filter` affects pixels behind an element within its backdrop boundary. Ancestor opacity and effects can change that boundary. Establish the DOM and surface layering first; do not debug inconsistent blur by increasing blur or opacity indiscriminately. [MDN backdrop-filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)

Apple's custom-view documentation combines material shape, tint, interactivity, grouping, and transitions in native APIs. A CSS implementation can borrow an idea such as an anchored transition while remaining an original, explicitly web-specific treatment. It cannot claim to reproduce Apple's native behavior merely because a translucent rounded rectangle looks similar. [Applying Liquid Glass to custom views](https://developer.apple.com/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views)

Native HTML controls should retain their browser semantics where appropriate. A custom menu, checkbox, or radio group must implement the behavior of the chosen web pattern, not only its appearance. Menu buttons expose expansion and menu relationships; checked choices expose checked state. The WAI-ARIA Authoring Practices Guide explains these patterns but is not itself a WCAG certificate. [Menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/), [Menu and menubar](https://www.w3.org/WAI/ARIA/apg/patterns/menubar/), [Checkbox](https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/), [Radio group](https://www.w3.org/WAI/ARIA/apg/patterns/radio/)

Do not translate Apple point measurements into CSS pixels without considering the platform, input, and applicable web criteria. Do not substitute an animated hover effect for an independently visible keyboard indicator. Use the project's [accessibility reference](../../skills/stn-ultradesign/references/accessibility.md) and [web engineering reference](../../skills/stn-ultradesign/references/web-engineering.md) for that implementation contract.

## Verification proposed by this research

Build a small original control specimen and test it within actual consuming layouts. Include quiet, selected, focused, pressed, pending, error, unavailable, expanded, and mixed states where they are defined. Cover control combinations, not only one state per screenshot.

Use real supported theme and density variants, long localized labels, keyboard and touch, a short viewport, and real background extremes. For motion and transparency preferences, check both the resulting appearance and whether the task remains understandable. Test menus near every relevant screen edge and inside scrolling or modal contexts. Compare shape transitions with input and focus behavior; a beautiful transition with a lost focus target is a failed interaction.

Record image dimensions, browser/runtime, revision, state, background, and preference settings with each result. Measure performance on the relevant device rather than labeling a visual effect lightweight from source inspection. Material recipes should remain adjustable until the user approves the actual rendered treatment.

**Limits:** This research reviewed source text and transcripts, including indexed HIG text where ordinary pages returned a JavaScript shell. It did not inspect every native animation frame, run an Apple SDK sample, benchmark rendering, validate device support, or establish user preference experimentally. No exact Apple color, shadow, blur, or timing specification is claimed where the reviewed sources do not provide one. All linked sources were accessed on 2026-09-16; source update dates are reported only where observed.


A further implementation lesson is to verify the painted content area, not merely declared colors. Apple's [systemBackground documentation](https://developer.apple.com/documentation/uikit/uicolor/systembackground) describes standard content with a white primary background in light appearance; [grouped backgrounds](https://developer.apple.com/documentation/uikit/uicolor/systemgroupedbackground) serve grouped content. Official indexed documentation was read. This supports separating surface roles, not prescribing one white/gray palette to every application or claiming UIKit constants are macOS/web rendering contracts.
