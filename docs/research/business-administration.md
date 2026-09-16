# Research: business application administration

**Reviewed September 16, 2026.** This research examined official Atlassian, Google, Apple and Stripe product documentation. The operational `skills/stn-ultradesign/references/business-administration.md` module was independently authored. No third-party skills, code, assets or templates were incorporated. Published product facts are distinguished from our design recommendations.

## Main finding

Effective administration organizes settings by their consequences: for a person, membership, organization, project, object, billing account or integration. A single undifferentiated settings menu hides those boundaries. A universal hierarchy of user, administrator and owner is equally unreliable: the products distribute specific capabilities across different roles, scopes and conditions.

Our synthesis: understand the application's actual resources, roles and responsibilities before redesigning its interface. Record each setting's location, effect, read/write requirements, authoritative data source, inheritance, persistence and time to take effect. This is a workflow and information-architecture exercise. Backend enforcement remains a separate dependency; showing or hiding controls does not prove authorization, and inspecting credentials is unnecessary.

## What the products demonstrate

**Atlassian.** Its documentation covers both Centralized and Original User Management. A site administrator can have different capabilities depending on the experience. Centralized management separates site administration from user-access administration. Organization-admin status alone does not imply product access; additional automatically assigned app roles can be removed separately. Record the management experience and effective capabilities rather than inferring authority from a title. [Admin roles](https://support.atlassian.com/user-management/docs/what-are-the-different-types-of-admin-roles/), [Site-admin differences](https://support.atlassian.com/atlassian-cloud/kb/site-administrator-role-in-the-centralized-user-management-and-original-user-management-experiences/)

Current Jira documentation uses space roles; an earlier project-role URL redirects to space-permission guidance. Roles and shared permission schemes can affect different scopes. That terminology change does not justify silently renaming an existing application's domain concepts. [Space roles](https://support.atlassian.com/jira-cloud-administration/docs/how-to-use-space-roles/), [Permission schemes](https://support.atlassian.com/jira-cloud-administration/docs/grant-space-permissions-using-permission-schemes/)

**Google.** Google Account manages personal information and its visibility. Cloud resources instead follow a hierarchy of organization, optional folders, projects and resources. A person is distinct from an organizational project they created. [Google Account](https://support.google.com/accounts/answer/15781205?hl=en), [Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)

Google Cloud combines inherited allow policies; deny policies and principal access boundaries add other mechanisms. A blanket rule that the most restrictive role wins would be misleading. Cloud Billing and Google payments profiles also have distinct, partly overlapping permissions. Explain effective access and its origin instead of inventing a simpler evaluation rule. [IAM overview](https://docs.cloud.google.com/iam/docs/overview), [Billing access](https://docs.cloud.google.com/billing/docs/how-to/billing-access)

**Apple.** Personal Apple Account information is separate from App Store Connect team administration. Several team roles exist, but there is one Account Holder. Individual and organizational program membership differ. Some roles and additional resource permissions cannot have their access limited to selected apps. [Apple Account](https://support.apple.com/en-gb/105023), [Accounts and roles](https://developer.apple.com/help/app-store-connect/manage-your-team/overview-of-accounts-and-roles), [User management](https://developer.apple.com/help/app-store-connect/manage-your-team/add-and-edit-users/)

Ownership transfer is more than another role change: organizational membership requires an eligible employee with authority to bind the organization legally. This is Apple's requirement, not a universal requirement for every product. The transferable lesson is to model an owner's actual obligations explicitly. [Account Holder transfer](https://developer.apple.com/help/account/access/transfer-the-account-holder-role)

**Stripe.** An organization-level grant is inherited by its accounts. Assigning a weaker account role does not cancel it. Multiple roles can apply simultaneously. Make the account/organization context and effective access clear. [Organization access](https://docs.stripe.com/get-started/account/orgs/team), [Roles](https://docs.stripe.com/get-started/account/teams/roles)

## Lifecycle and authority shape the interface

Atlassian's centralized experience distinguishes temporary suspension, with restorable roles and groups, from removal, which requires another invitation and assignments. Neither automatically deletes the person's global Atlassian account. Accurate confirmation copy must preserve that distinction. [Suspend or remove](https://support.atlassian.com/user-management/docs/remove-or-suspend-a-user)

With Atlassian SCIM provisioning, the identity provider manages synchronized groups and linked attributes. External users and managed accounts are treated differently. Local forms should not silently offer edits that disappear at the next synchronization. [Provisioning](https://support.atlassian.com/provisioning-users/docs/understand-user-provisioning)

Google documents propagation delays for IAM changes. Saving a revocation and its becoming fully effective are therefore different states. Verify the application's actual behavior before promising immediate effect. [Access-change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation)

Atlassian and Google provide audit logs with system-specific scope, access and availability. The skill must not invent unlimited retention or complete retrospective records. [Atlassian audit log](https://support.atlassian.com/security-and-access-policies/docs/view-audit-log-activities/), [Google Cloud audit logs](https://docs.cloud.google.com/logging/docs/audit)

## Original design model

The following model is our synthesis, not a universal menu specification:

| Scope | Candidate location | Main design question |
|---|---|---|
| Personal account | Profile, personal security, preferences | Does the change affect only this person? |
| Membership | Workspace-specific role and notifications | Can the setting differ across organizations? |
| Organization | Organization information, members, groups, policies | Who is affected, and who can administer it? |
| Project/workspace | Local workflows, fields, team and defaults | Is the effect local or shared through a scheme? |
| Billing | The responsible billing account | Are payment management and product administration separate? |
| Developer access | The owning organization, project and environment | Does the integration belong to a person or a workload? |

For each scope, derive the access decision from actor, action, resource, scope, conditions and authoritative policy. Choose visible, disabled with explanation, request access, or hidden according to the task. Do not confuse missing permission with an unavailable plan, service failure or unfinished setup.

Describe the full membership journey: prepare, send, accept, expire or revoke an invitation; change roles and groups; suspend and restore access; remove membership; transfer ownership. Define side effects, effective state, Back/cancel and failure recovery for every transition. An audit observes or simulates consequential transitions unless their execution is explicitly authorized with safe fixtures.

## Required review cases

A full audit inventories **every settings page, component usage, widget, drilldown and defined state transition**, including relevant role, scope, inheritance and provisioning variants. Risk determines sequence, not silent omissions. Unreviewed entries remain visible and prevent a full-coverage claim.

Concrete cases include a personal change that does not affect colleagues; a project change without unintended organization-wide effects; invoice access without general administration; explanations of inherited grants; invitations opened under the wrong identity; invitation withdrawal; concurrent role edits; the last owner; provider-managed attributes; delayed effect; organization switching during an action; and an understandable audit record without secrets.

In concept-first work, refine and approve scope structure, the role matrix, states, screens and actual wording before production implementation. Implement and verify that version; preserve earlier or explicit direct-implementation authorization as defined in the skill. Audit-only work ends with findings and coverage. Measure effectiveness through fewer configuration errors, clearer access decisions, successful recovery and faster discovery of the right setting. Research supplies grounded design rules; a real product pilot must establish their practical effect.
