# Developer-interface UX: API access, webhooks and API documentation

Research and access date: **September 16, 2026**. Sources are public original documentation from Stripe, Google, Atlassian, Apple, GitHub, the OpenAPI Initiative, SmartBear, Redocly and OWASP. Every page below was opened directly and relevant content read. No authenticated customer system was operated, and no real key was created, revealed, rotated or revoked.

The resulting `references/developer-platforms.md` is independently authored. Tables, decision steps and acceptance scenarios are our synthesis. No third-party skills, templates, code or assets were incorporated. Published product rules are examples, distinguished from security guidance and the OpenAPI specification. This module evaluates the user experience of legitimate developer settings; it does not authorize credential collection or penetration testing.

## Source register

All sources were read directly on September 16, 2026. “Product” identifies a vendor-specific contract; “specification” identifies the authoritative technical description; “guidance” does not imply certification.

| ID | Source | Type | Relevant finding |
|---|---|---|---|
| D01 | [Stripe API keys](https://docs.stripe.com/keys) | Product | One-time display does not apply to every key. Manually created live secrets differ from certain Stripe-created keys. |
| D02 | [Stripe key practices](https://docs.stripe.com/keys-best-practices) | Product/guidance | Restricted access, explicit management permissions and usage review belong to key administration. |
| D03 | [Stripe Workbench](https://docs.stripe.com/workbench/overview) | Product | Requests, errors, objects and events can be investigated together, illustrating connected diagnostic interfaces. |
| D04 | [Stripe webhooks](https://docs.stripe.com/webhooks) | Product | Automatic retries, manual resend and absence of delivery-order guarantees are separate concepts. Manual resend does not automatically stop further retries. |
| D05 | [Stripe signature errors](https://docs.stripe.com/webhooks/signature) | Product | Verification depends on the unchanged body and matching endpoint secret. Local CLI forwarding and Dashboard endpoints use different secrets. |
| D06 | [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) | Product | API-request idempotency is a separate mechanism; it does not automatically deduplicate an application's webhook processing. |
| D07 | [Google API keys](https://docs.cloud.google.com/docs/authentication/api-keys) | Product | Standard API keys do not authenticate a principal; bound authorization keys act as a service account. Restrictions and product caveats matter. |
| D08 | [Google authentication](https://docs.cloud.google.com/docs/authentication) | Product/guidance | Human and machine identities, plus short-lived and federated authentication methods, are described separately. |
| D09 | [Google service account key practices](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys) | Product/guidance | Long-lived keys require deliberate lifecycle management; alternatives should be evaluated. |
| D10 | [Atlassian token management](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) | Product | Personal and service-account tokens have distinct management paths. Expiry and scopes are visible; recovery of the secret value is not provided. |
| D11 | [Atlassian API Access reference](https://developer.atlassian.com/cloud/admin/api-access/rest/api-group-api-token/) | Product/API contract | Management operations have their own permissions. Metadata includes expiry and last activity; this is not retrieval of a secret value. |
| D12 | [Apple App Store Connect API](https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-api) | Product | Individual and team keys have different paths and access models. Private keys can be downloaded once; revocation is irreversible. |
| D13 | [GitHub personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) | Product | Token types and permissions differ; GitHub Apps are an alternative for suitable automation. |
| D14 | [GitHub webhook practices](https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks) | Product/guidance | Secret-based verification and delivery identifiers support appropriate processing and redelivery. |
| D15 | [GitHub failed deliveries](https://docs.github.com/en/webhooks/using-webhooks/handling-failed-webhook-deliveries) | Product | GitHub does not automatically retry failed webhook deliveries. Interfaces should explain this difference from Stripe. |
| D16 | [OpenAPI 3.2.1](https://spec.openapis.org/oas/v3.2.1.html) | Specification | Published September 10, 2026; also the official latest document on the access date. Format version and documented API version are different. |
| D17 | [OpenAPI security](https://learn.openapis.org/specification/security.html) | Official explanation | Security definitions and per-operation use must be read together. Interfaces must not misrepresent combinations and alternatives. |
| D18 | [OpenAPI parameters](https://learn.openapis.org/specification/parameters.html) | Official explanation | Parameter location, serialization and request body are separate contract elements. A generic input does not automatically represent them correctly. |
| D19 | [Swagger UI configuration](https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/) | Tool | Interactive execution, persisted authorization and external validation have distinct settings. Review UI defaults. |
| D20 | [Redocly CORS proxy](https://redocly.com/docs/realm/config/cors-proxy) | Tool/product | Proxy behavior and destination restrictions change data paths. Guidance applies to the documented edition and configuration. |
| D21 | [OWASP object-level authorization](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/) | Security guidance | Resource authorization belongs on the backend; hidden buttons do not prevent unauthorized direct requests. |
| D22 | [OWASP SSRF prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) | Security guidance | Server requests to configured URLs require controls, including webhook tests, destinations and documentation proxies. |

## Lessons for the skill

**Information architecture must show ownership and effect.** Personal tokens belong to a person; technical integrations need a durable owner and explicit organization, project and environment context. Navigation follows the actual product model. A global “API” page can be too vague; a project filter is misleading if it filters only the list while credentials retain broader permissions.

**Administration does not imply unrestricted secret visibility.** Listing, creating, changing permissions, rotating, revoking and revealing are separate capabilities. Governance can expose usage metadata and revocation without returning secret values. The skill calls for an action matrix and appropriately scoped implementation evidence rather than one universal administrator switch. Synthetic fixtures or redacted evidence should support UX review; obtaining real secret values is not necessary.

**Lifecycle UX includes failure.** One-time display needs an understandable handoff, including failed copying and interrupted creation. Planned rotation and confirmed compromise need different guidance. Expiry requires understandable time zones; unknown last use must not be presented as never used. These acceptance ideas are original design proposals to reconcile with the real backend contract.

**Webhooks need operational interfaces.** Endpoint, event, delivery attempt and domain processing are distinct. HTTP success does not establish a completed order. Resending historical events may have consequences, so a design should explain destination, environment, event and replay meaning alongside diagnosis and recovery. Deduplication is processing behavior, not a decorative checkbox.

**API documentation can both explain and act.** A reference should connect navigation, version, authentication, inputs, schemas, responses, errors and examples. An interactive explorer additionally needs an explicit destination environment, appropriate handling of user-supplied authorization and an understood network path. An attractive Swagger or Redoc screen does not establish these properties.

**Version checks matter.** OpenAPI 3.2.1 was published only six days before this review. This does not justify an automatic migration: validators, renderers and generators must support the features used. Recheck vendor navigation, expiry rules, editions and behavior during implementation.

## Acceptance and limits

The reference includes cases for read-only integrations, staging/production context switches, restricted administrator views, interrupted secret handoff, rotation, expiry, duplicate/late webhooks and redacted diagnostic exports. For design work, agree the concept, states and permitted actions before production implementation, then check implementation against the same contract. Audit-only work does not require implementing a redesign.

A requested full audit inventories every implemented page, usage, widget, drilldown and defined workflow transition. Relevant developer interfaces include credential subtypes, permission states, webhook management and every published operation/explorer implementation in scope. Shared components and examples do not replace their individual usage checks. Inaccessible states remain coverage gaps.

This research includes no live customer-system verification or security certification. Publicly documented properties do not prove a later implementation's end-to-end security. Vendor examples establish no universal expiry period, retry interval or token-management interface. Making these differences visible and testable is part of the skill's purpose.
