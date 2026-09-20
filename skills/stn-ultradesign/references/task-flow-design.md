# Task flows before interface polish

Use when a product feels complicated, hides useful work, or presents an attractive shell with incomplete primary workflows. Apply within the requested scope; this module does not turn a focused fix into a redesign. Reuse the [preference brief](discovery-and-preferences.md), existing approvals and [feature map](feature-parity.md). Substantial concepts retain the established twenty-question method; this procedure adds no question quota or approval gate.

## 1. Name the work and its first useful step

Describe each critical task as **actor → trigger → object or content → intended outcome**, without naming a proposed control. Connect it to existing capabilities and the user's confirmed priorities. Include normal repeated work and consequential exceptions, not only first use. Record what already works and must remain easy.

Trace **entry → first meaningful result → relevant context/detail → outcome → return**, using only the stages the task needs. The outcome may be understanding content, comparing an offer, completing a purchase or changing an object. For monitoring, the first useful result may be recognizing a relevant change without clicking. Distinguish opening a menu from making progress.

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

Separate search within the current collection from workspace-wide retrieval. Explain the searched scope, matching behavior, results and return path; keep keyboard shortcuts supplemental to visible access.

Favor recognition over remembering hidden commands, prior values or IDs. Shortcuts can accelerate a visible route, but they do not replace equivalent pointer, touch and accessible detail access.

## 3. Keep a coherent hierarchy across sizes

Separate product destinations, collections, individual objects, local views and commands. Do not place them at one visual level merely because tabs are convenient. Label the current object and scope near the work. Avoid unrelated global sections appearing inside an object's local tabs.

Before polishing connected surfaces, trace which object owns each value or action, its scope and relationship cardinality: one item, several related items or a shared definition. Distinguish a derived view from an independent setting and useful repeated access from conflicting duplication. Record the consequences of changing, moving or removing either, including which other surfaces or objects change. Preserve valid differences in purpose, ownership and scope; this mapping does not itself authorize data-model changes.

Choose persistent peers when frequent switching benefits from them; use hierarchy for real parent-child relationships. Measure avoidable travel and uncertainty rather than enforcing an arbitrary maximum click count.

Preserve useful existing navigation unless the requested change or demonstrated task benefit supports replacing it. On a wide workspace, a global rail plus a local settings sidebar can expose distinct scopes and show the selected content directly. Do not replace this with a mandatory overview-and-return loop merely to reduce the number of visible columns. Compare opening a category, switching among peers and returning in both versions, including draft preservation and usable content width. A directory can help first-time orientation without becoming a repeated detour. Use the [settings pattern decision table](navigation-and-materials.md#decongest-settings-without-losing-features) to balance frequency, space and familiarity.

On compact layouts, use a clear collection → object → detail sequence when simultaneous panes no longer fit. Preserve identity and context rather than stacking every desktop navigation region.

Define Back, close, parent navigation and direct-entry behavior separately. Returning should restore relevant selection, filters, sort, time, scroll and focus. A deleted source needs a logical successor. A drawer is suitable only while its content remains readable and its task understandable; a full page may better support extensive work. Preserve the approved brand and device preferences when selecting these forms.

## 4. Minimize competing structure, not required work

For each persistent region record its task, frequency, concealment risk and space cost. Remove repetition and decorative framing before reducing text size or hiding needed controls. Use proximity to group relationships and a coherent spacing system to separate different decisions.

Progressive disclosure needs a visible invitation and useful content behind it. A compact overview may defer detailed metrics, history or configuration, but the relevant object must visibly offer those paths. Check that reduction has not erased an existing graph, event sequence, export or diagnostic branch. Critical failures remain perceivable when optional chrome is hidden. Focus modes need an available exit and an explicit restoration contract.

For repeated tasks, compare entry to the first meaningful result, peer switching and return. Count actions, navigation transitions, focus traversal, re-entry and context switches; eliminate unnecessary effort rather than chasing a universal click limit. Compare direct peer selection with Back → overview → next item. Check correctness, wrong turns, reading burden, latency and recovery alongside counts. One overloaded screen can be slower than a clear sequence. Preserve consequential confirmations and useful safeguards; fewer clicks alone do not establish a better workflow.

## 5. Connect live signals to investigation

Use [analytical meaning](analytical-meaning.md) for definitions and [data visualization](data-visualization.md) for interaction/data scope. For each relevant live surface, connect current value or event → affected object → time-aligned detail → supporting evidence → permitted action → return. Existing statistics and events need actual reachable views, not attractive placeholders.

Keep contextual linkage and freshness as separate contracts. A related-event panel must identify its object and time scope even when its data requires explicit refresh.

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

For live investigation, evaluate pause/resume, contextual detail and refresh cadence against the actual operational task. A visual streaming simulation cannot prove production delivery or buffering behavior.

Use safe fixtures to exercise delayed/out-of-order data, empty periods, connection loss, restoration and permission changes where reachable. Do not fabricate metric data, claim native streaming performance from animation, or seek unauthorized records. Keep updates understandable without constantly moving the inspected item or flooding assistive announcements.

## 6. Use proportion as a candidate, not a certificate

The golden ratio, approximately 1.618, can generate a candidate division or rhythm. It does not determine the correct sidebar, chart, dialog or media-grid dimensions. A rectangle preference is not evidence of faster navigation, readable labels or useful information capacity.

Proportional systems can help explore composition, but no fixed rectangle ratio proves business-interface quality. Judge the visible content relationships, reading order and task performance under real constraints.

Start with task space, intrinsic content, useful media aspect ratio, reading width and control constraints. Compare a proportion-based candidate with a content-driven alternative using identical content and conditions. Keep a ratio only when the rendered result improves the intended relationship without clipping, excessive wrapping, lost comparisons or unnecessary navigation. Test both themes and relevant intermediate widths. Do not distort data scales or crop meaningful imagery to fit a mathematical motif.

## 7. Expose missing primary workflows before presentation

Before calling a concept ready for its declared scope:

1. Reconcile each critical task with a visible entry, complete proposed path, required detail/evidence, result and return. List undisplayed capabilities separately. A screenshot or feature-map label cannot close a missing task.
2. Walk each critical path from its actual entry in the rendered artifact, including first-use, empty or unselected states when reachable. Give the reviewer the task without author cues naming the route or control. Record whether the entry was discoverable separately from whether its handler completed the task; direct activation can verify the latter while leaving the former failed. Exercise meaningful failure and compact/input variants. Record prototype, application and untested evidence distinctly.
3. Show the resulting task matrix alongside the concept. A primary task with only a placeholder keeps that part unfinished. A partial concept may still be presented explicitly as partial; do not quietly shrink the agreed scope.
4. Compare the revision with its baseline using the same safe task/fixture. Preserve strengths and explain changes in effort, clarity and available work. Representative expert walkthroughs identify hypotheses; they are not user studies. User observation is needed to claim demonstrated comprehension or faster performance.
5. Translate criticism into **observed failure → affected task → concrete change → acceptance condition → new evidence**. Re-render and repeat the affected journey. “More minimal” is not a completed correction. A user's rejection stays open until explicitly resolved.

For a full audit, continue through every discovered in-scope usage and defined transition under [audit-method.md](audit-method.md); critical-task prioritization is an order of work, not sampling permission. Concept reviewability does not establish production readiness or authorize implementation. Follow the existing [concept approval contract](concept-to-code.md).
