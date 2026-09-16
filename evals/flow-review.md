# Dispatch concept review — source-only evaluation

**Verdict:** the draft is not complete for its stated workspace scope. The next revision should complete the delivery-investigation journey, connect summaries to the right records, and restore list context. Visual refinement cannot close the missing scan history, tracking search, transit analysis, and route-rule branches.

This is a bounded review and a proposed next-revision contract, not a new application, an approved design, a production audit, or permission to implement production changes.

## Evidence and limits

Reviewed on 2026-09-16: the supplied task, its `index.html`, and STN Ultradesign with the relevant workflow, product, parity, discovery, analytical, accessibility, adaptation, and verification references. No other project concept, previous evaluation, public research document, account, or production page was inspected. No browser, rendering, runtime interaction, screen reader, automated accessibility check, or user study was used.

Source findings below establish what this fixture defines and omits. They do not establish actual layout, browser focus behavior, task speed, user comprehension, production behavior, authorization enforcement, or accessibility conformance. External links in the skill were not followed; vendor patterns are not evidence about this product.

Reproducible source identity (SHA-256):

- `outputs/stn-ultradesign/evals/flow-fixture/index.html`: `7e7d5771a286c3ecaf927eb09945bec95edefd8ecb95339f1727eebb1879fe18`.
- `outputs/stn-ultradesign/evals/flow-fixture/task.md`: `5bcadcc4c4b7d2a2f9c3194d7aef97fb116d0aee55527d82cfda6546e291364b`.
- `outputs/stn-ultradesign/skills/stn-ultradesign/SKILL.md`: `db87ea4fbf59a21409d738fb4d8402ba20678bd4245dee07d65804fc89ec305f`.

## Product and task brief

The supplied notes establish two actors: dispatchers monitor late deliveries and investigate a delivery; team leads also configure route rules. The primary work unit is an identifiable delivery, with scan events and transit measurements as supporting evidence. Monitoring becomes investigation when a dispatcher identifies a late record or receives a tracking reference. Successful investigation means finding the intended delivery, inspecting its scans and last-hour transit measurements with trustworthy time context, then returning to the same working list. Configuring a route rule is a separate administrative task with an explicit target, change, and result.

Confirmed constraints are compact readability, both themes, keyboard and touch, timezone-bearing scan timestamps, and potentially missing measurements. The number of concurrently monitored deliveries, operational urgency, refresh tolerance, exact late-delivery definition, transit-time definition, route-rule fields, and supported browsers remain unknown. Misidentifying a delivery or interpreting stale/missing data as a current measurement could misdirect investigation; the actual business cost has not been supplied.

Retain the useful beginnings: readable domain labels, textual delivery states, native form controls with visible labels, semantic table structure, explicit row-open actions, a selected-reference heading, an explicit return button, and honest synthetic-data labeling. Their runtime quality remains untested.

## Prioritized findings

Priority describes consequence for the supplied tasks, not measured incident frequency.

| ID | Priority and evidence | Consequence | Concrete correction |
| --- | --- | --- | --- |
| F01 | High — `index.html:10–11`: **More → Delivery tools → Scan history / Statistics** ends at buttons without actions or content. There is no history filter. | The primary investigation never reaches its supporting evidence; opening a modal is not useful task completion. | Put **Scan history** and **Transit time** visibly in the selected delivery's detail. Supply real proposed content, working filters and a return path in the next synthetic revision. |
| F02 | High — lines 7–9: no tracking-reference search; **Apply** has no handler or form submission. The list, metric and scope text are static. | Known-reference retrieval and region/date scoping are absent from the proposed workspace. | Add labeled tracking search and an explicit applied-scope contract shared by list and summary. Include a no-match result and recovery. |
| F03 | High — lines 10, 13, 15: opening a record changes only its heading. The same latest scan and static SVG remain; the numeric output changes randomly every second and never reads the Live checkbox. | The apparent investigation data is not tied to the selected delivery. The Live affordance promises control the fixture does not provide. | Bind record identity, scans and measurements to the same deterministic synthetic dataset. Define and implement pause/resume, freshness and missing-data behavior. |
| F04 | High — line 14 explicitly resets region to its first option and date to `2026-09-16` on return. | Returning to monitoring loses even the filter values the person entered. | Preserve the applied scope and list position; restore focus to the originating delivery action or a documented successor. |
| F05 | High for scope completion — line 5 links to `#rules`, but no corresponding surface or edit flow exists. `#deliveries` and `#profile` likewise lack matching targets. | A complete workspace claim conceals the team lead's required configuration branch. | Retain Route rules as a distinct destination and design its full proposed edit/result/return flow using the actual rule contract when supplied. Profile's intended contents remain unknown; do not invent account features. |
| F06 | High — line 8 presents **18 late deliveries**, but its arrow opens hard-coded `PK-104`. Lines 10 and 15 omit transit units, time axis/window, missing samples and meaningful sample linkage; the scan shows `09:34` without a timezone. | Summary drill-through changes grain without explaining which record was chosen. Timing evidence cannot support a defensible conclusion. | Make the summary open its contributing late-delivery list. Show selected-object identity, an explicit one-hour interval, timestamp timezone and confirmed units; distinguish absent samples from zero. |
| F07 | Medium, with runtime gaps — line 4 defines only a light palette, no adaptation rule for the nonwrapping filter row, and a hover-only hint. Detail changes have no explicit focus handling. The chart has an accessible name but no equivalent values/description. | Both-theme coverage is missing in source. Compact, touch and keyboard task continuity are unverified, with concrete risks to investigate. | Produce both theme variants, adaptive task layouts, visible text actions, chart data access and explicit focus contracts. Verify rendered behavior; do not declare a contrast, target-size or focus failure from CSS absence alone. |

The count of 18 and the two displayed rows are not sufficient evidence of a numerical error: this is a synthetic fixture with an undocumented population. Their relationship is undefined and must be made explicit, rather than forcing the count to equal all visible rows.

## Current capability map and proposed destination

All dispositions are proposals; none is approved or verified. No capability is retired.

| Capability | Current fixture | Next destination and preservation contract |
| --- | --- | --- |
| Region and date selection | Inputs exist; application is inert | Collection toolbar; preserve selected and applied values, define their time basis and effect. |
| Tracking-reference search | Absent | Labeled collection search; preserve authorized search semantics once confirmed, show effective scope and direct result opening. |
| Monitor late deliveries | Static count and list | Scoped collection, with count linked to contributing late records and explicit completeness/freshness. |
| Open individual delivery | Reference heading changes | Selected delivery detail; identity, state and evidence all refer to that delivery. |
| Scan history and filtering | Unimplemented button in More | Visible local Scan history section/view; actual timestamped events and functioning scan filters. |
| Last-hour transit measurements | Unlabeled static path plus unrelated random number | Visible local Transit time section/view; time-aligned chart and equivalent table, including missing data. |
| Return to original list | Button resets inputs | Back/close returns to preserved region, date, query, list state, selected row and focus. |
| Team-lead route rules | Dead destination | Separate Route rules destination; known team-lead editing capability preserved, actual scope and fields pending. |
| Light/dark, keyboard/touch | Light styling and some native controls only | Every required journey in both themes and both input methods; no core operation depends on hover. |
| Profile destination | Dead link; no supplied capability description | Record as unfinished/undefined; establish its purpose before assigning content or removing it. |

Existing locales, system-theme following, density switching, export, sorting, saved views, escalation actions and additional permission roles are not established by the supplied evidence. Do not present them as preserved features or silently add them as required scope.

## Outstanding decisions — all pending

No user interview or delegation is claimed. This review can proceed without answers, while dependent meaning, access and final visual choices remain open. The following early discovery record supports a later substantial concept; it does not make twenty answers or approvals a condition of delivering this review.

Resolve business meaning and task dependencies first:

1. What event and boundary make a delivery “late,” and who owns that definition? This determines count, status and filtered population.
2. Does the selected date mean promised delivery date, dispatch date, scan date or another date, in which timezone? This governs list and summary agreement.
3. What does transit time measure, in which unit and aggregation, and what does each last-hour sample represent? This governs chart validity.
4. How are missing, delayed and stale samples distinguished, and what freshness makes this information useful? This governs status and refresh behavior.
5. Does tracking search respect region/date filters, or search a wider authorized collection? This determines explicit scope and no-match recovery.
6. What rule fields, effective scope, validation and save consequences do team leads actually configure, and what can dispatchers read? This blocks an honest detailed rule-edit contract, not the dispatcher review.

Twenty distinct preference/working-practice questions for the next visual direction follow. Each is unanswered; none repeats the already confirmed requirement to support both themes, keyboard, touch or compact readability.

| Question | Decision affected |
| --- | --- |
| Q01. On entry, should dispatchers see late deliveries first or all deliveries with late items emphasized? | Opening collection and primary emphasis. |
| Q02. Which late-delivery characteristic should drive the first scan of the list: delay, destination or another verified attribute? | Information priority; no invented attribute is assumed available. |
| Q03. Which list facts must remain visible during investigation? | Persistent context alongside detail. |
| Q04. How often do dispatchers compare consecutive deliveries versus finish one before opening another? | Peer navigation and list/detail tradeoff. |
| Q05. Should the first detail view emphasize recent scans or the transit timeline? | Detail hierarchy. |
| Q06. Should scans be newest-first or chronological during a typical investigation? | Event reading sequence. |
| Q07. Which known scan-filter choices should be directly visible, and which may sit in labeled disclosure? | Filter density and discoverability. |
| Q08. When inspecting a past point, should the view pause automatically or require an explicit pause action? | Stable inspection and clearly signaled live state. |
| Q09. On resuming live display, should new information be summarized before returning to now? | Interruption and resume presentation. |
| Q10. Which scope and selection should survive leaving and reopening the workspace, beyond the required immediate Back restoration? | Optional persistence boundaries. |
| Q11. Is simultaneous list/detail or a wider full-page investigation preferable for the actual daily cases? | Structural alternative to validate. |
| Q12. Which delivery facts are essential at a glance on a phone? | Compact collection composition without loss of detail access. |
| Q13. During tablet use, is quick collection switching or more space for scans the greater priority? | Medium-width arrangement. |
| Q14. Within readable compact rows, should destination names wrap or reveal their full text through an accessible detail treatment? | Row height and scanability. |
| Q15. Which visible labels should remain familiar to dispatchers, especially “Transit time” and “Scan history”? | Vocabulary continuity. |
| Q16. Which theme should first appear in the actual working environment? | Initial presentation; both themes remain required. |
| Q17. Which product name and identity should the workspace represent, given the draft's “Parcel desk” title and “Delivery operations” heading? | Naming and brand authority. |
| Q18. Should the current system-font character remain, or should a different authorized type direction be explored? | Typography inheritance. |
| Q19. Should accent color primarily identify interaction, selected delivery or another specific purpose, while statuses stay distinct? | Color roles and attention hierarchy. |
| Q20. Which of the current rounded panels, restrained surfaces and motion character should be retained, evolved or opened to exploration? | Shape/material/motion inheritance, separately from layout. |

## Recommended next revision: `dispatch-investigation/v0.2` — specification draft

**Visual thesis, provisional:** make the delivery list and its evidence the dominant workspace. Use a compact scope/search strip and a modest late-delivery summary; make the selected delivery's scans and transit timeline directly recognizable. Route-rule configuration remains a product destination, not a delivery-local tool.

Compare two structures with the same fixture before choosing final layout: a persistent list beside the selected delivery preserves peer context but reduces evidence width; sequential full-page list/detail gives investigation more space but depends more on reliable restoration. A list/detail arrangement is the candidate for sufficiently wide windows; sequential detail is the candidate when both panes cannot remain useful. Neither is a proven winner. No fixed ratio or universal breakpoint is asserted.

Each persistent region has a task reason: product navigation switches Deliveries/Route rules; scope and search identify the collection; the list supports monitoring and selection; a compact detail header maintains delivery identity, state and return; the evidence area supports investigation. A large isolated metric card and generic More dialog need not dominate these tasks. Keep critical stale/missing status visible even when secondary detail is collapsed.

Provisional brand inheritance: preserve established domain vocabulary and synthetic-data honesty; retain system typography as an unapproved neutral starting point; explore theme-specific semantic colors without treating the current yellow chart line as a brand rule; evolve repeated rounded containers and spacing only where they improve working space; use visible text labels with supplementary icons; introduce no imagery without a task reason; define restrained state feedback and reduced-motion behavior. No supplied brand authority or asset license is inferred.

### Next-revision acceptance contract

All checks below are **not run**. They describe the next isolated concept revision and its evidence obligations, not passed tests.

| ID | Concrete revision requirement | Acceptance evidence to obtain |
| --- | --- | --- |
| C01 | Apply region/date through one explicit scope model. Summary, rows and scope labels use the same applied values. Keep draft input distinct if Apply remains. | In a deterministic fixture, change both inputs and apply; compare expected rows/count/context, including an empty intersection and timezone-boundary date. |
| C02 | Provide labeled tracking-reference search with clear authorized/filter scope and accessible results. | Find each fixture reference, open the correct result, recover from no matches and clear the query without unexplained scope changes. Unknown search semantics stay an explicit dependency. |
| C03 | A late-delivery summary opens the matching collection, not an arbitrary record. Row actions identify their delivery. | From the summary, reach its contributing records and open one; demonstrate why the count agrees with its population or disclose a partial list. |
| C04 | Detail visibly identifies reference and state. Scan history and Transit time have direct local entries or visible sections; remove the mandatory More detour for these primary tasks. | Open `PK-104` and `PK-109`; show distinct, deterministic evidence for each. Neither branch ends at a placeholder. |
| C05 | Scan history displays actual synthetic events, dates and timezone-bearing times. Filters produce visible scope, results and a reset path. | Filter a multi-event history, inspect a selected event and recover from zero matches. Preserve distinction between no matching scans and failed loading. |
| C06 | Transit detail explicitly covers the last hour, with confirmed units, sample timestamps, window endpoints and selected-delivery identity. Supply exact-value access and a useful accessible description. | Reconcile chart/table against the same fixture. Include true zero, one missing sample, an empty period and delayed data. Gaps remain gaps; no fabricated zero or connecting line implies observations that do not exist. |
| C07 | Define Live as display-follow behavior. Proposed Pause freezes the inspected window/selection while clearly exposing incoming/stale status; it does not imply collection stopped. Resume explicitly returns to the current window. | Pause during updates, inspect a timestamp, introduce delayed/out-of-order and unavailable-data cases, then resume. Show whether history has gaps; do not silently jump to now while paused or on return. |
| C08 | Scans and transit share an explicit timezone and relevant time context. If selecting a scan changes the chart window, label that effect and provide a return to the last-hour view. | Trace one timestamp from event to measurement evidence without claiming a causal relationship unsupported by data. Event-linked chart navigation is a proposed enhancement requiring shared identifiers/time data, not an established existing capability. |
| C09 | Back/close restores the original list's applied region/date, query, selection and scroll, plus focus to the invoker or a defined successor. Preserve any other list state actually introduced. | Start with nondefault region/date and a searched/selected record; inspect and return. Repeat after resize and a new incoming record. If routing/history is introduced, verify browser Back and define direct-entry fallback explicitly. |
| C10 | Deliver a concrete Route rules branch for team leads once its real field/scope contract is available: entry → identify target/scope → edit → validate → save result or recoverable error → return. | Use safe synthetic rules and actual documented capability distinctions; preserve drafts after failure and define cancel. Until the missing contract is resolved, mark this branch unfinished and the overall workspace partial. No live configuration action is authorized. |
| C11 | Show both themes and adapt list/detail by usable width. Keep the complete dispatcher journey reachable through keyboard and touch; filters and evidence remain accessible on narrow screens. | Render and interact at compact, medium and wide sizes plus layout boundaries and zoom. Record actual dimensions, browser and fixture. Check full labels, local table overflow, dialog behavior if any, theme contrast and focus. |
| C12 | Establish explicit keyboard focus on opening detail and returning; visible actions replace reliance on hover hints. Use understandable modal naming/focus behavior for any retained modal. Avoid incessant live announcements. | Manual keyboard and supported assistive-technology walkthrough, accessibility-tree inspection and appropriate automated checks. WCAG 2.2 AA is a recommended design target, not a conformance or legal claim. |
| C13 | Demonstrate loading, empty, partial/missing, stale/unavailable and retry where the proposed data flow can reach them, preserving scope and selected object. | Safe fixture states show truthful feedback and recovery; no empty state masquerades as a failed request, and no failure replaces preserved inspection with unrelated data. |
| C14 | Refine the rendered concept using the same end-to-end scenario and record old/new evidence. Keep missing branches and open decisions visible. | Annotated rendered views plus interaction results for monitor → identify → inspect scans → inspect timing → return. Owner feedback and approval are separate records; neither is inferred from passing technical checks. |

The desired outcome for the dispatcher walkthrough is correct identification and evidence interpretation with preserved return context. Record independent completion, wrong turns, assistance and misinterpretation when representative users are available. Measure time only in comparable successful tasks; no numerical improvement is claimed now.

**Ready now:** a source-backed diagnosis and reviewable revision specification. **Not ready:** a completed visual concept, complete workspace, production implementation, verified feature parity, runtime accessibility result, or claim that users work faster. Route rules and the semantic decisions above remain explicit dependencies; the production-page audit remains outside this exercise.
