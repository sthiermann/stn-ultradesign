# Task flows before interface polish

Use when a product feels complicated, hides useful work, or presents an attractive shell with incomplete primary workflows. Apply within the requested scope; this module does not turn a focused fix into a redesign. Reuse the [preference brief](discovery-and-preferences.md), existing approvals and [feature map](feature-parity.md). Substantial concepts retain the established twenty-question method; this procedure adds no question quota or approval gate. Source review: 2026-09-16.

## 1. Name the work and its first useful step

Describe each critical task as **actor → trigger → object → intended outcome**, without naming a proposed control. Connect it to existing capabilities and the user's confirmed priorities. Include normal repeated work and consequential exceptions, not only first use. Record what already works and must remain easy.

Trace **entry → first meaningful action → object context → evidence/detail → decision or action → return**. For monitoring, the first useful result may be recognizing a relevant change without clicking. For investigation, it may be selecting the affected object and period. Distinguish opening a menu from making progress.

For every step, identify what the user knows, what they need to recognize, the visible affordance, required data, authorized role, feedback and next destination. Mark missing content, inaccessible states and simulated behavior. An inventory entry named “statistics” does not establish a usable statistics workflow. Use the [task-flow record](../assets/task-flow.template.md), linked to existing surface, usage and transition IDs.

## 2. Make the next action recognizable

| Need | Design decision | Failure to test |
| --- | --- | --- |
| Repeated primary destination | Stable, understandable name and visible access in its task context | An unexplained icon or hidden gesture is the only route |
| Find a known object | Scoped search, useful result identity and direct opening | Search silently covers another account or only loaded records |
| Explore unfamiliar content | Visible categories, filters and meaningful defaults | Users must know a query language before discovering available work |
| Inspect briefly | Contextual preview with a clear route to full detail | Preview conceals essential fields or becomes a dead end |
| Work across peers | Retain a list, next/previous control or useful sibling navigation | Repeated return to a distant parent merely to open the next object |
| Rare secondary command | A labeled, discoverable group or overflow | A frequent or critical command disappears to make the layout cleaner |

Make search scope visible at its entry and in results. Advanced query syntax may accelerate repeated work, but should not silently replace discoverable filters. Research the requested product or platform conventions; this skill prescribes no fixed search position or visual language.

Linear distinguishes workspace search from searching a current view; Stripe provides immediate matches and fuller result views. Borrow the explicit retrieval contract, not the vendors' exact shortcuts or ranking. [Linear search](https://linear.app/docs/search), [Stripe search](https://docs.stripe.com/dashboard/search)

Favor recognition over remembering hidden commands, prior values or object IDs. Shortcuts and command menus can accelerate a visible route. Linear's Peek is documented as keyboard-only; it illustrates rapid inspection, not equivalent access for all inputs. Provide an appropriate pointer/touch route and accessible detail equivalent in the target product. [Linear Peek](https://linear.app/docs/peek)

## 3. Keep a coherent hierarchy across sizes

Separate product destinations, collections, individual objects, local views and commands. Do not place them at one visual level merely because tabs are convenient. Label the current object and scope near the work. Avoid unrelated global sections appearing inside an object's local tabs.

Choose persistent peers when frequent switching benefits from them; use hierarchy where there is a real parent-child relationship. Do not invent a maximum number of clicks or navigation levels. Microsoft's guidance discusses both structures and avoiding repeated up-and-down travel; its numerical recommendations are contextual Windows guidance. [Microsoft navigation](https://learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics)

Preserve useful existing navigation unless the requested change or demonstrated task benefit supports replacing it. On a wide workspace, a global rail plus a local settings sidebar can expose distinct scopes and show the selected content directly. Do not replace this with a mandatory overview-and-return loop merely to reduce the number of visible columns. Compare opening a category, switching among peers and returning in both versions, including draft preservation and usable content width. A directory can help first-time orientation without becoming a repeated detour. Use the [settings pattern decision table](navigation-and-materials.md#decongest-settings-without-losing-features) to balance frequency, space and familiarity.

On compact layouts, make collection → object → detail a clear sequence when simultaneous panes no longer fit. Preserve identity and context instead of stacking every desktop navigation bar. Google's list-detail pattern explicitly adapts between simultaneous and sequential views. [Android common layouts](https://developer.android.com/design/ui/mobile/guides/layout-and-content/common-layouts)

Define Back, close, parent navigation and direct-entry behavior separately. Returning should restore relevant selection, filters, sort, time, scroll and focus. A deleted source needs a logical successor. A drawer is suitable only while its content remains readable and its task understandable; a full page may better support extensive work. Preserve the approved brand and device preferences when selecting these forms.

## 4. Minimize competing structure, not required work

For every persistent region record its task, frequency, consequence of concealment and space cost. Remove repetition and decorative framing before reducing text size or hiding necessary controls. Group strongly related information closely; separate unrelated decisions. Atlassian documents proximity and a consistent grid/spacing system, but its token values are not universal dimensions. [Spacing](https://atlassian.design/foundations/spacing), [Grid](https://atlassian.design/foundations/grid)

Progressive disclosure needs a visible invitation and useful content behind it. A compact overview may defer detailed metrics, history or configuration, but the relevant object must visibly offer those paths. Check that reduction has not erased an existing graph, event sequence, export or diagnostic branch. Critical failures remain perceivable when optional chrome is hidden. Focus modes need an available exit and an explicit restoration contract.

For repeated tasks, compare entry to the first meaningful result, peer switching and return. Count actions, navigation transitions, focus traversal, re-entry and context switches; eliminate unnecessary effort rather than chasing a universal click limit. Compare direct peer selection with Back → overview → next item. Check correctness, wrong turns, reading burden, latency and recovery alongside counts. One overloaded screen can be slower than a clear sequence. Preserve consequential confirmations and useful safeguards; fewer clicks alone do not establish a better workflow.

## 5. Connect live signals to investigation

Use [analytical meaning](analytical-meaning.md) for definitions and [data visualization](data-visualization.md) for interaction/data scope. For each relevant live surface, connect current value or event → affected object → time-aligned detail → supporting evidence → permitted action → return. Existing statistics and events need actual reachable views, not attractive placeholders.

Stripe's Inspector connects objects with related logs and events, while its log view explicitly requires refresh. This demonstrates why contextual linkage and freshness are separate contracts. [Stripe Workbench](https://docs.stripe.com/workbench/overview)

Record the following where supported:

| Contract | Required distinction |
| --- | --- |
| Time | Event time, observation time, ingestion, display refresh; timezone and absolute versus rolling window |
| Measure | Unit, aggregation, interval, selected object/population, missing samples and threshold authority |
| Live state | Following current data, paused inspection, historical view, reconnecting, stale or unavailable |
| Pause | Whether display movement, queries or collection stop; never imply recording stopped unless it did |
| Resume/reconnect | Resume position, buffered/new items, duplicates, gaps and whether history is complete |
| Investigation | Event selection and chart range remain aligned; changing one filter exposes the affected scope |
| Return | Restore object, period and selection; do not jump to “now” without a defined user action |

Grafana's log exploration offers pause/resume and contextual detail, and its refresh guidance balances update cadence with actual need. These are candidate behaviors; they do not prove a different application's streaming implementation. [Grafana logs](https://grafana.com/docs/grafana/latest/visualizations/explore/logs-integration/), [Refresh guidance](https://grafana.com/docs/learning-paths/visualization-logs/time-range-refresh/)

Use safe fixtures to exercise delayed/out-of-order data, empty periods, connection loss, restoration and permission changes where reachable. Do not fabricate metric data, claim native streaming performance from animation, or seek unauthorized records. Keep updates understandable without constantly moving the inspected item or flooding assistive announcements.

## 6. Use proportion as a candidate, not a certificate

The golden ratio, approximately 1.618, can generate a candidate division or rhythm. It does not determine the correct sidebar, chart, dialog or media-grid dimensions. A rectangle preference is not evidence of faster navigation, readable labels or useful information capacity.

Russell's experiments report that judgments and context affect preferred rectangle proportions. A 2024 study reports favorable implicit associations but mixed explicit ratings. Neither establishes universal business-interface superiority. [Russell, 2000 abstract](https://pubmed.ncbi.nlm.nih.gov/10742842/), [Salera and colleagues, 2024 abstract](https://iris.uniroma1.it/handle/11573/1721721)

Start with task space, intrinsic content, useful media aspect ratio, reading width and control constraints. Compare a proportion-based candidate with a content-driven alternative using identical content and conditions. Keep a ratio only when the rendered result improves the intended relationship without clipping, excessive wrapping, lost comparisons or unnecessary navigation. Test both themes and relevant intermediate widths. Do not distort data scales or crop meaningful imagery to fit a mathematical motif.

## 7. Expose missing primary workflows before presentation

Before calling a concept ready for its declared scope:

1. Reconcile each critical task with a visible entry, complete proposed path, required detail/evidence, result and return. List undisplayed capabilities separately. A screenshot or feature-map label cannot close a missing task.
2. Walk each critical path in the rendered artifact without relying on the designer's explanation. Exercise meaningful failure and compact/input variants. Record prototype, application and untested evidence distinctly.
3. Show the resulting task matrix alongside the concept. A primary task with only a placeholder keeps that part unfinished. A partial concept may still be presented explicitly as partial; do not quietly shrink the agreed scope.
4. Compare the revision with its baseline using the same safe task/fixture. Preserve strengths and explain changes in effort, clarity and available work. Author walkthroughs identify hypotheses; user observation is needed to claim demonstrated comprehension or faster performance.
5. Translate criticism into **observed failure → affected task → concrete change → acceptance condition → new evidence**. Re-render and repeat the affected journey. “More minimal” is not a completed correction. A user's rejection stays open until explicitly resolved.

For a full audit, continue through every discovered in-scope usage and defined transition under [audit-method.md](audit-method.md); critical-task prioritization is an order of work, not sampling permission. Concept reviewability does not establish production readiness or authorize implementation. Follow the existing [concept approval contract](concept-to-code.md).
