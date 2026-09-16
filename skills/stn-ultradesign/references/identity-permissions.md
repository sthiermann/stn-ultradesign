# Account and access workflows

Load for the user experience of sign-in, registration, passkeys, MFA, account recovery, sessions, permissions, roles, invitations, sharing, tenant switching or security settings. Access date: 2026-09-16. Review what people see, understand and can accomplish: layout, instructions, decisions, feedback and recovery. Do not obtain credentials, inspect secret stores or bypass an unavailable role. Use authorized test fixtures and user-controlled authentication under the boundary in `SKILL.md`. Standards below constrain the design; they do not turn a UX audit into a backend security assessment. Source paragraphs summarize published guidance; audit decisions are this skill's original method.

## 1. Establish the identity model

Distinguish identity proofing, authentication, authorization, organization membership, resource sharing, consent and device permissions in the concept contract. Record who controls each step: the application, identity provider, platform, organization administrator or support team. Identify the applicable assurance policy and who can approve changes to it.

Build an actor/action/resource/scope matrix before redesigning access controls. Include anonymous, invited, active, suspended and removed members where applicable. Add lifecycle changes: ownership transfer, expired invitation, lost authenticator and organization departure. State what happens to owned data and shared work.

Treat access as an explicit contract: hiding a button communicates availability; the server must enforce permissions on every relevant operation. Separate `UI verified`, `server evidence reviewed` and `security verification outstanding` in findings.

## 2. Design sign-in as a recoverable journey

Make account creation and existing-account access distinguishable. Offer methods supported by the actual service and organization policy. Show the current account where it helps prevent signing in under the wrong identity. Keep the intended destination through authentication when safe and supported; avoid dropping users into an unrelated home page after a forced sign-in.

For every method specify idle, submitting, challenged, cancelled, rejected, temporarily blocked, unavailable and complete states. Include back navigation, opening a second tab, switching account and resuming an interrupted task. An authentication loop is a workflow failure even if each individual screen appears correct.

Agree account-disclosure policy with the security owner, including visible messages and response differences. Pair necessary generic wording with useful next actions; avoid inventing account facts. Test that error copy never contradicts the backend outcome.

## 3. Password policy: verify the current standard

Derive password requirements from the product’s verified current authentication policy. Explain accepted length and disallowed values before submission, permit paste and password-manager use, and retain useful validation without exposing account facts. Do not invent complexity rules or scheduled password changes as design improvements; flag policy questions for the responsible owner.

Audit the actual configured service policy; do not silently relax an organization's security policy during a cosmetic redesign. Explain valid requirements before entry. Check that frontend and server rules agree, long inputs remain usable and rejected values receive an actionable reason. Verify reveal/hide controls without losing cursor position or input.

Apply the accessible-authentication checks in [accessibility.md](accessibility.md): password managers, paste and autofill need an end-to-end test. Do not manufacture a “strength percentage” that implies measured attack resistance. Keep credentials out of analytics, examples, screenshots and logs used in the audit.

## 4. Passkeys: a complete lifecycle

Map passkey setup, sign-in, device changes and fallback to the actual identity implementation. A polished enrollment screen is insufficient when a person cannot recover access on another device.

Use familiar language around the platform interaction and report the actual result when it returns. Explain creation in an account-related context. Make existing credentials visible and manageable without pretending the application controls every credential-manager action. Validate platform-specific assumptions against current supported environments.

Keep managing an existing sign-in method distinct from authenticating with it; account settings and sign-in need different entry and recovery contracts.

Test cancelled platform dialogs, no available passkey, another device, an unsupported environment, duplicate attempts and removal of a credential. Define fallback without claiming that all fallbacks provide equal assurance. Before removing the last usable method, make the remaining access route explicit. Distinguish removing a credential from this account and removing its copy from a credential provider. Do not promise universal synchronization or recovery across providers.

## 5. MFA and recovery

Plan enrollment, verification, backup methods, loss, replacement and organization enforcement together. A successful setup illustration is incomplete if losing a phone strands the user.

For one-time codes, test whole-code paste, autofill, leading zeroes, screen readers, resend, expiry and a newly requested code invalidating an old one. Prefer a single coherent input experience; visually segmented fields must not break those operations. Announce the remaining action without placing credentials in a live region unnecessarily. A countdown must reflect real server policy.

Treat recovery as its own journey: request, handoff, expiry, invalid or already-used link, new credentials, completion and session consequences. Verify these outcomes against the identity implementation rather than assuming a form submission completed recovery.

Test expired links, reused links, multiple requests, lost access to the delivery channel and a reset completed in another tab. Explain what changed and how to continue. Respect the approved support and identity-verification policy; a friendly recovery flow must not invent a bypass around account ownership checks.

## 6. Federation and enterprise sign-in

An identity-provider button represents a handoff with failure and return states, not a complete security implementation. Use the configured protocol and current implementation guidance for redirects, identity scope and token protections; record security dependencies outside the UX review separately.

Audit provider cancellation, organizational restrictions, unavailable provider, mismatched account, unverified address, account linking and duplicate membership. A user might belong to more than one organization with different requirements. Explain when they must use a managed identity without revealing unnecessary organization membership to an unauthenticated visitor.

Require a deliberate policy for linking identities; matching displayed email text alone is not sufficient evidence to approve a design assumption. Preserve task context around redirect and reauthentication. Mark protocol validation as a backend dependency when it was not reviewed. Avoid presenting a provider logo as a guarantee of the application's own security.

## 7. Sessions and sensitive changes

Confirm server-enforced expiry, logout and privilege-change behavior before specifying the visible session experience. A local screen reset does not prove the session ended.

Define the visible experience for inactivity expiry, absolute expiry, forced sign-out, sign-out from another device and a role change during use. Keep a recoverable draft where the data policy permits and say whether it was saved. Avoid claiming an action succeeded when reauthentication interrupted the commit.

For email changes, credential changes, security-method removal and access escalation, specify whether fresh verification is required and how the user returns to the task. Show relevant active sessions with a comprehensible description and a revocation route if the product supports them. Clarify whether logout affects one session, one device, the application or a federated session. Test browser-back behavior and cached protected content after sign-out.

## 8. Roles, permissions and sharing

Name roles by a user's responsibility and explain consequential capabilities with examples. Distinguish inherited permissions from direct grants and organization policy from object-specific exceptions. A disabled action can aid discoverability when the reason and request-access path are helpful; hiding can be appropriate when disclosure itself is sensitive. Choose through product and security requirements rather than a blanket rule.

| Scenario | Concept must define | Verification evidence |
|---|---|---|
| Invite collaborator | Recipient, organization, scope, role, expiry | Wrong account, expired invite, accept and revoke |
| Share resource | Named users versus broader audience | Resulting access and restricted-recipient view |
| Change role | Before/after abilities and dependencies | Allowed and denied operations after change |
| Transfer ownership | New owner, retained access, pending acceptance | Last-owner and failed-transfer paths |
| Remove member | Data ownership and access consequences | Revocation reflected across active views |

Use actual backend capabilities in the UI. Keep a material permissions change reviewable before commit. Logically related bulk operations may still yield per-resource failures; show the exact result rather than a misleading overall success message.

## 9. Tenant context and account switching

Treat a client-selected tenant or workspace as a context selector, not proof of authorization. Verify the UI’s scope and record server-side isolation dependencies for caches, files, sessions and background work.

Make current workspace and identity visible at consequential moments. On switching, define what happens to drafts, selections, uploads, notifications and open dialogs. Recheck access for deep links and distinguish inaccessible resources from resources that legitimately moved. Avoid displaying another workspace's cached data during a loading transition.

Test two tabs in different workspaces, identical resource names, revoked membership, background job completion after switching and an external invitation opened under the wrong account. A UI inspection can reveal wrong-context behavior; proving tenant isolation requires server/API evidence. Record that distinction in every finding.

## 10. Account closure and verification boundary

Treat export, subscription cancellation, organization departure and account deletion as separate outcomes. Explain retained obligations or pending work using actual product rules. Define ownership transfer before the last administrator leaves. Make time-limited recovery and irreversible steps truthful and visible.

Finish with an evidence table covering UI behavior, accessibility, integration dependencies and security checks actually performed. The concept is approvable only when actor, scope, transitions, side effects and recovery are explicit. Implementation is complete only when the approved behavior is verified; a secure-looking interface is never proof that authorization or identity assurance is enforced.
