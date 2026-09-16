# Liquid Glass, controls, and an independent product identity

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
