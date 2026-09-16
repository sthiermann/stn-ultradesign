# HTML, CSS and React implementation

Use for web frontends. Native desktop/mobile apps also need their framework's current interaction and accessibility APIs; a DOM audit cannot certify a native app. The procedures below are original engineering guidance. Verify current implementation contracts for the project’s installed framework and supported browsers.

## Learn the existing implementation before choosing tools

Inspect framework and dependency versions, component wrappers, CSS strategy, token source, routes, data layer, form library, validation, SSR/hydration, tests and browser policy. Choose native features or an existing accessible primitive when they fit. A new library earns its cost only if it solves a real capability gap. Do not migrate frameworks or replace the design system merely because another stack is fashionable.

Map the design contract into four layers: tokens, primitives, composed patterns and product journeys. Keep visual variants separate from business permissions and data loading. Shared components need explicit behavior contracts, not only a screenshot gallery.

## Semantic HTML

Choose elements by interaction: links navigate, buttons act, native inputs collect values, fieldsets group related choices, and table structure expresses tabular relationships. Use headings and landmarks to expose the same hierarchy as the visual design. Preserve logical document order; CSS placement cannot compensate for an incoherent focus/reading order. Verify the chosen elements against the current language and browser contract.

Associate each field with a label, guidance and relevant error. Choose `autocomplete`, input type and `inputmode` by meaning and expected input. A numeric-looking identifier is often text: postal codes can have letters or leading zeroes. Placeholder text is not the field's only label. Retain browser autofill and password-manager support.

For disclosure, use a real disclosure behavior. For a modal, define name, opening focus, containment, Escape/close behavior, scroll, background inertness and focus restoration. Native `<dialog>` can provide modal behavior through `showModal()`; setting only the `open` attribute is not equivalent. Check support and behavior in the project’s target browsers.

The Popover API concerns display/lifecycle and does not choose whether content is semantically a menu, tooltip or dialog. Set the correct behavior for the intended pattern. Verify current support for newer attributes instead of assuming every evergreen browser implements them.

## Resilient CSS layout

Start with intrinsic sizing and normal document flow. Use Grid for two-dimensional relationships and Flexbox for appropriate one-dimensional groups. Account for minimum-content sizing, long strings and nested flex/grid children; investigate whether `min-inline-size: 0` or wrapping is needed before hiding overflow.

Use viewport media queries for application-wide changes and user/device capabilities; use container size queries when a component must adapt to the actual space its parent gives it. Declare a suitable containment context and test nesting. Provide a usable fallback for the supported browser baseline.

Prefer logical properties for layout that should follow writing direction. Check whether a particular icon or order is directional before mirroring it. Test inline/block behavior under the supported writing directions.

Apply fluid values only where the contract permits variation. A `clamp()` expression is not automatically accessible: text must still resize appropriately and avoid clipping. Define readable text measure and flexible control height. Avoid fixed-height text containers. Treat viewport units, mobile browser bars, safe areas and on-screen keyboards as separate constraints; test the actual target browser.

Build CSS around semantic tokens such as `text-muted`, `surface-raised`, `border-critical`, and `action-primary`, with consistent state mappings. Derive theme roles rather than mechanically inverting every color. Check actual rendered contrast, including alpha compositing and images. A perceptually organized palette such as OKLCH can help authoring, but does not itself prove WCAG contrast or browser-gamut compatibility.

Use cascade layers or the project's established ordering to manage overrides. Avoid escalating specificity until a single component can only be corrected by another override. Maintain documented z-index roles and stacking contexts for sticky bars, overlays, menus and toasts.

Choose token interchange only when it serves the project’s actual tools. Verify format support and preserve semantic roles; adopting a new format alone is not a reason to replace a working token source.

## Type, assets and motion in production

Check typeface rights, script coverage, fallback metrics, supported weights, numeral style and rendering at actual sizes. Load only necessary font resources. Verify layout before and after fonts load. A missing font must surface as a conformance issue if it materially changes the approved design.

Use the existing icon family consistently, with accessible names for interactive icons and hidden semantics for decoration. Give images an intentional crop and reserved dimensions; test replacement images. Provide responsive sources where useful. Do not fabricate product imagery, reviews or metrics that users could mistake for real evidence.

Motion should express a state or spatial relationship. Prefer compositing-friendly changes where they preserve the design; measure costly effects. Provide meaningful static transitions for reduced-motion preferences. Essential information and completion states must remain visible without animation. Never make layout or focus correctness depend on a decorative animation's timing.

## React state as UX infrastructure

Avoid contradictory, duplicated and unnecessary React state. For a consequential async interaction, a discriminated state such as editing/saving/saved/error can express transitions more safely than unrelated booleans. Keep draft and confirmed values distinct when failures are possible.

React component identity and tree position affect whether state is retained. Stable keys and deliberate reset boundaries therefore affect focus, form contents and continuity. Test switching records or tenants and returning to drafts. Resetting sensitive state on an identity change may be required even when retaining UI state elsewhere is helpful.

Use effects for synchronization with external systems. Derive ordinary display values during rendering and put direct user actions in event handlers where appropriate. Follow the project's data-fetching architecture; account for races, cancellation, late responses, retry and stale data rather than adding ad hoc fetch effects to each view.

For fields, maintain a consistent controlled/uncontrolled model and keep controlled input updates responsive. Preserve composition input for languages that use IMEs; avoid formatting that jumps the caret or commits incomplete text. Validate at useful times rather than announcing errors on every intermediate keystroke.

`useId` can create IDs for accessible relationships; it is not the source of data keys for a list. Ensure label, help and error references remain unique when multiple instances of the same form appear.

Expose component state through appropriate semantics (`aria-expanded`, `aria-selected`, `aria-invalid`, etc.) with the actual correct pattern. A focusable custom control needs its complete keyboard contract; adding a role alone is insufficient. Reuse mature primitives, then test their integration.

## Async and data boundaries

For each action specify pending behavior, duplicate-activation handling, success confirmation, failure recovery and draft preservation. Optimistic updates are suitable only when the visible state can be reconciled and the consequences allow it. Do not declare a payment, permission change or irreversible operation successful merely because a request started.

Keep search/filter/sort/page state shareable in the URL when the task benefits from links and browser history. Keep sensitive data out of URLs. Announce relevant changes without moving focus unexpectedly. Restore list position and selection when returning from details where the task requires continuity.

Virtualization can reduce rendering cost but changes what exists in the DOM. Test keyboard navigation, assistive technology, selected items, focus retention, print, browser find and export. Prefer pagination or simpler rendering if they satisfy both scale and usability.

Use actual permission decisions from trusted application state to communicate availability. The server still enforces access. Clear or re-key tenant/user caches as needed to avoid showing another scope's data; coordinate the fix with the application's security architecture.

## Performance is observable behavior

Set field performance targets for loading, interaction and layout stability, segmented by relevant devices. Verify the current metric definitions and thresholds before interpreting them. A local sample cannot establish production performance or overall usability.

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

## Deliver contemporary materials and navigation on the web

Read [navigation-and-materials.md](navigation-and-materials.md) for the composition decision.

“HTML5 design” is not a visual specification. HTML defines semantic elements and behavior; CSS defines presentation mechanisms. Neither prescribes a fashionable palette, corner radius or shadow. Record these as product decisions and validate them against the task.

### Material is a rendering contract

Define each material by purpose, foreground/background pairing, opacity, blur, border, highlight, shadow, stacking level and fallback. Keep glass on a composited surface layer; do not lower the opacity of a wrapper that also contains text. Give diagrams, code, forms and tables a stable readable backing when they appear inside a translucent container. Test their entire scroll range over bright, dark, patterned and moving content. Contrast belongs to the resulting pixels, not an isolated color token.

CSS `backdrop-filter` filters content behind an element. Its result depends on transparency and backdrop-root boundaries; nested opacity/filter effects can change what is sampled. It does not automatically reproduce a native platform's material renderer, optical behavior or adaptive legibility. Apply it only when the current project's selected material requires it. Use a solid surface as the working baseline, enhance through feature queries, and verify the actual minimum supported browsers.

Verify current support for `prefers-reduced-transparency` in the project’s browsers. Honor it when available, but do not rely on every browser exposing the system preference. For a product with prominent translucent materials, provide a usable opaque appearance option and test the fallback. Respect forced colors and contrast preferences without removing the semantic distinction between selected, focused, disabled and destructive controls.

Shape and elevation need a small intentional grammar. Define a restrained radius hierarchy, nested inset relationships, and shadow direction/softness by layer. Decide whether a floating toolbar, anchored inspector, modal and content block should feel related or distinct. A dark-theme shadow may need a boundary highlight to communicate separation. Avoid applying one decorative shadow to every row or stacking blurred layers merely to appear advanced. These are design hypotheses to render and compare, not universal pixel values.

### Motion must preserve the interaction

Specify motion by cause: navigating deeper or back, revealing a contextual inspector, changing a selection, moving an item, saving, or receiving urgent information. For each, define what moves, origin/destination, continuity, cancellation, interruption and the reduced-motion alternative. Do not animate every incoming value in a monitoring grid or block an urgent action behind a transition. A changing datum should not reset the entire page animation.

CSS View Transitions can connect old and new visual states. Verify the exact API and browser support required by the project. Feature-detect the chosen API; keep the navigation/state update fully functional when unsupported or interrupted. Never make browser Back, focus restoration, document title, URL or draft retention depend on the animation completing.

If the project's installed React release supports `ViewTransition`, follow that release's integration contract. Current React documentation describes framework-coordinated transitions and explicitly notes that reduced motion is not disabled automatically. Do not layer a competing `document.startViewTransition()` coordinator around React's own transition mechanism. Inspect the lockfile and router before choosing an implementation; do not import an API from a newer documentation version into an older installed release.

Prefer transitions of transform and opacity when they express the intended result, and profile layout/paint/compositing costs on representative hardware. Properties requiring layout or paint can be more expensive than composited changes. This is a starting point, not a guarantee that an arbitrarily large blurred layer or video grid will perform well. Compare measured frame delivery and input response with the effects enabled and disabled.

### Navigation state survives adaptation

Model destination, selected object, local section, filter state, draft state and temporary overlay separately. When a wide list-detail layout becomes a narrow navigation stack, preserve the selected object's URL, the list's query/scroll context, its available actions and the route back. Do not create a second mobile data model or silently remount a form with a new key when the viewport changes.

Use links for destinations and buttons for commands. Give navigation regions distinct accessible names and mark the current destination. Do not turn an ordinary list of route links into an ARIA menu unless the complete menu interaction is intended. Modal drawers need dialog behavior; a persistent side panel does not automatically need a modal focus trap.

Measure space occupied by persistent navigation at the actual target sizes and text settings. A stack of app bar, breadcrumbs, section tabs, local tabs and sticky action bar can leave little space for the task even when every component passes separately. Record the resulting usable content area and demonstrate a simpler hierarchy. There is no universal maximum percentage: the decision follows the product's task and needs a rendered comparison.

Check sticky and floating controls while tabbing and scrolling with the on-screen keyboard. WCAG 2.4.11 AA requires a focused component not to be entirely hidden by author-created content; the skill's preferred design target is to keep the full focus indicator and relevant control comfortably visible. Distinguish that stronger design target from the criterion's minimum. Verify safe areas, reduced viewport height, long translated titles, split-window use and role-dependent navigation entries.

### Acceptance evidence for these effects

Record rendered bright/dark/busy backgrounds, each supported theme, the opaque fallback, reduced motion, input response under representative load, and interrupted/back navigation. Exercise a real content-first or maximum-workspace mode if the task needs one: entry and exit, keyboard recovery, critical-status visibility, saved selection and return to the previous arrangement. A static polished screenshot cannot close these checks.
