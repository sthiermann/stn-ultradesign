# Platform adaptation: desktop, tablet, phone

Read when a UI resizes, changes orientation, supports mixed input, runs on more than one platform, or occupies an embedded container. These are operational choices to validate against the project’s tasks, supported platforms and current implementation.

## 1. Model the available space and interaction

Record viewport and container dimensions, browser zoom, text scale, pointer capabilities, keyboard availability, orientation, host chrome, safe areas, and the task in progress. A tablet may have a pointer; a desktop may accept touch; a large physical screen may expose a narrow app window. Use device names as test labels rather than as complete capability definitions.

Base application layout on available window space and component layout on its allocated container. Preserve task state when either changes.

Define explicit adaptation rules before changing styling:

| Situation | Candidate adaptation | Invariant |
|---|---|---|
| Narrow and touch-oriented | One dominant content region, concise navigation, reachable controls | Core task remains complete |
| Medium with mixed input | Selective panes, contextual tools, touch-usable actions | Input changes preserve access |
| Wide workspace | Concurrent list/detail, comparison, or inspector where useful | Added space carries useful context |
| Wide reading surface | Bounded text measure with deliberate margins | Text does not stretch without limit |
| Short viewport or virtual keyboard | Scrollable task region and visible current field | Focused input and action remain reachable |
| Large text or zoom | Reflow, wrap, alternate arrangement | Essential content remains available |
| Embedded card or panel | Adapt to the component's container | Component works beyond a full-width demo |

Completion: each major view has a written transformation and a preservation rule. For concept-first design, include these in the reviewable concept under [concept-to-code.md](concept-to-code.md) and obtain the required approval. In audit-only work, document existing behavior and gaps. Preserve already approved scope and explicit direct-implementation authorization. “Make it responsive” is insufficient to review. After approval, treat the recorded layout transformations, token roles, component variants, and task invariants as the conformance contract. Propose and approve material deviations instead of improvising a different mobile design during coding.

## 2. Preserve task continuity across layout changes

List/detail, supporting-pane and feed arrangements are useful candidates. On narrow surfaces, a task may become sequential; on wide surfaces, it may benefit from concurrent context.

For every transition, record what happens to selected object, sort order, filters, search query, scroll position, draft values, open disclosure, navigation history, and keyboard focus. Specify only what is relevant to that flow, then test it. If a focused pane disappears, transfer focus deliberately to the corresponding visible context. Resizing must not silently submit, discard, duplicate, or restart work.

Use browser history and deep-link behavior appropriate to the application. When detail becomes a separate narrow view, returning should restore the meaningful list context. If an inspector becomes a drawer, its scope must still identify the selected object. Test route refresh at both sizes; do not rely only on the transition from a desktop session.

Avoid equating fewer visible elements with fewer supported capabilities. Secondary information may move into an accessible disclosure or detail view. Document any intentionally unsupported task by surface and provide a clear explanation in the product when necessary. An inaccessible hidden control is not a mobile adaptation.

## 3. Respect platform conventions without losing product identity

| Environment | Preserve | Validate before adopting |
| --- | --- | --- |
| Native desktop | Window, navigation, keyboard and text conventions | Current runtime and accessibility behavior |
| Native mobile/tablet | Back behavior, safe areas, adaptive space and input conventions | Installed framework and device support |
| Cross-platform web | Browser semantics, history, focus, zoom and links | Supported browsers and input capabilities |
| Embedded platform | Host navigation, theming and component contracts | Exact extension surface and permitted APIs |

Test safe areas, changing window size, orientation, localization and text enlargement. Translate a selected native reference into web constraints deliberately rather than copying its point values.

A selected material may depend on native adaptation beyond translucent styling. Document what the web implementation can reproduce, what needs a fallback and what remains unverified.

Check the installed library and framework versions. Design guidance and native or web implementations do not necessarily advance together.

Determine whether the host uses ordinary DOM, embedded content or a remote-rendered extension before selecting APIs or components.

## 4. Adapt density and input independently

Choose interaction geometry from tasks and capabilities, then adjust content density. Keep visible affordances available without hover where touch or keyboard users need them. A drag operation needs a usable alternative appropriate to the task. Tooltips can supplement labels but cannot be the only path to essential instructions.

Do not choose touch target size from a device name alone. Verify coarse and fine pointer use, keyboard input and the product’s density choice independently.

Test hybrid behavior deliberately: begin a task with touch, continue with a keyboard, inspect focus after pointer input, and activate contextual actions without hovering. For a compact option, check the actual hit areas and reading comfort. Keep user preference persistent at an appropriate scope; avoid surprising mode changes in the middle of work.

## 5. Implement a reviewable adaptation contract

For HTML/CSS/React projects, separate content and task state from presentation variants. Prefer a shared meaningful DOM structure when it can express all arrangements. Use viewport-level rules for the app shell and container-level rules for reusable content where supported by the project's browser baseline. Select exact breakpoints where the composition stops working with realistic content, while respecting a coherent project scale.

When different structures are necessary, ensure only the active one participates in interaction and accessibility. Preserve state above presentation branches where appropriate, keep identifiers unique, and account for focus when mounting or unmounting a control. Check that visual order and reading/tab order remain coherent. These are acceptance requirements; verify the chosen implementation against current HTML, CSS, and React documentation in the engineering reference.

Use relative and intrinsic sizing where suitable, wrap text, and cap reading widths independently from workspace widths. Validate fixed or sticky headers, bottom action bars, dropdowns, and dialogs against keyboard appearance, zoom, safe-area insets, and scroll containers. Every scroll region needs an understandable purpose and a usable way to reach its content.

## 6. Test boundaries, not just device presets

Use the product's supported range and representative hardware. Example CSS viewport probes such as 360, 768, 1024, and 1440 pixels are starting fixtures, not universal device definitions or conformance criteria. Add widths immediately below and above every actual breakpoint, a short landscape window, and an embedded narrow container.

| Probe | Required observation |
|---|---|
| Continuous resize | No trapped content, accidental reset, or repeated layout thrashing |
| Orientation change mid-form | Values survive and current work remains locatable |
| Keyboard opens over a field | Field, error, and next action can be reached |
| Large text and browser zoom | No essential clipping or unusable fixed region |
| Long localized strings and RTL | Order, alignment, punctuation, and actions remain understandable |
| Slow data or partial failure | Layout stays interpretable during intermediate states |
| Dark, contrast, reduced motion | The adapted composition remains perceivable and usable |
| Dense and sparse data | Empty and maximum realistic content both work |
| Touch, keyboard, mixed input | Equivalent task completion without hidden controls |

Completion: record pass, fail, or not tested for each relevant probe and route family. Include actual settings and reproducible failures. If only emulated resizing was available, report that limitation; do not claim physical-device, assistive-technology, or real-user validation. For a scoped fix, recheck affected consuming routes. For a full audit, inspect every usage and its relevant configurations. Outstanding device-specific checks remain gaps and prevent a complete-coverage claim.
