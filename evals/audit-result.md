# Independent UI/UX audit: Luma Operations

Date: September 16, 2026. Mode: audit only; the application was not changed.

**Result:** All three implemented pages and all application actions defined in the source were exercised in the running fixture, including both project drilldowns, every deletion-dialog exit and webhook details. Significant problems with forms, keyboard operation, dialogs and reliable feedback were confirmed. **This is not a completed full UI/UX or WCAG audit:** responsive layouts, several input methods and the complete applicable WCAG criteria review remain outstanding.

## Basis and actual scope

- Task: `evals/audit-fixture/task.md`.
- Skill used: `skills/stn-ultradesign/SKILL.md`, particularly `audit-method.md`, `verification.md`, `accessibility.md`, `data-visualization.md`, `business-administration.md` and `developer-platforms.md`.
- Only application source examined: `evals/audit-fixture/index.html`, 21 lines; SHA-256 `74ee7a4c906066c108c9cb10b3ad81bf8f7ab55062e19ad2f4301b0e4c4d76e3`.
- Runtime: `http://127.0.0.1:8767/`, Microsoft Edge on macOS, dedicated tab. Browser and OS versions were not recorded. CUA had no browser provider; inspection used native application control, the accessibility tree and screenshots.
- Visible role: only “member,” workspace “Example Workspace,” synthetic identity Casey. Other roles, tenants, feature flags and configurations are not implemented.
- The browser confirmed 100% zoom at the end. A brief change to 110% was reverted. Attempts to reach 200% did not produce a verified 200% test. Screenshot dimensions of 1280 × 768 are **not** a CSS-viewport measurement.
- The fixture has no real server, real keys or external side effects. Its purported deletion was therefore exercised as an authorized simulation.
- At the end, CUA reported that the Mac was locked and could not be unlocked automatically. Further runtime tests were blocked. The last verified state was `#missing`; a subsequent attempt to return was prevented by the lock.

No other evaluation files, scoring rubrics or conclusions were read. No application changes, installations or backend security tests were performed. This English edition translates the archived report; it is not a new test run.

## Evidence log

The excerpts below come from UI states actually returned during the run. Screenshots were visually examined but not archived as separate image files. Evidence here consists of observation notes, accessibility-tree excerpts, source locations and calculated contrasts.

| ID | Executed check and observation |
|---|---|
| E01 | Entry `/`: Overview, Settings and Developers are present. Overview shows Jan 98%, Feb 99%, Mar 100%, “Monthly completion increased dramatically.” and a Teams table. The accessibility tree also exposes all three values as text. |
| E02 | Opened `Operations →`: “Operations projects” and `Project Linden` appear. Opened `Project Linden`: heading, “3 overdue tasks,” `Close details`. Closing removes details; the tree then reports focus on HTML content rather than the project trigger. |
| E03 | Settings: changed Display name from Casey to `Casey Updated` and Notification email to `invalid-email`. Tab from the email field moves directly to `Delete workspace`. The tree lists `Save changes` as text only. |
| E04 | Pointer activation of `Save changes` resets both fields to Casey and casey@example.test; “Server unavailable. Try again.” appears. No field-level validation precedes this outcome. Activating again with the restored defaults gives the same error. |
| E05 | `Delete workspace` opens an overlay; the tree still places focus on the background trigger. Escape does not close it. Tab focuses `×`; Shift+Tab returns to the background trigger. The overlay is exposed as a container, not a named dialog. |
| E06 | Closed the dialog separately through `Cancel` and `×`; both work visually, with focus subsequently on HTML content. Reopened and selected `Delete everything`: native alert “Deletion simulated; no real data changed.” Dismissed with `OK`. |
| E07 | Developers: readonly field containing `demo_value_not_a_live_secret`; scope options `Full workspace access` and `Read only`. Selected `Read only`, activated `Save`: “Changes saved.” Reload restores `Full workspace access` and removes the message. Save was also exercised in the default scope. |
| E08 | Webhooks says “No deliveries yet.” `View delivery details` opens “Delivery attempts / Loading…”. Loading persists in a later screenshot and after navigation/browser Back. Source contains no completion, failure or retry transition. |
| E09 | Navigated Developers → Overview; browser Back returns to Developers and preserves its local message/drilldown state; Forward returns to Overview. Entering `#missing` hides all main content while retaining the header and navigation. |
| E10 | Visually inspected Overview, both project levels, the dialog and Developers with delivery details open. Chart bars have radically different lengths; secondary gray text appears weak. No formal screenshot pixel measurements were taken. |
| E11 | Reproducible contrast calculation from CSS colors using WCAG sRGB linearization: `#b9bec7` on `#f4f6fa` = **1.725:1**; on white = **1.866:1**. Controls: white on `#244bc5` = 7.272:1; `#242b39` on `#f4f6fa` = 13.118:1. Image compression was not a measurement source. |
| E12 | Source: fixed 1200px shell without media/container queries (line 7); bar widths 10/105/220 for values 98/99/100 (line 11); Save div without button/keyboard semantics (line 12); global dialog divs without focus logic (line 15); unknown hashes without fallback (lines 17–18); form reset before failure (line 19). |

## Prioritized findings

Severity follows the skill's local scale. There is no basis for a percentage design score or claimed revenue/efficiency gains.

### UX-01 — High: settings cannot be saved with a keyboard

**Location:** Settings, `Save changes`; source line 12. **Evidence:** E03, E12; directly observed.

Reproduce by editing Display name and tabbing through the email field. The next focus is `Delete workspace`; Save is absent from the focus order and has no button role. It is a `div` with only an `onclick` handler.

**Impact:** keyboard-only users cannot perform a central action. Relevant WCAG 2.2 criteria are 2.1.1 Keyboard and the missing programmatic role under 4.1.2 Name, Role, Value.

**Recommendation and acceptance:** use a correctly named native submit button. After input, Save and Retry must be operable through Tab/Enter/Space, with accessible error feedback. This does not require redesigning the entire page.

### UX-02 — High: a save failure destroys the draft

**Location:** Settings, both fields and error feedback; lines 12, 19. **Evidence:** E04; observed and confirmed in the handler.

Change both values and activate Save. The application reports a server failure but resets the inputs first. “Try again” therefore cannot resend the same changes. Even an obviously invalid email reaches this outcome; the direct click path bypasses native form validation.

**Impact:** entered work is lost, obscuring the cause and recovery path. This loss is demonstrated; whether an empty field should be allowed is not a documented product rule.

**Basis:** recovery and truthful save states from the workflow/business-administration modules. Preserving the draft is a contextual UX recommendation here. No blanket WCAG violation is claimed merely because client-side validation is absent.

**Recommendation and acceptance:** preserve values on failure, separate field validation from transport errors, and retry the same draft. `Casey Updated` and a valid changed email should remain after the simulated server failure. Invalid email needs clear correction guidance; retry must not clear the form.

### UX-03 — High: the deletion dialog lacks a reliable modal/focus contract

**Location:** Settings → Delete workspace → overlay; line 15. **Evidence:** E05, E06.

Focus remains on the background when opening. Escape does nothing; Shift+Tab from Close reaches the background. The accessibility tree reports a generic container. After Cancel or ×, focus does not return to the trigger.

**Impact:** keyboard and assistive-technology users cannot reliably follow the context and scope of a consequential action. Existing explanatory text and a working Cancel action are useful but do not complete the interaction model.

**Basis:** the modal interaction pattern is informative guidance. Missing role/name information also concerns SC 4.1.2. Not every interaction-pattern deviation, such as Escape considered alone, is automatically a separate WCAG violation.

**Recommendation and acceptance:** use appropriate native dialog behavior or a fully implemented modal component: accessible name, suitable initial focus, inactive background, contained focus order, Escape/Cancel, and return to the trigger. Recheck all three exits with pointer and keyboard. No actual deletion occurred or is claimed.

### UX-04 — High, strongly supported by source: fixed width prevents an adaptive shell

**Location:** the shell on all three pages, including local components and drilldowns; line 7. **Evidence:** E12; **no executed 320px runtime test**.

The shell is always 1200 CSS pixels wide, with a fixed 220px navigation and no adaptive rules. At a 320px viewport, its structure extends 880px beyond the visible width. Forms and navigation do not require inherently two-dimensional presentation.

**Impact:** important content will likely require horizontal movement in narrow views. Desktop screenshots do not establish tablet/phone suitability.

**Basis:** WCAG 1.4.10 Reflow, including exceptions. A possible exception for a particular table would not exempt the whole fixed shell.

**Recommendation and acceptance:** specify a fluid main area and suitable compact navigation. Actually operate all three pages, every expanded level and the dialog at 320 CSS pixels and appropriate medium/wide sizes. Use local table scrolling only where the task justifies it. The dialog can flex-shrink; `width:450px` alone does **not** establish a separate 498px minimum-width defect.

### UX-05 — Medium: the chart exaggerates a two-percentage-point change

**Location:** Overview → Completion rate; line 11. **Evidence:** E01, E10, E12.

Labels are 98%, 99%, 100%, but bar widths are 10, 105, 220. The final bar is 22 times the first's length. Equal value increments also produce unequal length increments of 95 and 115px; a shared linear scale cannot explain them. “Increased dramatically” reinforces the impression without documented domain justification. “Current month” also does not clearly match three monthly values without a year.

**Impact:** the graphic can suggest substantially greater quantitative change than the numbers support.

**Basis:** numerical consistency, the data-visualization module,.

**Recommendation and acceptance:** use a common, understandable bar scale or an appropriate dot/line representation with an explicit range. Express the change as +2 percentage points, identify the period and justify evaluative language. Text values were present in the checked accessibility tree; the chart is not claimed to be wholly invisible to screen readers. Its structure and meaning still require a real screen-reader check.

### UX-06 — Medium: secondary text has insufficient contrast

**Location:** header on all three pages; Overview “Status for the current month”; lines 7, 9, 11. **Evidence:** E10, E11.

The two normal-text/background pairs reach only 1.866:1 and 1.725:1. These uses are neither inactive controls nor logos nor incidental text inside images.

**Basis:** WCAG 1.4.3 Contrast Minimum, requiring 4.5:1 for normal text. This finding concerns the specified text usages, not every gray line.

**Recommendation and acceptance:** adjust secondary text to at least 4.5:1 on both actual backgrounds and inspect every header usage. Primary text and white Save text on blue passed the calculated static color-pair checks; this is not a complete contrast pass for all states.

### UX-07 — Medium: “Changes saved” claims persistence that does not occur

**Location:** Developers → Scope/Save; line 13. **Evidence:** E07.

Select `Read only`, activate Save, then reload: the display returns to `Full workspace access`. The handler only changes feedback text. This is a demonstrated prototype inconsistency, **not** evidence of a real permission change or security vulnerability.

**Impact:** someone may believe they restricted access. Even a demonstration should label simulated outcomes clearly.

**Recommendation and acceptance:** explain the simulation or implement a defined persistent test state. In a future real product, report success only after confirmed saving and distinguish saved from effective permissions. Reloaded state must match the promised contract. Backend enforcement requires separately authorized evidence.

### UX-08 — Medium: webhook details remain in a contradictory loading state

**Location:** Developers → Webhooks → View delivery details; line 13. **Evidence:** E08 and the full handler source.

Despite “No deliveries yet,” the detail action opens “Delivery attempts / Loading…”. There is no request or transition to results, empty state or failure. Waiting longer would not resolve this source-defined dead end.

**Impact:** users cannot tell whether data exists, processing is underway or any action would help.

**Recommendation and acceptance:** show an honest completed empty state for this fixture. If a real request is intended, define loading, empty, populated, failure and appropriate retry states. Do not present permanent loading without ongoing work. No real webhook deliveries or provider retry rules were tested.

### UX-09 — Medium: save feedback lacks programmatic status semantics

**Location:** Settings `#save-status`, Developers `#key-status`; lines 12–13, 19. **Evidence:** E04, E07 and source.

Both messages are written into ordinary empty paragraphs without live-region, status or alert semantics. Success/failure appears visually without deliberate focus movement. Text nodes being readable in the tree does not demonstrate automatic announcements.

**Basis:** WCAG 4.1.3 Status Messages. **Confidence:** the missing programmatic mechanism is demonstrated in source; actual spoken output was not heard.

**Recommendation and acceptance:** implement an appropriate preexisting feedback region with suitable urgency. Announce outcomes clearly once; retry should neither remain silent nor interrupt repeatedly without reason. Verify the intended browser/screen-reader combinations afterward.

### UX-10 — Low: unknown direct links leave the main content empty

**Location:** hash navigation; lines 17–18. **Evidence:** E09.

Opening `#missing` leaves the main area blank. Navigation and header remain, so escape is not completely blocked. An invalid, outdated or mistyped link nevertheless lacks explanation and a defined fallback.

**Recommendation and acceptance:** provide a clear not-found state or appropriate default route. Check direct links to every known page, unknown hashes, reload and browser Back/Forward. Back/Forward worked between the valid pages tested.

## Additional contract questions and withheld claims

- Settings mixes apparently personal fields with workspace deletion. “Workspace actions” already separates one section. Whether Display name and Notification email are global, workspace-specific or shared is undocumented. Establish ownership and effects before reorganizing; do not invent an organization model.
- “All members can manage workspace keys” is explicit fixture content. There is no basis to impose owner-only access as a universal standard. Actual deletion/key-management permissions need a product contract and appropriate backend evidence.
- `demo_value_not_a_live_secret` is clearly synthetic. It is not a demonstrated secret leak. Masking alone would not establish authorization in a real product either.
- CSS declares the Close button as 14 × 14px. It merits usability review but is **not an automatically demonstrated WCAG 2.5.8 failure**: spacing/equivalent-target exceptions need actual geometry checks. Cancel provides another dismissal path. 44 × 44 CSS pixels is not a blanket AA requirement.
- Project drilldowns lack programmatically exposed expanded states; closing details moves focus to HTML content. Refinement should define disclosure and focus behavior, including return to Project Linden. Untested screen-reader unusability is not asserted.
- No “more modern” font, palette, glass effect or animation is necessary purely as a matter of taste. Existing native labels, table headers, main headings and clear deletion-consequence wording are useful foundations.

## Inventory and coverage matrix

`pass` applies only to the named executed check; `fail` means investigated with a finding. Outstanding responsive, assistive-technology and other cross-cutting checks appear separately below. Visiting an element does not make it pass overall.

| Entity / concrete usage | State or transition checked | Result and evidence |
|---|---|---|
| Shell: header, three-link main navigation, main area on Overview/Settings/Developers | Content, labels, route changes, grouping | **fail** contrast/adaptive source; links work (E01, E09–E12) |
| Overview: h1 and secondary period text | Initial | **fail** contrast and unclear period (E01, E11) |
| Completion widget: h2, SVG with three labels/bars, conclusion | Every provided value | **fail** scale (E01, E10, E12) |
| Teams widget: h2, table, both headers, only row, owner, Operations button | Initial, opening | **pass** content/first transition; other accessibility dimensions unresolved (E01–E02) |
| Operations drilldown: h3, Project Linden button | Open, open project | **pass** defined opening actions; disclosure semantics need improvement (E02) |
| Project Linden detail: h4, task status, Close details button | Open/close | **fail** focus after closing; content reachable (E02) |
| Settings: h1, both label/input usages | Initial values, editing, invalid email, Tab order | **pass** labels/input; validation contract incomplete (E03–E04) |
| Settings: Save div and feedback | Click, failure, retry, keyboard attempt | **fail** UX-01/02/09 (E03–E04) |
| Settings: Workspace actions h2, Delete workspace button | Open | **pass** trigger and stated scope; modal contract fails (E05) |
| Deletion overlay: container, title, explanation | Open, Escape, focus order | **fail** UX-03 (E05) |
| Dialog: × | Close | **pass** visible dismissal; **fail** focus return (E06) |
| Dialog: Cancel | Cancel | **pass** visible dismissal; **fail** focus return (E06) |
| Dialog: Delete everything | Simulated confirmation | **pass** stated simulation result (E06) |
| Browser alert: explanation, OK | Acknowledge | **pass** local confirmation (E06) |
| Developers: h1, API credentials h2, policy text, key label, readonly field | Initial | **pass** content/accessible field name; no real secret/backend testing (E07) |
| Developers: scope label and native select | Both defined options | **pass** selection operable (E07) |
| Developers: Save and feedback | Save in both scopes, reload after Read only | **fail** UX-07/09 (E07) |
| Webhooks: h2 and empty-state text | Empty | **fail** inconsistency with subsequent view (E08) |
| Webhooks: View delivery details button, h3, loading text | Open, navigate away/return | **fail** UX-08 (E08–E09) |
| Additional router case | Unknown hash | **fail** UX-10 (E09) |

**Visited counts:** 3/3 main pages; 2/2 nested project drilldowns; 1/1 webhook drilldown; 1/1 application overlay with 3/3 defined exits; 1/1 resulting native alert. Both scope options and both Save handlers were activated. Every explicit application handler in `index.html` was exercised; repeated loops were not counted as new implementation branches. A defective path counts as investigated coverage, never as passing product quality.

## What remains before a complete-audit claim

| Outstanding dimension | Status and next check |
|---|---|
| Responsive integration of every usage above | **blocked** by the locked Mac; check 320 CSS pixels, tablet width, wide/short windows, expanded states and dialog. Fixed shell is already a source finding. |
| Zoom and text adjustment | **not-tested** at 200%/target reflow size; verify actual zoom, text-spacing overrides and long input. 110% is not a substitute. |
| Complete keyboard operation | **Partially tested**; Save/modal barriers are established, but not every action, applicable key and local navigation has been fully repeated. |
| Screen reader | **not-tested**; accessibility trees are not listening tests. Check dialog opening/closing, chart meaning, fields, feedback and drilldowns with an actual screen reader. |
| Pointer targets/focus appearance | **not-tested** as a full geometric/visual matrix; especially × with applicable exceptions and every focused usage. |
| Touch and on-screen keyboard | **not-tested**; no actual tablet/phone interaction. |
| Full WCAG 2.2 A/AA criteria register | **not-tested** as a complete review; reconcile every applicable criterion with evidence or justified nonapplicability. Findings are not certification. |
| Forced colors and further content lengths | **not-tested**; examine controls under these conditions. No second theme/locale implementation was found. |
| Roles, tenants, authentication, real APIs/webhooks and offline server cases | **not-applicable to this isolated fixture**: no implementation or real counterpart exists. A future production claim must explicitly bring these areas into scope. |
| User comprehension and task improvement | **not-tested**; representative users would need to understand periods, scope and error recovery. No demonstrated improvement factor. |
| Other browsers/performance | **not-tested**; no cross-browser, device, load or field-performance pass. No measured performance promises. |

**Recommended sequence:** address save accessibility and draft preservation first, then the modal contract and adaptive shell; afterward, address chart correctness, contrast, truthful save/loading states and status announcements. Implementation would require clarifying the affected concept states and obtaining approval where applicable. This task remains an audit with no application changes. Outstanding applicable checks need evidence before a full audit can be completed; simply relabeling this review as “complete” would not be justified.
