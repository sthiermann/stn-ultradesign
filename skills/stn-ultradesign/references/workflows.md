# Workflows: complete journeys, observable states, recoverable actions

Load when auditing or designing navigation, forms, onboarding, wizards, settings, dialogs, search, uploads, notifications, checkout, collaboration or AI-assisted tasks. Access date: 2026-09-16. Source paragraphs describe published guidance; the decision rules, contracts and test scenarios below are this skill's operational synthesis. Pattern-library conventions are evidence to evaluate in context, not universal laws.

## 1. Start with a workflow inventory

Create one record per meaningful user outcome, not per screen. Cover the primary actor, occasional actor, support/admin actor and any collaborator who receives the result. Establish where users enter from: navigation, search, notification, invitation, saved link, browser history, another device or an external identity provider.

For each workflow record the desired outcome, existing friction, frequency, failure cost, prerequisites, data touched and actual authorization scope. Locate every route and component involved. Inspect both the normal flow and meaningful variants; use `not applicable` with a reason rather than manufacturing features a product does not need.

Build the inventory around families: discover, compare, create, edit, approve, share, transfer, pay, import/export, configure, authenticate, recover, leave and delete. Specialized products add their own families, such as appointment rescheduling, access provisioning or incident response. A workflow inventory is complete only relative to a declared product boundary and evidence; never promise that a generic list covers all possible workflows worldwide.

## 2. Write the concept contract before code

In concept-first mode, make each changed workflow concrete enough to approve before production implementation. For audit-only work, document existing behavior and findings; for already approved or explicitly direct implementation, preserve that authorization. Include representative screens, the transition logic, actual copy, responsive behavior and consequential edge states. Refine the concept with the user, freeze the approved revision and use its identifiers in implementation and verification.

| Contract field | Required content |
|---|---|
| Outcome and actor | What the actor achieves and in which account, workspace or tenant |
| Entry and preconditions | Entry links, prerequisites, permissions and existing draft |
| State | Visible content, enabled actions, retained input, loading and error treatment |
| Transition | Trigger, guard, next state and focus destination |
| Validation | Local and server checks, timing, message and correction route |
| Exit | Back, cancel, close, leave, timeout and resume behavior |
| Side effect | What changes externally, when it commits and how it can be undone |
| Completion | Evidence of success, reference, next action and resulting permissions |
| Adaptation | Desktop/tablet/mobile arrangement, keyboard/touch and assistive-technology behavior |
| Acceptance | A reproducible scenario proving the promised behavior |

Treat unresolved contract decisions as named gaps. Provide a proposed default and its reason. Do not silently substitute a different workflow while implementing an approved concept. If testing reveals a material flaw, show the conflict and a revised concept before adopting it.

## 3. Specify states as behavior, not illustrations

For each data-bound surface evaluate initial, loading, ready, genuinely empty, no search matches, no access, stale, offline, failed and partially available states. For edits add unchanged, dirty, validating, saving, saved, rejected, conflicted and abandoned. For operations add queued, running, cancel requested, cancelled, completed, failed and outcome unknown where applicable.

Do not implement every label as a separate screen. Decide which states need a distinct message or action. “No records” must not mask a failed fetch; “Saved” must not mean only that a local request started. Define what survives navigation, refresh, sign-out and device changes. Use explicit event and result names in the contract so design and engineering agree on the meaning.

For every recovery action answer: what will retry repeat, can it duplicate a side effect, will it overwrite work, and how will the user know the outcome? These questions are especially important for money, invitations, publishing and bulk edits.

## 4. Choose the appropriate task structure

GOV.UK advises starting question journeys with one question per page and preserving browser-back behavior. That guidance belongs to its service context. [Question pages](https://design-system.service.gov.uk/patterns/question-pages/) USWDS distinguishes a linear step indicator from nonlinear or conditionally changing forms. [Step indicator](https://designsystem.digital.gov/components/step-indicator/)

Use a single page when users need to compare fields, edit quickly or understand a compact whole. Use a wizard when dependencies, risk or unfamiliarity justify guided sequencing. Use a task list when independently completable sections can be resumed or delegated. Use an editor when iteration and spatial context dominate. A dashboard is useful only when users can explain the decision each element supports.

Validate the choice with a representative novice and frequent-user scenario. Count unnecessary decisions, repeated entry and lost context; do not optimize raw click count at the expense of comprehension. A shorter flow is an experiment to evaluate, not proof of better UX.

## 5. Navigation and orientation

Give each route an intelligible title and a stable location in the product. Distinguish global navigation, workspace navigation, page tabs, local filters and contextual actions. A change to a local filter should not unexpectedly reset the whole workspace. Explain the object currently being edited when the same component appears in many contexts.

Preserve deep links to meaningful states where product and privacy constraints permit. Define what happens if the object was deleted, access was revoked or the link opens in a different tenant. Preserve browser history sensibly; opening an item and going back should restore the user's list context where feasible.

On small screens decide which navigation persists, moves into a disclosure or changes form. Keep the destination model consistent across devices. Test direct arrival into a nested page with no prior context and return from an external step. Verify that a selected item is distinguishable from keyboard focus.

## 6. Forms and input design

Ask only for data with a known purpose. For each field identify the data type, accepted formats, sensitivity, optionality, prerequisite and downstream use. Choose controls according to the real domain: an identifier containing digits is not automatically a mathematical number. Show a persistent label, relevant example and constraint before submission when that constraint cannot reasonably be inferred.

Treat names, addresses, phone numbers, date formats and identifiers as international data. Record which locales the product actually supports; do not invent a globally valid regex. Where normalization is appropriate, show the interpreted result and preserve the meaningful original. Verify browser autofill, input method composition, paste and mobile keyboards.

USWDS's complex-form guidance considers trust, progression and retaining submitted information. [Complete a complex form](https://designsystem.digital.gov/patterns/complete-a-complex-form/) Apply this by stating preparation needs, data use and what users can save. Test with missing, unusually long, partially known and valid-but-uncommon answers. Make dependency changes explicit when they invalidate later answers.

## 7. Validation and correction

GOV.UK recommends an error summary plus field-level messages for validation failures and distinguishes user-correctable input errors from service problems. [Recover from validation errors](https://design-system.service.gov.uk/patterns/validation/)

Decide when each check becomes useful: before submission for obvious constraints, after meaningful interaction for field feedback, and after server response for authoritative business rules. Avoid interrupting unfinished input. Preserve valid non-sensitive answers after rejection. Make error copy state the issue and an achievable correction, with a support route when the user cannot fix it.

Test multiple errors, a changed server rule, expired availability and a field removed by conditional logic. Ensure the error refers to the current value rather than a stale request. Keep validation errors discoverable without relying on red, a toast or a disappearing tooltip. A disabled submit button needs an understandable reason; consider allowing submission to expose actionable validation instead.

Completion means the user can find every remaining issue, correct it and succeed without restarting the workflow.

## 8. Wizards, review and long-running applications

GOV.UK's task-list pattern supports grouped work; its check-answers pattern offers review before final submission. [Complete multiple tasks](https://design-system.service.gov.uk/patterns/complete-multiple-tasks/), [Check answers](https://design-system.service.gov.uk/patterns/check-answers/) USWDS recommends manageable question groups, save/resume and explaining impacts when an earlier answer changes later work. [Progress easily](https://designsystem.digital.gov/patterns/complete-a-complex-form/progress-easily/)

Specify step entry, completion and editability. Show progress truthfully: avoid a fixed total when branches can change it. Preserve answers going back. A “Change” action from review should return to review with dependencies revalidated. Distinguish draft complete from submitted; a green step must not imply a committed transaction.

For collaboration, define who can complete each section and whose work is currently visible. Include missing prerequisites, handoff, submitted/read-only, returned-for-correction and withdrawn states. On resume, explain what changed since the draft. Test interruption immediately before and after final submission, including browser refresh and a duplicated request.

## 9. Onboarding and first use

GOV.UK recommends requiring an account only when the service needs it and allowing useful access before account creation where possible. [Create accounts](https://design-system.service.gov.uk/patterns/create-accounts/)

Identify the first meaningful user outcome. Make required setup distinguishable from optional personalization, product education and commercial upsell. Ask for access or information when its purpose becomes understandable. Let users defer nonessential setup and find it later. Avoid tours that block the task while explaining controls the user has not encountered.

Design first use around authentic user data or clearly labeled samples. Show whether an example can be edited, copied or discarded. Include returning users, invited users, migrated accounts and experienced users joining a second workspace. A completion checklist should correspond to actual usefulness, not merely encourage engagement.

Measure first successful task, time to useful outcome, abandonment and avoidable support requests. An onboarding redesign passes only if it improves the chosen outcomes without hiding privacy, price or account consequences.

## 10. Settings and preferences

Organize settings by a user's intent and scope: personal preferences, account identity, organization policy, workspace defaults and individual-object overrides. Make inheritance explicit. For each setting state what changes, who is affected, when it takes effect and whether permission is required.

Choose one saving model per coherent group. Immediate settings need clear pending, success and failed-save behavior; staged edits need clear Save, Cancel and unsaved-change handling. A switch that starts a costly, delayed or multi-step operation may need a different control. Preview cosmetic choices when possible and make recovery to a usable configuration easy.

Test search or discoverability for rarely used settings, a locked organization policy, permission loss during editing and changing a dependent setting. Keep destructive account actions findable and distinct from ordinary preferences. Confirm that reset affects exactly the announced scope. A UI reset must not imply deletion of stored personal data unless that is what the service actually does.

## 11. Permissions and contextual requests

Android's permission guidance asks for permission in the context of the requested feature and calls for graceful degradation after denial or revocation. [Request runtime permissions](https://developer.android.com/training/permissions/requesting)

Apply a capability-specific contract: what resource, for what task, for how long, and what alternative exists? Separate the app's explanation from the operating system or browser grant dialog. Respect cancellation. On return, inspect the actual permission state; do not infer success from having opened a dialog.

Cover unavailable hardware, restricted environments, policy denial, temporary grants and permission later revoked. Prefer narrower access where the platform and task support it. A location-denied state might offer manual location entry; a camera-denied state might offer file selection. Keep explanation and recovery within the affected feature rather than blocking unrelated work. Authentication and product authorization are separate concerns; use [identity-permissions.md](identity-permissions.md).

## 12. Dialogs and interruptions

Use a modal when an immediate scoped decision must be completed or dismissed before returning. Use an inline region, side panel or page when users need surrounding context or substantial work. Write the outcome into action labels. Distinguish Cancel from a negative decision and from closing an informational overlay.

Specify initial focus, keyboard handling, background behavior, close control, unsaved data, nested popups and focus return in the contract; use [accessibility.md](accessibility.md) for APG-backed behavior. Test a long translation and the virtual keyboard. A dialog that fits desktop can still conceal its action or error on a phone.

Review interruption frequency over the whole task. Several individually defensible alerts may together create a hostile flow. A confirmation should expose decision-relevant information rather than ask a reflexive generic question. Preserve a comprehensible route when the original trigger disappears or the underlying object changes.

## 13. Destructive and consequential actions

WCAG AA SC 3.3.4 requires at least one of reversal, checking with correction, or confirmation for the specified legal, financial and stored-data submissions; it is not a rule that every action needs a modal. [Error Prevention](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html)

Classify consequences by reversibility, affected people, data volume, external commitment and recovery cost. Prefer undo when recovery is real and reliable. For irreversible or widely consequential actions, show exact objects, scope and consequences at the decision point. Typed confirmation is a product-specific option for exceptional risk, not a general standard.

Test individual and bulk deletion, cancel, failure, partial success and an object changing during confirmation. Clarify retention, restore window and whether collaborators lose access. An Undo button must actually undo the committed effect or clearly explain its narrower operation. Do not label a local dismissal as reversal of a sent invitation or processed payment.

## 14. Asynchronous work, slow networks and offline mode

Tie feedback to real milestones: accepted request, queued job, processing, committed result and available output. Use measurable progress only when the system can support it. For unknown duration explain the phase or next action. Allow departure when safe and provide a way to retrieve the result.

Distinguish saved locally, waiting to sync and saved remotely. Show stale information when still useful, with enough context to interpret it. Define the policy for queued writes: order, cancellation, duplicate prevention, expiry and conflict. Do not promise offline editing just because a page is cached.

Simulate a failed request, a timeout after server acceptance, reconnect, a page reload during upload and a second tab editing the same record. Check that retry cannot silently multiply purchases or messages. Cancellation may require a “cancelling” state before completion; do not equate closing a dialog with terminating server work.

## 15. Concurrent edits and collaboration

Identify whether the workflow uses exclusive editing, last-write-wins, automatic merge or explicit conflict resolution. Explain the user-visible consequences. Show collaborator presence only when it helps; avoid claiming that a presence indicator guarantees current data.

When a save conflicts, retain the user's draft, identify what changed and offer an appropriate merge, reload or copy route. Make the conflict understandable in the user's vocabulary. Record authorship and change history when necessary to reconcile shared work.

Test two users editing the same field, independent fields, deleted objects, reassigned ownership and lost authorization. Evaluate tenant switching and browser tabs, where stale context can cause wrong-workspace actions. The concept contract must specify the authoritative outcome, not simply a decorative conflict banner. If backend behavior is unknown, mark this dependency and refrain from claiming complete recovery.

## 16. Search, filtering, sorting and selection

Define what is searchable, the current scope, query interpretation and result ordering. Separate suggestions from committed results. Preserve filters and sorting when users inspect a result and return. A no-results state should expose removable constraints or a revised query without erasing the user's input.

For dynamic filtering, prevent older responses from replacing newer ones. Make count updates perceivable without excessive announcements. For large collections decide between pagination, progressive loading and virtualization according to navigation, accessibility and retrieval needs. Verify deep links and browser history if the state is represented in the URL.

Define whether selection applies to visible rows, the current page, loaded items or every matching item. Explain what happens when filters change. Bulk actions show affected counts and exceptions, and must handle partial permissions and partial failure. Test zero, one, many, duplicate-named and inaccessible results, plus clear/reset behavior.

## 17. Upload, import, export and download

GOV.UK provides both file-picker and drag/drop paths and recommends reusing a prior upload within a journey when appropriate. [File upload](https://design-system.service.gov.uk/components/file-upload/) OWASP treats type checks, size limits, storage and scanning as server-side security considerations; UI file restrictions alone do not establish safety. [File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)

Before selection explain allowed formats, limits and purpose. During processing distinguish transferred from validated or imported. Provide per-file status, removable queued items and clear retry behavior. For imports show mapping, preview, duplicates and a row-level error report before committing consequential changes.

For exports identify scope, filters, format, locale and sensitive fields. Explain whether the output is a current snapshot. Keep a durable retrieval route for background generation. Test corrupt files, duplicates, unsupported encoding, extreme names, expired download links and a job completed after the user navigated away. Do not display success while processing still may reject the file.

## 18. Notifications and empty states

Carbon distinguishes notification intent from delivery type and recommends relevant, timely information with disruption appropriate to the situation. Its pattern guidance includes draft areas; do not mistake every example for a shipped component. [Notifications](https://carbondesignsystem.com/patterns/notification-pattern/)

Use inline feedback for a local issue, a persistent banner for an ongoing broad condition and a transient message for low-risk acknowledgement. Important recovery instructions need a durable home. Group repeated events and make notification preferences understandable by type and channel.

Distinguish first-use empty, completed work, filtered-empty, deleted content, missing permission and service failure. Give the next useful action and enough context to understand why nothing appears. Do not add a promotional illustration to obscure a missing-data error. Test several simultaneous notifications and a screen-reader journey. Verify that dismissing a message does not falsely resolve the underlying condition.

## 19. Checkout, subscription and cancellation

Specify the complete financial journey: offer, eligibility, total, currency, tax and fees where applicable, billing cadence, payment, authentication challenge, confirmation, receipt and later management. The design contract must use actual product terms, not attractive placeholder claims.

Handle changed price, unavailable stock, declined payment, pending authorization, duplicate submission and unknown outcome. A timeout must lead to a status check or safe retry, not a claim that nothing happened. Make the final action communicate the commitment and provide a durable reference after success.

Design plan changes, refunds, cancellation, renewal and data export as real workflows. Clearly state effective dates and retained access. Check obligations with qualified owners for the relevant market; no single UI pattern establishes worldwide consumer-law compliance. Test that a user can understand both joining and leaving with comparable clarity. Measure completion alongside accidental purchase, disputes and cancellation support burden.

## 20. AI-assisted and agentic workflows

Microsoft's HAX guidance covers initial expectations, ongoing interaction, errors and adaptation over time. [Human-AI Interaction Guidelines](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/) Its explanation guidance cautions that explanations can increase trust even when that trust is unwarranted. [Guideline 11](https://www.microsoft.com/en-us/haxtoolkit/guideline/make-clear-why-the-system-did-what-it-did/)

Specify what the AI proposes, what it can execute, and which actions require an actual user decision. Show inspectable inputs, relevant evidence, editable output and honest limits. A generated plan, a queued action and a completed external action are distinct states. Never use a confidence decoration as fabricated evidence.

Design stop, revise, retry, resume, reject, compare and revert where meaningful. Keep a user's manual changes when regenerating. For multi-step agents show consequential progress and partial results without flooding the interface. Test wrong output, missing evidence, ambiguous intent, tool failure, permission change and interrupted execution. Judge success by reliable task completion and recoverability, not by how human the animation appears.

## 21. Completion, help and service recovery

GOV.UK confirmation guidance covers evidence of completion and what follows. [Confirmation pages](https://design-system.service.gov.uk/patterns/confirmation-pages/)

Make completion state what actually happened, what remains pending, who acts next, and how to return. Include a reference or record when users will need proof or follow-up. Avoid implying approval when an application was only received. Keep the next action specific to the user rather than automatically sending everyone to a dashboard.

Provide help at the point of confusion and a support route for cases software cannot resolve. Preserve a safe diagnostic reference without exposing secrets. For outages, distinguish retryable incidents from invalid input and state whether existing work is safe. Test a user returning days later, with no memory of the original workflow.

## 22. Verify the workflow as one system

For each high-priority workflow run: normal completion; user mistake and correction; back/cancel; interruption/resume; slow or failed service; role/permission boundary; narrow viewport; keyboard and assistive-technology route. Add concurrency and external-side-effect scenarios when relevant. Select combinatorial tests based on risk; record untested combinations explicitly.

Attach observations to contract identifiers. Evidence includes exact state, trigger, expected result, actual result and reproducible artifact. Separate sourced requirements, existing product constraints and design hypotheses. Close a finding only after the relevant outcome works and nearby behavior remains intact.

Track completion rate, critical error rate, recoverability, time to successful outcome and user confidence appropriate to the task. Compare before/after with the same task and conditions. State sample limits. A visually compelling concept is ready for approval when its material behaviors are reviewable; an implementation is complete when it faithfully satisfies that approved concept and the verified workflow contract.
