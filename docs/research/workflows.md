# Research: workflows, accessibility, identity and permissions

Research and access date: **September 16, 2026**. Sources are publicly accessible primary publications from their respective publishers. Operational modules are independently authored; no third-party skills, source code, templates or assets were incorporated. This report explains source authority and limits. Detailed review procedures appear in `skills/stn-ultradesign/references/`.

## Findings and necessary distinctions

A dependable design skill needs three separate layers: technical requirements with testable criteria, contextual published patterns, and reasoned product decisions. An audit must not collapse these into one label of “global standards.” A screen structure that helps an occasional public application process can obstruct a frequently used professional editor.

WCAG 2.2 is a W3C Recommendation; the current published document is dated December 12, 2024. Its success criteria and conformance rules differ from explanatory Understanding documents. AA includes applicable A and AA criteria. A checked component does not establish conformance of an entire process. [Source 1](https://www.w3.org/TR/WCAG22/)

Precise classification prevents common misstatements: 24×24 CSS pixels is the AA target-size baseline with defined exceptions; 44×44 is the separate AAA criterion. Larger touch targets can remain a useful product choice, but their rationale must be accurate. Focus Appearance is AAA; Focus Not Obscured Minimum is AA and prohibits complete obscuration by author-created content. [Source 2](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [Source 4](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html), [Source 5](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html)

WAI-ARIA Authoring Practices provide implementation guidance, not a guarantee that every example is immediately production-ready in every browser/assistive-technology combination. COGA supplements cognitive accessibility guidance rather than adding another WCAG conformance catalog. Verification must combine technical tests, real interaction and human judgment. [Source 11](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/), [Source 12](https://www.w3.org/TR/coga-usable/), [Source 13](https://www.w3.org/WAI/test-evaluate/tools/selecting/)

The final NIST SP 800-63B-4 from July 2025 is the relevant version for claims about that NIST authentication guidance; earlier drafts differ. It is not automatically a legal requirement for every application worldwide. Establish the applicable assurance and organizational policy before proposing changes. [Source 22](https://pages.nist.gov/800-63-4/sp800-63b.html)

## Implications for the skill

The following points are our synthesis:

1. **Define workflows as contracts.** Before implementation, establish actor, scope, entry, prerequisites, states, transitions, validation, Back/Cancel, interruption, resumption, side effects and success. Desktop, tablet, phone, keyboard and assistive technology belong to the same contract.
2. **Agree a reviewable concept first when redesign is requested.** Include realistic content and important failures. After refinement and approval, implement traceably. Material deviations need an explicit concept revision, not silent restyling. Audit-only work does not require implementation.
3. **Inventory the actual application.** Routes, roles, states and external steps define coverage. Justify nonapplicable patterns. An endless generic checklist does not replace full coverage of the concrete product.
4. **Distinguish meanings.** Empty, filtered empty, denied, load failure, stale and offline are different states. Locally saved, queued for synchronization and saved on the server are different promises.
5. **Check failure consequences.** Retries must not unintentionally duplicate payments, invitations or publication. Canceling, closing and terminating a server process differ. Unknown outcomes need an appropriate status check.
6. **State security boundaries.** Frontends explain permissions; hidden controls do not establish server authorization. Attractive passkey dialogs replace neither account recovery nor correct protocol implementation. Review legitimate sign-in/access UX without obtaining real passwords, tokens or sessions.
7. **Measure improvement.** Task completion, critical errors, recovery, time to useful outcomes and comprehension support comparison. Visual modernity and actual usability need separate evidence.

## Pattern selection and domain limits

GOV.UK recommends starting question processes with one question per page. This is not a universal requirement to split professional settings into many separate pages. USWDS describes its step indicator for linear sequences and distinguishes nonlinear or dynamically branching forms. The skill preserves these boundaries as decision rules. [Source 14](https://design-system.service.gov.uk/patterns/question-pages/), [Source 18](https://designsystem.digital.gov/components/step-indicator/)

FIDO documents passkey management, sign-in and fallback paths. Scope matters: consumer UX with synchronized passkeys is not automatically the policy of a regulated organization. [Source 23](https://www.passkeycentral.org/design-guidelines/required-patterns/), [Source 24](https://www.passkeycentral.org/design-guidelines/principles)

OWASP distinguishes authentication from authorization and recommends checking permissions on every request. Tenant changes also require consistent context across data, caches and background work. The design audit treats these as integration dependencies and explicitly leaves untested backend assurance unresolved. This is not an instruction to conduct penetration testing. [Source 26](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), [Source 29](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html)

Operational modules also cover upload/import/export, search/filter/bulk selection, notifications, destructive actions, purchase/subscription/cancellation, collaboration and AI workflows. Additional primary links appear beside the relevant claims. The skill claims neither uniform workflows across industries nor legal compliance from implementing a pattern alone.

## Required HTML, CSS and React knowledge

These learning objectives are our technical synthesis:

- **HTML:** native actions and navigation, visible labels, groups/legends, appropriate table structure, input purpose, file inputs, form submission and semantic status presentation.
- **CSS:** robust reflow, text enlargement and spacing overrides, actual hit areas, focus appearance, contrast, long content, accessibility modes and overlays without clipped actions.
- **React:** explicit states rather than contradictory Boolean flags, stable object identity, appropriate focus after transitions, synchronized form values, stale-response handling and recoverable error boundaries.
- **Integration:** truthful save/process states, appropriate retries, server validation, permission matrices, session expiry, tenant scope and clearly limited frontend conclusions.
- **Verification:** actual keyboard/screen-reader paths, narrow and enlarged layouts, error/return/interruption, role changes, concurrent editing and comparison with the approved concept revision.

## Verified core register: 30 primary sources

Every link was opened or its primary content retrieved during research on **2026-09-16**. Living documentation does not always provide a reliable publication date, so the access date is recorded.

| No. | Publisher and direct source | Role in the skill |
|---|---|---|
| 1 | [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Normative basis and conformance scope |
| 2 | [WAI — Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | Target size and exceptions |
| 3 | [WAI — Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) | Reflow and two-dimensional content |
| 4 | [WAI — Focus Not Obscured Minimum](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) | Visibility around overlays and sticky surfaces |
| 5 | [WAI — Focus Appearance](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html) | Distinguishing AAA from AA |
| 6 | [WAI — Accessible Authentication Minimum](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) | Cognitive barriers during sign-in |
| 7 | [WAI — Redundant Entry](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html) | Repeated entry in one process |
| 8 | [WAI — Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) | Resilience to user adjustments |
| 9 | [WAI — Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html) | Pointer alternatives in addition to keyboard operation |
| 10 | [APG — Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) | Focus, modality and return |
| 11 | [APG — Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/) | ARIA limits and interoperability |
| 12 | [W3C — COGA Content Usable](https://www.w3.org/TR/coga-usable/) | Supplemental cognitive-accessibility guidance |
| 13 | [WAI — Selecting Evaluation Tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/) | Limits of automated checks |
| 14 | [GOV.UK — Question Pages](https://design-system.service.gov.uk/patterns/question-pages/) | Contextual question workflows |
| 15 | [GOV.UK — Validation](https://design-system.service.gov.uk/patterns/validation/) | Finding and correcting errors |
| 16 | [GOV.UK — Check Answers](https://design-system.service.gov.uk/patterns/check-answers/) | Review before submission |
| 17 | [GOV.UK — Complete Multiple Tasks](https://design-system.service.gov.uk/patterns/complete-multiple-tasks/) | Nonlinear groups of tasks |
| 18 | [USWDS — Step Indicator](https://designsystem.digital.gov/components/step-indicator/) | Appropriate progress-indicator use |
| 19 | [USWDS — Progress Easily](https://designsystem.digital.gov/patterns/complete-a-complex-form/progress-easily/) | Complex forms and resumption |
| 20 | [GOV.UK — Confirmation Pages](https://design-system.service.gov.uk/patterns/confirmation-pages/) | Completion evidence and next steps |
| 21 | [GOV.UK — Create Accounts](https://design-system.service.gov.uk/patterns/create-accounts/) | Justifying account requirements |
| 22 | [NIST — SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) | Current identity/authentication guidance |
| 23 | [FIDO — Required Passkey Patterns](https://www.passkeycentral.org/design-guidelines/required-patterns/) | Sign-in and management together |
| 24 | [FIDO — Passkey Principles](https://www.passkeycentral.org/design-guidelines/principles) | Consumer UX and security boundaries |
| 25 | [OWASP — Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) | Account disclosure and sign-in errors |
| 26 | [OWASP — Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Permission enforcement |
| 27 | [OWASP — Forgot Password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) | Recovery as a separate process |
| 28 | [OWASP — Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | Expiry, logout and security events |
| 29 | [OWASP — Multi-Tenant Security](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html) | Tenant context and isolation |
| 30 | [Android — Runtime Permissions](https://developer.android.com/training/permissions/requesting) | Contextual permission requests and denial |

## Delivered modules and remaining limits

- `references/workflows.md`: decision rules and complete state/transition contracts across 22 review areas.
- `references/accessibility.md`: WCAG classifications and exceptions, plus original manual/automated procedures; the complete criteria register must still be inventoried.
- `references/identity-permissions.md`: identity lifecycle, permission UX, passkeys, recovery and tenant changes with an explicit backend boundary.

The assembled skill's effectiveness on a real application has not been established by this research. That requires a pilot with the same starting task before and after changes, recorded concept approval and traceable user outcomes. Research supports the method; it does not replace evidence of effectiveness.
