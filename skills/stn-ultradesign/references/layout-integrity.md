# Layout integrity under real content

Read when auditing rendered surfaces, reviewing a concept, or changing content, geometry, shared controls or responsive behavior. Use this procedure before claiming that affected layouts render correctly. Apply it to every in-scope usage and its relevant contexts; an isolated component specimen does not establish its fit inside a page, drawer or widget. Reuse the inventory, obligations and evidence described in [audit-method.md](audit-method.md) or the bounded requirement record. This is a verification pass, not a second audit system.

## Plan observable expectations

For each affected usage, identify its owning container and the permitted behavior when space or content changes: grow, wrap, stack, scroll locally, abbreviate with accessible full content, or switch to an agreed presentation. Record intentional overlays and their dismissal, focus and stacking rules. Natural wrapping is not a defect; lost meaning, broken grouping, clipped controls and blocked tasks are.

Plan checks before collecting passing screenshots. Include normal content and at least one plausible stress case per distinct sizing or interaction behavior. Select finite context classes from the supported product, with reasons for exclusions. A full audit covers every usage; a focused change covers affected usages and dependencies. Additional instances can share a fixture only when their behavior and constraints are equivalent.

| Probe | Conditions to exercise | Observable result |
| --- | --- | --- |
| Available space | Supported compact, medium and expanded spaces; immediately below, at and above real viewport/container breakpoints; narrow embedded panels; short landscape; resize while work is open | Content fits its owning region, navigation and actions remain reachable, and the task survives the transformation |
| Content growth | Long localized labels, user names, unbroken identifiers, large/negative numbers with units, dense badges and multi-line validation; supported RTL and densities | Containers accommodate content according to the contract; text, icons and actions retain their association and readable spacing |
| Controls and toolbars | Long button text, icon plus label, pending spinner, disabled/error states, wrapping groups and open selectors | Labels stay readable within the hit area; padding and icon size remain coherent; primary/secondary actions retain their hierarchy and full functionality |
| User text settings | Applicable text enlargement, reflow and spacing overrides from [accessibility.md](accessibility.md#7-reflow-text-adaptation-and-orientation) | Essential content and functions survive; readable text is not shrunk or hidden to manufacture a fit |
| Floating and anchored layers | Menus near every constrained edge, tooltips, drawers, dialogs, sticky headers/actions, concurrent notifications; scroll and resize while open | Layers remain attached to the correct context, avoid unintended clipping and interception, and preserve focus, dismissal and access to content |
| Asynchronous changes | Font fallback and loaded font, missing/late images, skeleton to data, expanded details, validation, live counts, empty/error/retry | Both intermediate and settled states remain usable; content shifts do not obscure or relocate an action during activation |
| Mobile and input constraints | Supported touch/keyboard paths, orientation changes, browser chrome, safe areas and actual on-screen keyboard where available | Focused fields, errors, close and commit actions remain reachable; unavailable hover does not hide essential work |

Use actual CSS viewport and container dimensions, not physical device resolution alone. Browser zoom, text enlargement, a narrow viewport and a real virtual keyboard exercise different behaviors; record which was performed. If device-specific testing is unavailable, retain the relevant gap rather than treating an iframe or resized desktop browser as equivalent.

## Inspect what is painted and what responds

1. Open the real usage through its normal entry with the planned fixture. Inspect normal, stressed and relevant transient states, including open overlays and the maximum intermediate extent of motion. Capture the artifact revision, viewport and usable container size, browser, zoom/text settings, locale, theme, density, state and fixture.
2. Check page and local overflow, line wrapping, box boundaries, padding, alignment and control reachability. Scroll through the full relevant region; an opening screenshot can miss a covered footer or off-screen error. For tables and graphs, inspect headers, cells, legends, axes, tooltips and empty/loading states within their actual widget allocation.
3. Use geometry and hit testing to investigate suspected defects. Compare scroll/client extents for the intended scroll owner; inspect text and control bounds against their clipping ancestors, and verify the element receiving input at a visibly actionable point. Account for transforms, portals, sticky positioning and stacking contexts. A larger scroll extent can be intentional; intersecting rectangles can represent valid nesting or overlays. Classify the relationship instead of reporting every intersection as a collision.
4. Inspect the rendered result visually as well. Bounding boxes do not measure shadows, painted decoration, glyph clearance or perceived grouping reliably. Verify keyboard focus and touch access where relevant. Check both a working control and a neighboring area that should not activate it, following [verification.md](verification.md#minimum-useful-interaction-pass).
5. Repeat the original reproduction after correction, then recheck usages affected by the same primitive or sizing rule. Exercise the intended exception too: a legitimate scrollable table or open popover must remain usable after removing accidental overflow elsewhere.

Common causes worth inspecting include intrinsic minimum sizes in flex/grid, fixed heights containing variable text, margins outside allocated widths, absolute positioning that ignores content growth, overflowing children clipped by an ancestor, and a portal or transformed ancestor changing the positioning context. Correct the cause while preserving the task. A blanket overflow-hiding rule, smaller text, deleted action or suppressed error message is not evidence of a repaired layout.

## Close each obligation with evidence

Use the existing acceptance or audit record; link evidence rather than maintaining duplicate result tables. For each check, record:

| Record | Required content |
| --- | --- |
| Identity | Requirement/obligation, usage, fixture and artifact revision |
| Conditions | Actual viewport and container, state, input and relevant appearance/text settings |
| Expectation | Allowed wrap/scroll/overlay behavior and the concrete failure condition |
| Observation | Rendered evidence, measurements and interaction outcome appropriate to that claim |
| Result | Pass, fail, blocked or not-tested; exact reproduction and remaining dependency |

An allowed overlap names the owning surface, purpose and preserved access. A truncation decision includes how essential full content is reached with supported inputs. A multi-line button can be valid when deliberately designed; accidental clipping, an isolated icon or unreadable grouping remains a finding. A two-dimensional data region does not exempt surrounding controls or prose from adaptation.

Keep layout, accessibility, information usefulness and data correctness results separate. A valid table shape cannot establish correct filters or useful widgets; use [data-visualization.md](data-visualization.md) for those checks. A screenshot, CSS declaration or successful build cannot by itself close the corresponding interaction obligation. Unperformed required checks remain visible before concept or implementation readiness is claimed.
