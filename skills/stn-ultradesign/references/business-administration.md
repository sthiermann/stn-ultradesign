# Business administration: settings scope, roles and member lifecycle

Load when auditing or designing a business application with personal accounts, organizations, workspaces, projects, teams, members, roles, policies, billing or administrative settings. Read [identity-permissions.md](identity-permissions.md) for authentication and security boundaries, [workflows.md](workflows.md) for transition contracts, and [developer-platforms.md](developer-platforms.md) for credentials, API settings and webhooks.

These structures, decision rules and audit procedures are original working methods. Verify the actual product edition, account type, administrative experience and governing policies before proposing a menu or permission model.

## 1. Learn the boundaries, not the menu coordinates

**Decision rule.** Preserve the real ownership and permission boundaries. Improve scope visibility, explanations and navigation without collapsing them into a single ambiguous “Settings” area. An administrator, owner, billing contact and product user are separate responsibilities unless the actual product deliberately combines them.

## 2. Inventory every setting as a controlled resource

Before rearranging navigation, make a settings register. For every setting record: canonical name, purpose, owning scope, affected people, read permission, write permission, source of authority, default, override rules, persistence, effective time, dependencies and recovery. Include rarely visited settings and settings accessible only by direct URL.

In a full audit, enumerate and inspect every settings page, component usage, widget, drilldown and defined state transition in scope. A shared component's passing example does not prove its other usages correct. Expand the ledger for every applicable role/capability variant, inherited/external setting mode and scope variant. Attach evidence or an explicit untested reason to each entry; untested entries prevent a claim of complete coverage. Risk prioritizes the order of work, not undocumented omissions.

Identify the layers the application genuinely has. A solo tool may need only personal and project settings; a multi-tenant service may also need organization, workspace, environment and billing-account layers. Do not add an enterprise hierarchy merely because a reference product has one.

Distinguish personal identity from a membership record. One person may belong to several organizations, with a different role and notification preference in each. Changing a global display name can affect multiple contexts; leaving one workspace need not delete the person's account. Put these consequences into the concept contract before selecting controls.

Completion criterion: every audited setting has one authoritative home, a known scope and an explicit owner. Cross-links may improve discovery; duplicate editable copies require a shared source of truth and consistent feedback.

## 3. Choose a home by who and what changes

Use this proposed placement table as a starting point, then adapt it to the product's domain and research.

| Setting family | Default home | Typical contents | Scope cue and audit question |
|---|---|---|---|
| Personal identity | Account/Profile | Name, avatar, contact identity | Does the change follow the person across organizations? |
| Personal security | Account/Security | Authenticators, sessions, recovery | Is this the person's identity or an organization requirement? |
| Personal preferences | Preferences | Language, appearance, accessibility, personal notifications | Is the preference global, device-local or membership-specific? |
| Organization identity | Organization settings | Organization name, domains, business profile | Does this affect every workspace or only the selected organization? |
| Membership and access | Organization/People and access | Members, groups, roles, invitations | Which scopes can the acting administrator manage? |
| Organization policy | Organization/Security or policies | SSO, provisioning, session rules, approved integrations | Which controls are inherited or externally managed? |
| Project/workspace configuration | Selected project or workspace settings | Workflow, fields, members, defaults | Does the user see the exact object being configured? |
| Resource-specific behavior | Resource settings | Sharing, ownership, retention override | Is the setting local and is an override allowed? |
| Billing | Billing account or organization billing | Plan, invoices, payer, tax, payment instruments | Is this a separate financial authority or payer relationship? |
| Developer administration | Owning org/project/environment | Integrations, service identities, keys, endpoints | Is the credential personal or owned by an application? |

A profile menu can link to personal settings and an explicit administration destination. Organization/project switchers should expose the current context before people enter consequential settings. Use separate headings when personal and organization controls must share a screen. Search results should include a scope label and preserve that scope after navigation.

Where billing exists, distinguish viewing invoices, changing payment methods, managing spending and administering product resources. A generic administrator label cannot explain those separate grants.

## 4. Model permissions as decisions, not role names

Create a permission matrix using `principal + action + resource + scope + conditions + authority source + result`. Role names are a readable projection of that matrix. Separate viewing configuration, changing configuration, using the feature, accessing content and granting access to others.

Explain the product's actual grant, inheritance, condition and denial rules. Do not assume that the most restrictive role wins or that a weaker local grant can cancel inherited access.

The following is an **illustrative contract**, not a ready-made authorization policy:

| Action | Resource/scope | Questions the contract must answer |
|---|---|---|
| Edit own notification preference | Membership in workspace A | Personal override allowed? Locked by policy? |
| Invite a colleague | Organization A, selected projects | Can the actor grant this role and these scopes? Seat or domain restriction? |
| Manage project fields | Project A1 | Local fields or a shared schema affecting other projects? |
| View billing documents | Billing account B | Financial permission independent of organization membership? |
| Enforce SSO | Organization A | Authorized security role, tested provider and recovery policy? |
| Export audit events | Organization A | Separate read/export rights, sensitive fields and retention? |
| Revoke integration access | Integration A1-production | Correct environment, owner and dependent workloads? |

Show effective access and its origin where administrators must diagnose it: direct grant, group membership, inherited role, time-bound grant or external policy. If the actor cannot inspect an ancestor policy, say that the view is incomplete instead of claiming there is no inherited access. Verify decisions on the server; front-end visibility is only the presentation layer.

## 5. Decide what each user sees

Use **enabled** for actions the person can perform now. Use **disabled with an explanation** when the action is relevant and a prerequisite, policy or temporary condition explains its unavailability. Use **request access** when there is an actual approval route. Use **hidden** when a capability is irrelevant, its existence is sensitive or the product deliberately reduces noise. These choices are contextual; none replaces access control.

Ensure explanations are available to keyboard and touch users, not only pointer hover. Distinguish no permission, no product entitlement, insufficient plan, incomplete setup, policy restriction and temporary outage. Do not turn an access denial into an upsell when a purchase would not solve it.

Direct URLs must have a deliberate outcome: request permission, switch to the correct account, return to a safe context or display an appropriately non-disclosing unavailable state. A blank page is not an authorization design. Preserve the intended destination when a legitimate access request is approved.

## 6. Make the member directory operational

A useful directory supports the administrator's actual decisions: who has access, to what, through which source, and what needs attention. Show invitation/membership state, roles, scope and provisioned source where relevant. Avoid displaying global account status as if it were organization membership status.

Provide filters for actionable questions such as pending invitations, privileged members, externally managed accounts or expiring access when supported by the product. Row actions should be named and contextual. Detail views expose the effective permission explanation and a history of meaningful changes. Handle duplicate names and users with multiple identities safely.

For bulk operations, define whether selection means visible rows, the current page or all filtered results. Before applying a consequential change, show scope, counts and incompatible targets. Afterwards report per-target results and retain a recoverable selection. Make role and scope visible on narrow screens without forcing users to infer identity from an avatar.

## 7. Design the entire membership lifecycle

Use separate states with explicit transitions:

| Lifecycle step | Required behavior and recovery |
|---|---|
| Prepare invitation | Identify recipient, scope, proposed permissions and any seat consequence |
| Invitation pending | Show actual status; support permitted resend, edit or revoke behavior |
| Expired or revoked | Explain the route to a new invitation without suggesting old access works |
| Accept invitation | Show organization and role; handle the wrong signed-in identity |
| Membership active | Confirm effective access, required onboarding and policy obligations |
| Role or group change | Show before/after scope, inherited effects and whether change is effective |
| Access suspended | Explain temporary restriction, administrator route and retained data |
| Access restored | Re-evaluate current policy rather than assuming old access is still appropriate |
| Membership removed | Explain organization-specific revocation and remaining global identity |
| Ownership transferred | Validate successor, acceptance, residual rights and outstanding responsibilities |

Test pending invitations that outlive a policy change, account rename or organization switch. Do not preemptively grant access because an email was sent. Decide whether re-invitation restores previous grants or starts fresh; make the actual result visible.

## 8. Treat ownership and privilege changes as consequential

Identify last-owner/last-admin dependencies before removal, demotion or departure. Specify whether the successor must accept and when the previous owner's authority ends. Show impacts on billing, legal agreements, integrations, scheduled work and data ownership using actual product rules. Avoid encouraging credential sharing as a workaround.

A privilege increase should show the added capabilities and affected scopes; a reduction should show critical capabilities lost. Preserve the user's freedom to cancel before commitment. If fresh authentication or another approval is required, state the real policy and return to the original task afterwards. Test the actor demoting themselves, two administrators changing the same member and a successor becoming ineligible during transfer.

## 9. Resolve SSO and SCIM authority explicitly

Authentication answers which identity signed in; authorization determines what that identity may do. Provisioning changes account and membership data. Document their integration separately, even when a single identity provider participates in all three.

For every synced field or grant, show the authoritative source and an actionable management route. Define manual override behavior, precedence, synchronization delay and conflict resolution. A locally editable control that silently reverts after synchronization is a workflow defect. Do not advise users to disable provisioning casually to make an isolated edit.

Test first SSO login without prior membership, deprovisioning, deleted groups, renamed identities, duplicate accounts, manual-role conflicts, synchronization failure and provider outage. Include an approved administrator recovery procedure; do not invent a universal bypass. Record whether a removed user could be recreated by an unchanged upstream assignment. Verify offboarding across browser sessions and integrations with the responsible engineering owner.

## 10. Make setting changes truthful and durable

For every change distinguish edited locally, submitted, accepted, persisted and effective. Choose immediate saving for independent reversible preferences when appropriate. Use staged save/cancel for related values needing validation together. Use preview and impact review for policy changes that affect many people. Show the exact scope in the action area.

Use observed service guarantees for pending/effective messages; do not claim instant universal revocation after a successful request. Handle concurrent edits, refresh, failed saves and navigation with unsaved input. For inherited settings show the local value, effective value and controlling policy if the actor may inspect it. “Reset” must state whether it restores a factory default, an organization default or inherited behavior.

## 11. Audit trails and administrative accountability

Define the product's event contract: actor or service identity, action, target, scope, timestamp/time zone, outcome and correlation reference. Include before/after values where safe and relevant; redact secrets. Separate attempted, failed and completed changes. A success toast is not an audit trail.

Design search, filters, detail view, export and an understandable empty state. Explain retention or collection gaps without implying missing events never occurred. Protect viewing and exporting logs according to the real policy. Link a changed setting to its relevant history where supported, and test whether a background provisioning event can be distinguished from a human edit.

## 12. Keep administrative complexity usable across devices

Use a stable scope header and local navigation. Keep dangerous operations separated by consequence and explanation, not merely by red styling. Group settings around administrator intent; avoid a giant miscellaneous page or a maze of one-field dialogs. Provide direct links and scoped search for infrequent but important tasks.

On tablets and phones, prioritize identity, scope, current state and available action before secondary metadata. Turn oversized permission matrices into inspectable detail flows when necessary while preserving comparison access. Test keyboard navigation, screen-reader relationships, zoom, long role names, translated labels and the on-screen keyboard. An administration interface must not require a wide monitor to recover access or revoke a compromised member.

## 13. Run concrete acceptance scenarios

For an audit, inspect the following applicable scenarios in the existing product. In concept-first work, demonstrate them before concept approval, then verify the implemented behavior against the approved revision:

1. A member changes a personal preference without changing colleagues' settings.
2. A project administrator changes one project while the organization default remains intelligible.
3. A billing viewer can obtain an invoice without acquiring general product administration.
4. An administrator explains a member's effective permission, including a group or inherited grant.
5. A disabled action identifies a real prerequisite and offers an achievable next step.
6. An invitation opened under the wrong identity can be corrected without accidental membership.
7. Revoking a pending invitation prevents later acceptance according to actual service behavior.
8. A role reduction cannot be mistaken for removal of every independent grant.
9. A suspended, removed and globally deleted account have distinguishable outcomes.
10. A proposed last-owner removal is handled by the documented ownership policy.
11. An externally managed setting points to its authority and does not silently revert a local edit.
12. A failed or delayed save keeps the shown effective state truthful.
13. Two administrators editing the same policy receive an intelligible conflict outcome.
14. A workspace switch cannot apply a queued action to the wrong organization or environment.
15. A completed change can be found in the available audit history without exposing credentials.

Record route, actor, permission state, input, expected outcome, actual outcome and evidence for each test. Report server-enforcement and provider-integration checks separately from UI evidence. A beautiful directory or settings screen is incomplete if users cannot reliably determine who can do what and where.

Audit completion requires the observed scope map, decision matrix, lifecycle behavior, findings and verification evidence. Concept-first implementation additionally requires reviewable screens, actual user approval and conformance to that version. Existing approval or an explicit direct-implementation instruction does not need to be reopened. For a full audit, every registered surface, usage, role variant and defined transition must have a resolved coverage status and supporting evidence; clearly report any remaining untested entries. Improve organization, discoverability, clarity and recovery while preserving valid product constraints; any proposed permission-model change is a separate, explicit product/security decision.
