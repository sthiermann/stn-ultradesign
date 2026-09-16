# Developer platforms: API settings, credentials, webhooks, documentation

Read when auditing developer settings, integrations, API credentials, service accounts, webhook administration, developer portals, or interactive API references. Use [business-administration.md](business-administration.md) for organization and membership architecture. Use the work mode selected in `SKILL.md`. In concept-first work, follow [concept-to-code.md](concept-to-code.md). In audit-only work, inspect existing behavior and report findings; no design approval or implementation is required. Already approved scope and explicit direct-implementation authorization remain valid.

The decision tables, proposed page structures and acceptance cases are original working methods, not universal workflow mandates. They require verification against the application's real backend and policies. This module does not certify security or authorize creating, revealing, rotating, or revoking real credentials during an audit.

**Full-audit coverage:** enumerate every implemented credential type, settings page, list/detail view, component usage, widget, drilldown, overlay, permission-dependent state, and defined workflow transition in scope. Include each webhook endpoint-management surface and every published operation-reference page and explorer flow. Track inspected, failed, blocked, and untested entries explicitly. Shared components or representative examples do not discharge the obligation to review every usage and composition. Use non-production fixtures to exercise transitions safely; unavailable cases remain coverage gaps.

## 1. Place settings where ownership and consequences belong

Start with four separate questions: who owns the integration, which resources it can access, who pays for usage, and which environment it affects. Keep these answers visible on consequential screens. The location in navigation should match the controlling scope; cross-link related views rather than duplicating independent settings.

| Object | Candidate home | Context that stays visible |
|---|---|---|
| A person's access token | Account → Security or Developer access | Identity, resource scope, expiry |
| Workload identity | Organization/project → Service accounts | Owner team, effective permissions, workloads |
| Project credential | Project → Developers → Credentials | Project, environment, permitted operations |
| Webhook endpoint | Owning project/account → Developers → Webhooks | Destination, event scope, environment |
| Organization policy | Organization → Security → API access | Inheritance, affected projects, exceptions |
| API reference | Developer portal, linked from relevant settings | API version, server/environment, authentication |

These labels are candidates. Test whether people can find the right scope without guessing. For example, a finance administrator inspecting integration health should not need access to secret values. A developer managing staging must not land on production merely because both use the same page title.

Keep personal access separate from shared team or workload access where the product has those scopes. A project selector must correspond to actual enforcement, not cosmetic grouping.

## 2. Distinguish credential models before drawing the form

| Model | Represents | Design question |
|---|---|---|
| Personal token | An individual acting within supported permissions | What happens when their access changes? |
| Service/workload identity | A non-human integration | Who maintains it, and can it use short-lived access? |
| Project or account key | A provider-defined access contract | Does it identify a principal, meter usage, or both? |
| OAuth application | Delegated access through an authorization flow | What consent, scopes, and revocation apply? |
| Publishable identifier/key | Client-visible capability defined by provider | Which exact uses are safe to expose? |
| Webhook signing secret | Verification relationship for deliveries | Which endpoint/environment and rotation overlap? |

Never infer authentication semantics from the label “API key.” Identify whether a credential authenticates a principal, identifies a calling project, limits an integration, or combines those roles.

Evaluate the product’s supported workload identities, federation and short-lived access before proposing downloadable long-lived keys as the default. Match the actual deployment and security contract.

For automation, use an installation or workload identity where supported instead of tying essential infrastructure to an employee’s personal credential. Keep unsupported options as proposals with dependencies.

## 3. Specify permissions as actions, not a single admin switch

Record separate capabilities for listing credential metadata, creating credentials, choosing scopes, changing restrictions, revealing recoverable secrets, rotating, revoking, reading logs, testing endpoints, and resending events. Review permission dependencies and delegated authority. A user must not grant permissions their policy forbids.

For every action, identify the backend check and resource context. Hiding a button is presentation, not authorization. Direct-request checks with mismatched tenant, project, credential or endpoint identifiers require an explicitly authorized security test environment; otherwise record the enforcement dependency.

Render denied states with a useful reason when disclosure is allowed: insufficient role, organization restriction, missing approval, unavailable feature, or expired session. State who can resolve the issue without exposing private organizational information. Never equate “can revoke a credential” with “can read its secret.”

## 4. Design creation and secret handling around the real contract

The concept should show creation with a meaningful name, intended workload, scope, environment, expiry policy and review summary where supported. Offer task-based scope presets only when their contents are inspectable. Explain read/write distinctions and broad selections.

One-time disclosure is conditional on the product’s actual credential lifecycle. Verify whether a value can be recovered, revealed again or only replaced; render that contract accurately and keep secrets out of research evidence.

For a one-time secret, show the limitation before generation and again at handoff. Provide an explicit copy or download action and accessible success/error feedback. Copy failure must leave the authorized user a viable way to secure the secret. Do not infer storage success from a clipboard click. After the handoff closes, show metadata and a replacement path instead of a fake reveal control.

Mask secret-bearing fields by default when appropriate, but understand that masking alone is not protection. Check network responses, rendered DOM, persistent state, analytics, session replay, crash reports, exports, and generated snippets. List endpoints should return necessary metadata rather than all secrets. Keep sensitive creation responses out of incidental telemetry and browser persistence.

For new credential designs, document secure generation, protected storage or verification, disclosure, and revocation semantics with engineering before promising them in the UI. For existing integrations, preserve their real contract. Do not invent universal hashing, encryption, or recoverability rules: symmetric verification secrets and bearer-token verification can require different storage designs.

## 5. Make lifecycle changes operationally understandable

| Transition | Show before commitment | Verify afterward |
|---|---|---|
| Create | Owner, scope, environment, expiry | Credential exists once; authorized handoff works |
| Narrow access | Removed capabilities and likely dependents | Forbidden operations fail at the backend |
| Rotate | Replacement plan and any overlap deadline | New access works; old access ends as scheduled |
| Revoke | Credential identity and affected integration | Further requests fail under the documented semantics |
| Expire | Time zone, deadline, renewal/replacement path | State and enforcement agree |
| Disable temporarily | Reversibility and resumption conditions | Behavior matches the actual API contract |

Distinguish planned rotation from compromise response. Planned rotation may permit overlap if supported; confirmed exposure may require immediate revocation despite disruption. Show the consequence and preserve historical metadata when the product retains it; do not label revocation as complete deletion.

Use absolute deadlines alongside relative time when urgency matters. Show “expiry unknown” or “does not expire” only when supported by source data. Handle policy changes, owner departure, disabled accounts, and lost keys as explicit states. Revoke-all deserves a clear scope summary; do not hide an organization-wide effect inside a row menu.

Completion: the lifecycle diagram and UI states agree with server behavior, including failures between generation and handoff, partial deployment, and concurrent updates.

## 6. Provide observability without leaking secrets

A credential inventory can expose name, non-secret ID or safe fingerprint, owner, environment, scope summary, creation time, expiry, status, and available usage evidence. Separate “never used,” “usage unknown,” “no recent activity,” and “telemetry unavailable.” State freshness or retention limits where they affect a decision.

A governance view can expose allowed credential metadata and administrative operations without revealing raw credential values. Preserve the exact distinction between inspecting usage and accessing the secret.

Connect a selected credential or integration to related requests, errors and events when authorized and supported. Preserve object and time context through investigation and return.

Inspect log access, retention, redaction, pagination, freshness, and export behavior. Prefer request IDs and safe metadata for support. Show headers and bodies only at permitted detail levels; redact authentication material and sensitive payload fields. A screenshot or exported incident report must not silently become a credential leak. Clearly distinguish an API request log, a user administration audit record, and a webhook delivery attempt.

## 7. Treat webhooks as managed integrations

Model endpoint, event subscription, event, delivery attempt, and downstream processing as separate objects. The endpoint page should identify owning scope, environment, destination, enabled state, subscribed event types, payload/API version where applicable, signing configuration, and recent health.

The setup concept should include choosing the event scope, entering a destination, configuring verification, sending a test event, inspecting the result, and deciding whether to enable the endpoint. A successful synthetic test does not establish complete business processing. Explain whether test sends can create records or trigger downstream automation.

Subscription selection should expose exact event identifiers and useful descriptions. Make broad subscriptions intentional. Show changed subscriptions and destinations in review, because each changes what data goes where. A local development destination, sandbox endpoint, and production endpoint may require different verification material.

Diagnose delivery authentication with safe identifiers and the actual signing contract. Distinguish environment-specific secrets and body transformations without printing secret values into logs or prototypes.

If the product sends server-side requests to user-provided URLs, review server-side request forgery controls, destination restrictions, redirect handling, and network boundaries. A URL-shaped input and client-side validation are insufficient. Review endpoint testing and API explorer proxies under the same threat model.

## 8. Explain delivery, retries, and replay precisely

| Delivery view | Required distinction |
|---|---|
| Event identity | Business event versus each transport attempt |
| Timeline | Generated, attempted, acknowledged, failed, retry scheduled |
| Outcome | HTTP delivery result versus downstream business completion |
| Failure detail | Transport, timeout, response status, verification, processing if known |
| Replay | Historical event, chosen destination, current authorization, potential side effects |
| Evidence | Redacted payload, relevant headers, latency, attempt IDs |

Display the selected integration’s actual retry, ordering and redelivery policy. Manual replay may coexist with automatic retries; do not promise ordering, cancellation or deduplication that the backend does not provide.

Provide recoverable failure states: inspect, correct configuration, resend where allowed, or escalate with a safe diagnostic record. Before replay, show event, endpoint, environment and expected consequences. A replay control does not establish safe deduplication in the receiver.

Keep outbound request idempotency separate from webhook deduplication. A key used to retry an API request does not automatically make event consumption idempotent.

Acceptance includes duplicate, delayed, out-of-order, malformed, wrong-environment, wrong-secret, disabled-endpoint, and exhausted-retry cases relevant to the provider. State explicitly what is unknown rather than presenting transport acknowledgement as completed fulfillment.

## 9. Separate the API contract from its presentation tool

Verify the project’s OpenAPI specification and tooling versions before proposing a migration. The `openapi` format version and the API’s `info.version` describe different things. An interface specification does not prescribe a documentation layout.

Swagger UI and Redoc/Redocly are tooling choices. Record the actual edition, package version, rendering capabilities, hosting model, and interactive-console behavior. A visually rendered schema is not evidence that every declared feature is interpreted correctly. Retain the contract source and test examples against the deployed API where authorized.

Describe supported authentication accurately at global and operation level. OpenAPI security requirements can express alternatives and combinations; flattening them into one “API key required” badge can mislead users. A described permission is not backend enforcement. OpenAPI security

## 10. Make the reference answer a developer's next question

Propose a navigable reference with resource/task grouping, search, stable operation anchors, clear version selection, and nearby conceptual guides. On wide screens, a documentation column and example/result panel may help; on smaller screens, use ordered sections or tabs without losing the current operation or entered values.

| Region | Questions it must answer |
|---|---|
| Operation header | What does this do; which method/path; what side effects? |
| Access | Which identity, scopes, resource permissions, and environment? |
| Input | Which parameters are required, where sent, and under which constraints? |
| Body/schema | Which types, nested objects, variants, units, and semantics apply? |
| Examples | What is the smallest useful request; what changes in a realistic case? |
| Response | What status, structure, headers, pagination, and empty results occur? |
| Errors | What failed; can it be corrected or retried; which identifier helps support? |
| Lifecycle | What version, deprecation, replacement, or migration applies? |

OpenAPI distinguishes parameters and request payloads. Reflect requiredness, serialization, and location accurately rather than turning every input into an interchangeable text box. OpenAPI parameters

Keep descriptions and schemas inspectable together. Provide readable type information and expandable nested details, but leave required constraints discoverable. Examples must use synthetic data and explicit placeholders. Preserve syntax and accessibility when copying; distinguish response examples from actual server results. Validate examples against the advertised contract and test pagination, validation errors, and permission failures rather than documenting only a successful response.

## 11. Design the explorer as an action surface

Default to a documented sandbox or non-production target where available. Display destination, environment, identity context, and operation effects before execution. A production choice must be unmistakable; high-impact actions require deliberate confirmation according to the product's risk model. Do not infer safety only from an HTTP method.

Keep supplied credentials out of shareable links, analytics, ordinary browser persistence, and default copied examples. Provide clear session cleanup and redacted copy/export. If persistence is an intentional feature, document storage, lifetime, and removal rather than enabling it incidentally.

Inspect the API explorer’s configured submission methods, credential persistence and validation behavior. A collapsed request editor is not equivalent to disabling submission.

Confirm where requests originate and which parties receive credentials, including any proxy and destination restrictions. Never add an unrestricted proxy or forward authorization to arbitrary hosts to make an example request succeed.

Handle cancelled, timed-out, rate-limited, and ambiguous requests honestly. A client timeout may leave server outcome unknown. Show a request identifier and safe recovery path where supported. Reset or revalidate credentials when the environment or server changes; prevent test/live mismatch without echoing the submitted secret.

## 12. Verify concrete cases before calling the design complete

The following are test scenarios, using synthetic accounts and an authorized non-production environment:

| Case | Acceptance condition |
|---|---|
| Analyst creates a read-only export integration | Scope and owner are clear; write attempt is denied by server |
| Staging administrator follows a production credential link | Real authorization applies; environment remains explicit |
| Admin inspects a colleague's token | Permitted metadata is visible; unrecoverable secret is absent |
| Clipboard action fails at one-time handoff | User can complete a supported secure handoff without duplicate issuance |
| Rotation overlaps deployment | Active credentials and cutoff are accurate; old access ends correctly |
| Credential expires during work | UI and API explain failure and provide authorized recovery |
| Webhook is delivered twice | Receiver produces the intended effect once or follows a documented safe policy |
| An old event is resent after a new one | Processing follows the actual ordering/reconciliation contract |
| Endpoint reports success but downstream job fails | Delivery and business-processing states remain distinguishable |
| Explorer changes from sandbox to production | Credential/context validation and consequential-action review rerun |
| Reference contains an unsupported schema feature | Validation reports the gap; UI does not silently misdescribe it |
| Logs are exported for support | Secrets and unauthorized payload details remain redacted |

For frontend work, verify responsive tables, keyboard access, accessible copy status, code-block scrolling, long URLs, large schemas, loading/error states, and permission-sensitive empty states. Keep backend operations outside presentation components and verify actual response handling. Record screenshots and contract/API evidence separately: neither proves the other.

Audit completion requires mapped permission/lifecycle behavior, every in-scope page/component usage/widget/drilldown and defined workflow transition inspected, and evidence for relevant checks. Unavailable backend, provider, or device checks remain explicit gaps. For concept-first implementation, additionally require the approved concept and conformance to it. Missing access or fixtures must remain reported coverage gaps, never silently count as passed. Do not claim an end-to-end security result from a visual audit alone.
