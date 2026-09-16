# HTML, CSS and React implementation

Use for web frontends. Native desktop/mobile apps also need their framework's current interaction and accessibility APIs; a DOM audit cannot certify a native app. The procedures below are original engineering guidance informed by the linked primary documentation, checked 2026-09-16.

## Learn the existing implementation before choosing tools

Inspect framework and dependency versions, component wrappers, CSS strategy, token source, routes, data layer, form library, validation, SSR/hydration, tests and browser policy. Choose native features or an existing accessible primitive when they fit. A new library earns its cost only if it solves a real capability gap. Do not migrate frameworks or replace the design system merely because another stack is fashionable.

Map the design contract into four layers: tokens, primitives, composed patterns and product journeys. Keep visual variants separate from business permissions and data loading. Shared components need explicit behavior contracts, not only a screenshot gallery.

## Semantic HTML

Choose elements by interaction: links navigate, buttons act, native inputs collect values, fieldsets group related choices, and table structure expresses tabular relationships. Use headings and landmarks to expose the same hierarchy as the visual design. Preserve logical document order; CSS placement cannot compensate for an incoherent focus/reading order. These semantics are defined by the [HTML Living Standard](https://html.spec.whatwg.org/multipage/semantics.html) and [form elements](https://html.spec.whatwg.org/multipage/forms.html).

Associate each field with a label, guidance and relevant error. Choose `autocomplete`, input type and `inputmode` by meaning and expected input. A numeric-looking identifier is often text: postal codes can have letters or leading zeroes. Placeholder text is not the field's only label. Retain browser autofill and password-manager support.

For disclosure, use a real disclosure behavior. For a modal, define name, opening focus, containment, Escape/close behavior, scroll, background inertness and focus restoration. Native `<dialog>` can provide modal behavior through `showModal()`; setting only the `open` attribute is not equivalent. See [HTML dialog definition](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element).

The [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API) concerns display/lifecycle and does not choose whether content is semantically a menu, tooltip or dialog. Set the correct behavior for the intended pattern. Verify current support for newer attributes instead of assuming every evergreen browser implements them.

## Resilient CSS layout

Start with intrinsic sizing and normal document flow. Use Grid for two-dimensional relationships and Flexbox for appropriate one-dimensional groups. Account for minimum-content sizing, long strings and nested flex/grid children; investigate whether `min-inline-size: 0` or wrapping is needed before hiding overflow.

Use viewport media queries for application-wide changes and user/device capabilities; use container size queries when a component must adapt to the actual space its parent gives it. Declare a suitable containment context and test nesting. [MDN container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries) documents the mechanism and fallbacks.

Prefer logical properties for layout that should follow writing direction. Check whether a particular icon or order is directional before mirroring it. [MDN logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values) maps inline/block behavior to writing modes.

Apply fluid values only where the contract permits variation. A `clamp()` expression is not automatically accessible: text must still resize appropriately and avoid clipping. Define readable text measure and flexible control height. Avoid fixed-height text containers. Treat viewport units, mobile browser bars, safe areas and on-screen keyboards as separate constraints; test the actual target browser.

Build CSS around semantic tokens such as `text-muted`, `surface-raised`, `border-critical`, and `action-primary`, with consistent state mappings. Derive theme roles rather than mechanically inverting every color. Check actual rendered contrast, including alpha compositing and images. A perceptually organized palette such as OKLCH can help authoring, but does not itself prove WCAG contrast or browser-gamut compatibility.

Use cascade layers or the project's established ordering to manage overrides. Avoid escalating specificity until a single component can only be corrected by another override. Maintain documented z-index roles and stacking contexts for sticky bars, overlays, menus and toasts.

For token interchange, the [DTCG 2025.10 format](https://www.designtokens.org/tr/2025.10/format/) is a stable community specification, explicitly not a W3C Standard. Adopt it where interoperable tooling is useful; do not force a migration from a working token source solely to use the format.

## Type, assets and motion in production

Check typeface rights, script coverage, fallback metrics, supported weights, numeral style and rendering at actual sizes. Load only necessary font resources. Verify layout before and after fonts load. A missing font must surface as a conformance issue if it materially changes the approved design.

Use the existing icon family consistently, with accessible names for interactive icons and hidden semantics for decoration. Give images an intentional crop and reserved dimensions; test replacement images. Provide responsive sources where useful. Do not fabricate product imagery, reviews or metrics that users could mistake for real evidence.

Motion should express a state or spatial relationship. Prefer compositing-friendly changes where they preserve the design; measure costly effects. Provide meaningful static transitions for [reduced-motion preferences](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion). Essential information and completion states must remain visible without animation. Never make layout or focus correctness depend on a decorative animation's timing.

## React state as UX infrastructure

React's [state-structure guidance](https://react.dev/learn/choosing-the-state-structure) recommends avoiding contradictory, duplicated and unnecessary state. For a consequential async interaction, a discriminated state such as editing/saving/saved/error can express transitions more safely than unrelated booleans. Keep draft and confirmed values distinct when failures are possible.

React [preserves state according to tree position and identity](https://react.dev/learn/preserving-and-resetting-state). Stable keys and deliberate reset boundaries therefore affect focus, form contents and continuity. Test switching records or tenants and returning to drafts. Resetting sensitive state on an identity change may be required even when retaining UI state elsewhere is helpful.

Use effects for synchronization with external systems. Derive ordinary display values during rendering and put direct user actions in event handlers where appropriate. See [You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect). Follow the project's data-fetching architecture; account for races, cancellation, late responses, retry and stale data rather than adding ad hoc fetch effects to each view.

For fields, maintain a consistent controlled/uncontrolled model and keep controlled input updates responsive. [React input documentation](https://react.dev/reference/react-dom/components/input) describes the constraints. Preserve composition input for languages that use IMEs; avoid formatting that jumps the caret or commits incomplete text. Validate at useful times rather than announcing errors on every intermediate keystroke.

[`useId`](https://react.dev/reference/react/useId) can create IDs for accessible relationships; it is not the source of data keys for a list. Ensure label, help and error references remain unique when multiple instances of the same form appear.

Expose component state through appropriate semantics (`aria-expanded`, `aria-selected`, `aria-invalid`, etc.) with the actual correct pattern. A focusable custom control needs its complete keyboard contract; adding a role alone is insufficient. Reuse mature primitives, then test their integration.

## Async and data boundaries

For each action specify pending behavior, duplicate-activation handling, success confirmation, failure recovery and draft preservation. Optimistic updates are suitable only when the visible state can be reconciled and the consequences allow it. Do not declare a payment, permission change or irreversible operation successful merely because a request started.

Keep search/filter/sort/page state shareable in the URL when the task benefits from links and browser history. Keep sensitive data out of URLs. Announce relevant changes without moving focus unexpectedly. Restore list position and selection when returning from details where the task requires continuity.

Virtualization can reduce rendering cost but changes what exists in the DOM. Test keyboard navigation, assistive technology, selected items, focus retention, print, browser find and export. Prefer pagination or simpler rendering if they satisfy both scale and usability.

Use actual permission decisions from trusted application state to communicate availability. The server still enforces access. Clear or re-key tenant/user caches as needed to avoid showing another scope's data; coordinate the fix with the application's security architecture.

## Performance is observable behavior

The Google [Web Vitals reference](https://web.dev/articles/vitals) identifies good field thresholds at the 75th percentile: LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1, segmented by desktop/mobile. Treat these as web performance guidance, not a complete usability score. A single local run cannot establish production compliance.

Also measure the application's critical task: opening a large dataset, filtering, typing, navigating, saving and chart interaction. Reserve loading space, keep meaningful work visible, avoid full-page spinners for local changes, and handle slow/stalled requests. Reduce main-thread work before adding animation polish. Set budgets appropriate to the supported devices and network conditions.

## Learning and adoption sequence

| Capability to learn | Evidence of competence in a project |
| --- | --- |
| Semantic structure and forms | Task works with keyboard and meaningful accessible names |
| Layout/intrinsic sizing | Real content survives narrow widths, zoom and long strings |
| Tokens and component APIs | A theme or primitive fix propagates without page-specific patches |
| React lifecycle and state | Drafts, identity changes and async outcomes behave predictably |
| Workflow and recovery modeling | Back/cancel/retry/permission changes have defined outcomes |
| Visualization grammar | Charts answer a question without distorting the data |
| Performance profiling | Bottleneck measured under representative conditions and improved |
| Visual/interaction verification | Implemented result traceably matches its approved contract |

Learn a feature because an observed task or constraint needs it. New APIs such as view transitions, anchor positioning or newer container-query types require current compatibility checks and fallbacks; their novelty is not a reason to redesign the product around them.
