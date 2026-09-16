# Accessibility: interaction contracts and evidence

Load for every frontend audit, concept, component change, or responsive redesign. Source access date: 2026-09-16. **Standard** paragraphs summarize external requirements; **Audit procedure** and **Skill recommendation** paragraphs prescribe this skill's own method. Read the actual criterion, including definitions and exceptions, before declaring a failure.

## 1. Establish the target and scope

**Standard.** WCAG 2.2 is a W3C Recommendation; the current published document is dated 12 December 2024. AA conformance includes all applicable A and AA criteria and concerns full pages and complete processes. Understanding documents and techniques explain implementation but are informative. Conformance does not cover every disability-related need. [WCAG 2.2](https://www.w3.org/TR/WCAG22/)

**Audit procedure.** Record the requested conformance version and level, product surfaces, third-party steps, browser/assistive-technology combinations, and exclusions. Default the design target to WCAG 2.2 AA when none is specified; identify this as a project recommendation, not a statement of jurisdictional law. A legal compliance assessment requires the actual applicable jurisdiction, procurement contract, product type, and standard version.

Build a criterion-level ledger for the complete applicable A/AA set. This document emphasizes frequent failures; it is not a replacement for that ledger. Record `pass / fail / not applicable / not tested`, evidence, tested state, method, and limitation. A representative sample can support a scoped audit; it cannot prove untested pages conform.

## 2. Make accessibility reviewable before implementation

**Skill recommendation.** Include accessibility in the approved concept contract: reading order, accessible labels, keyboard behavior, focus destination after each transition, status announcements, mobile reflow, and motion alternatives. Draw the error and empty states alongside the ideal state. When the proposed visual treatment cannot meet the target, resolve that issue during concept refinement.

After approval, implement those behaviors faithfully. If a constraint emerges, show the concrete conflict and revised option; record a change to the contract before substituting a different interaction. Decorative changes do not justify silently dropping semantic or keyboard behavior.

## 3. Semantic structure and controls

**Standard.** User interface controls must expose names, roles, relevant states and values, and their changes programmatically. [SC 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) When a control has a visible text label, its accessible name contains that text. [SC 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html)

**Guidance.** ARIA assigns semantics; it does not supply keyboard behavior. APG examples require testing with the intended browsers and assistive technologies. [APG Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)

**Audit procedure.** Inspect the rendered accessibility tree, not only JSX. Trace headings and landmarks through one complete task. Use native buttons for actions, links for navigation, explicit labels for inputs, and proper table structures for tabular data. Check icon buttons, repeated row actions, toggles, sorting, selection, mixed checkboxes, validation and loading states. Identify a delete button's target without creating an excessively verbose name. Distinguish a navigation list from an application menu. Inspect custom components where props, portals or wrappers can disconnect labels from controls.

## 4. Keyboard, focus and overlays

**Standard.** Keyboard access covers functionality except functions whose underlying input depends on a movement path. [SC 2.1.1](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) Visible keyboard focus is AA. [SC 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html) AA SC 2.4.11 prevents author-created content from entirely hiding the focused component; it does not require the whole component always to remain uncovered. [SC 2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) The quantitative Focus Appearance criterion is AAA. [SC 2.4.13](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html)

**Guidance.** Modal dialogs contain their tab sequence, receive focus on opening, support Escape, and return focus to the invoker or a logical successor. Initial focus depends on content and consequences; long structured content may warrant focusing a heading rather than a button. [APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)

**Audit procedure.** Complete the critical task using Tab, Shift+Tab, Enter, Space, Escape and widget-specific keys. Open and close every overlay type; then repeat under zoom and with a sticky footer. Verify that a removed row or closed dialog leaves focus somewhere meaningful. Recheck nested popovers, date pickers, toasts and mobile navigation. A modal must actually prevent background interaction. Measure focus contrast and inspect clipped rings. Prefer fully visible focus as the design target even when partial visibility technically meets the minimum.

## 5. Pointer targets and gestures

**Standard.** AA target size is 24×24 CSS pixels. Exceptions cover a precise spacing test, an equivalent conforming control on the same page, inline targets, unmodified user-agent controls, and essential or legally required presentation. For spacing, a 24-pixel-diameter circle centered on each undersized target's bounding box must not intersect another target or another undersized target's circle. [SC 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) The 44×44 CSS-pixel enhanced target criterion is AAA and has its own exceptions. [SC 2.5.5](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html)

**Standard.** Dragging needs a single-pointer alternative that does not drag, unless essential or unmodified user-agent behavior. Keyboard equivalence alone does not satisfy this requirement. [SC 2.5.7](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)

**Audit procedure.** Measure the actual hit area, not the icon. Check dense rows, close controls, adjacent destructive actions and touch-only usage. Keep larger comfortable targets where the context permits; identify platform-specific point or dp guidance separately from CSS pixels. For a sortable list, test both keyboard reordering and a tap-accessible move command. For sliders, verify an exact-value entry or another usable pointer operation. Preserve access when hover is unavailable.

## 6. Contrast and redundant meaning

**Standard.** Ordinary text requires 4.5:1 contrast at AA; large text requires 3:1, subject to incidental and logo exceptions. Large text means at least 18 pt regular or 14 pt bold, approximately 24 or 18.67 CSS px respectively. [SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) Essential control/state visuals and required graphical information generally need 3:1 against adjacent colors, with the criterion's exceptions. [SC 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) Meaning cannot depend on color alone. [SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)

**Audit procedure.** Test actual combinations in light, dark, selected, focused, error, disabled and loading states. Include text over images, gradients and translucent surfaces; a passing token pair may fail in the final composite. Separate inactive-control exceptions from a recommendation that disabled explanations remain readable. Give chart series, validation and status another cue such as a label, shape, pattern or icon. Do not turn every decorative border into a claimed 3:1 requirement. Evaluate forced-colors mode with actual controls and focus states.

## 7. Reflow, text adaptation and orientation

**Standard.** At AA, vertically scrolling content reflows at 320 CSS px width; horizontally scrolling content at 256 CSS px height, without lost functionality or two-direction scrolling. Parts whose meaning or use requires two-dimensional layout are excepted; a data table exception does not automatically exempt individual cells or the surrounding page. [SC 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) Text resizing to 200% must preserve content and functionality, with stated exceptions. [SC 1.4.4](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)

**Standard.** Test user overrides of line height 1.5, paragraph spacing 2, letter spacing 0.12, and word spacing 0.16 times font size together. These are resilience test values, not mandatory default typography. Script-specific exceptions apply. [SC 1.4.12](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) A single display orientation may be required only when essential. [SC 1.3.4](https://www.w3.org/WAI/WCAG22/Understanding/orientation.html)

**Audit procedure.** Run both zoom and narrow-viewport checks; they exercise different failure modes. Inspect dialogs, banners, toolbars, tables, tabs, sticky elements and the on-screen keyboard. Preserve meaningful labels when layouts condense. Keep a table's horizontal overflow local and discoverable. Test long translated strings and user-generated names. A screenshot without overflow is insufficient if controls were simply hidden.

## 8. Forms, authentication and feedback

**Standard.** Detected input errors identify the field and describe the problem in text. [SC 3.3.1](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html) Previously supplied information needed again in the same process must be populated or selectable, except when essential, security-related, or no longer valid; cross-session storage is not required. [SC 3.3.7](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html)

**Standard.** AA authentication limits cognitive-function tests unless an alternative, an assistance mechanism, object recognition, or recognition of user-provided non-text content applies. Password-manager and copy/paste support are relevant assistance mechanisms. The criterion concerns authentication of existing users. [SC 3.3.8](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html)

**Audit procedure.** Submit an empty form, an almost valid form and a server-rejected form. Verify understandable correction instructions, preserved non-sensitive answers, an error summary where useful, and an accessible return to invalid fields. Test paste and autofill in password and one-time-code fields. Verify every step including identity-provider redirects and recovery, not just the first sign-in screen. See [identity and permissions](identity-permissions.md) for the security boundary.

**Standard.** Applicable status messages must be programmatically determinable without moving focus. [SC 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) **Audit procedure.** Listen to saved, failed, filtered, uploaded and background-completed states. Avoid repeated announcements on every keystroke or every streamed token. Reserve interruptions for information needing immediate attention.

## 9. Time, hover and cognitive support

**Standard.** Time limits need the adjustments or exceptions specified by SC 2.2.1. [Timing Adjustable](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html) Qualifying automatically moving or updating content needs pause, stop or hide controls. [SC 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) Additional hover/focus content has dismissibility, hoverability and persistence requirements with exceptions. [SC 1.4.13](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html)

**Guidance.** WAI's cognitive accessibility document is supplemental guidance, not an extra WCAG conformance requirement. It covers comprehensible structure, memory demands, mistake recovery and help. [COGA Note](https://www.w3.org/TR/coga-usable/) Consistent Help is an A criterion with a narrower scope concerning repeated help mechanisms. [SC 3.2.6](https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html)

**Audit procedure.** Test a task after interruption. Make current location, completed work and next action recognizable. Respect reduced-motion preferences and verify that animation removal preserves feedback. Review timeout handling with the security owner rather than inventing a universally safe duration. Check that tooltips are supplementary and critical instructions remain available without hover. Include captions, alternatives and other applicable media criteria in the full ledger whenever the product contains media.

## 10. Evidence and completion

WAI explains that evaluation tools alone cannot determine accessibility; human judgment remains necessary. [Selecting evaluation tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/)

**Audit procedure.** Combine automated checks with keyboard inspection, zoom/spacing tests, accessibility-tree inspection, screen-reader journeys and user research where feasible. State the exact browser, OS, assistive technology and versions actually tested. If access is unavailable, mark that portion untested and provide a precise manual script. Do not translate a green scanner result into a conformance certificate.

Close an accessibility finding only when its original reproduction passes, adjacent states still work, the evidence is attached, and the approved interaction contract remains satisfied. An unresolved blocker on a critical workflow stays visible regardless of improvements to typography or an aggregate quality score.
