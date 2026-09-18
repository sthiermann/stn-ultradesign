---
name: stn-ultradesign
description: Audit application UI/UX, discover individual design preferences, preserve existing features through traceable redesigns, and implement approved concepts faithfully across desktop, tablet, and mobile. Use for substantial frontend reviews, workflow redesigns, design-system work, and concept-to-code projects; a small unrelated code fix does not trigger a whole-product audit.
---

# STN Ultradesign

Turn observed user needs into coherent interfaces and complete workflows. Produce evidence, a reviewable design, and verified behavior. Match the user's language in discussion and deliverables. The reference material is in English; that does not set the product's language.

## Select the work mode

- **Audit:** Inspect the requested scope, produce findings and coverage. An audit request alone does not authorize a redesign.
- **Concept first:** For a new design or substantial redesign, discover individual preferences, map existing capabilities within the requested scope and its affected dependencies, present a concrete concept, refine it with the user, then implement the approved version. Use the [delivery workflow](references/delivery-workflow.md) to coordinate requirements, creative direction, component engineering, review and acceptance. Read [brand-discovery.md](references/brand-discovery.md), [discovery-and-preferences.md](references/discovery-and-preferences.md), [feature-parity.md](references/feature-parity.md) and [concept-to-code.md](references/concept-to-code.md) before developing the direction. Preparation, research, and isolated prototypes can proceed before approval; changes to the production implementation wait for concept approval. An explicit instruction to implement directly overrides this implementation boundary; existing features and confirmed preferences still apply.
- **Implement agreed concept:** Find the actual approved artifacts and decisions in this conversation or project; translate them into acceptance checks and implement them without reopening settled choices. Resume the [delivery workflow](references/delivery-workflow.md) at the authorized stage. Approval already given remains valid for that scope.
- **Focused improvement:** Address the specified component, workflow, or defect with proportional investigation. Preserve the rest of the product.

Do not turn a scoped request into a full audit. **A requested full audit must inspect every discovered page, component usage, widget, dialog, drilldown level and defined workflow transition in scope.** Representative screens are insufficient. Test each item's relevant states, roles, input and responsive configurations. Shared-component review must be accompanied by checks in every usage context. Reconcile static routes with runtime navigation, overlays, lazy content and permission-dependent surfaces. Track inaccessible or untested items as gaps; do not claim full completion until resolved. A reduced sample is a scope change requiring the user's agreement.

For full audits, maintain the schema-2 inventory and planned obligations from `audit-method.md` before recording results. Link usages to their surfaces/families and transitions to endpoints/workflows. Plan finite, justified behavior classes per entity; do not multiply every global dimension onto every screen. Newly discovered entities, contexts or branches reopen reconciliation. Source inspection cannot close runtime obligations; missing access is blocked, not inapplicable. An approved sample can finish its agreed scope but never completes the original full-audit coverage claim.

## Keep account and access reviews about the experience

Account and access work means reviewing the layout, language, navigation, states and recovery of sign-in, personal settings, roles, API access and related journeys. It is not permission to collect credentials, inspect secret stores, bypass access controls or conduct a penetration test.

Use user-controlled sign-in, an already authenticated session, or authorized synthetic test accounts. Do not ask the user to paste passwords, one-time codes, recovery codes, private keys or live API tokens into the conversation. Do not search password managers, credential files, `.env` secrets, browser cookies or session storage for access. Inspect safe configuration contracts and redacted fixtures instead. If a secret is unexpectedly visible, exclude it from notes, screenshots, prototypes and published artifacts; do not reveal or copy it to prove a design point.

An audit may inspect a form without submitting it. Creating or revoking real credentials, changing real permissions, sending test webhooks/messages, ending sessions or deleting data is a consequential product action, not implicit audit authorization. Exercise those paths only with explicitly authorized actions and safe fixtures. Missing access remains a recorded gap. Backend security enforcement is a dependency to identify, not a security certification this design skill can supply.

## Establish the product contract

Read project instructions, the existing design system and component library, supported browsers, app routes, localization, available tests, and any approved designs. Identify the users, their main tasks, roles, platform constraints, and current data states. Before allocating layout space, establish the application’s purpose, primary unit of work, operating conditions and observable success criteria using [product-thinking.md](references/product-thinking.md). Require a task reason for each persistent region; explore hiding secondary chrome when useful without hiding critical state or the return path. Distinguish evidence from assumptions. Ask only for missing decisions that materially affect the result; continue independent work while waiting.

For substantial work, use [requirements-conformance.md](references/requirements-conformance.md) to turn consequential requests, answers and discovered constraints into one traceable requirement register. Existing project records can serve this purpose. Link each active requirement to its decision, affected usages and observable acceptance obligations; preserve the distinction between accounted for, depicted, implemented and verified. Resolve contradictory instructions by their actual authority and scope. Changed decisions reopen affected evidence; a recorded gap is not a satisfied requirement. A focused fix needs only its bounded record.

For a substantial concept, cover at least **twenty distinct, product-specific preference questions early**, and more whenever an unresolved decision materially affects the result, before committing to a visual direction. Carry forward already confirmed answers without re-asking them; ask the remaining questions in digestible batches. Record explicit delegation if the user waives the remaining interview. Do not pad the count with discoverable facts, apply it to a narrow fix, or turn unanswered optional preferences into an approval gate. Use the [design brief](assets/design-brief.template.md) and distinguish confirmed answers, pending preferences and hypotheses.

During audits as well as concept work, ask as many focused questions as necessary to resolve material uncertainty about meaning, work practices and direction. Offer reasoned choices that distinguish applicable requirements, established vendor patterns and taste. Reuse confirmed answers; keep a decision queue and continue independent inspection while dependent conclusions remain provisional. An audit has no arbitrary question quota or ceiling. Follow [discovery-and-preferences.md](references/discovery-and-preferences.md).

Establish the company/product brand and the authority of supplied guidelines or assets. Ask how much to inherit separately for typography, colors, shapes, icons, imagery, voice, layout/navigation, motion and materials. Record preserve/evolve/reinterpret/explore decisions with concrete limits in the [brand inheritance matrix](references/brand-discovery.md); do not infer that keeping brand colors also freezes the old layout. Reuse existing answers and authorization.

Remain neutral to design language. When the user chooses a company identity, platform language or visual reference, read [project-research.md](references/project-research.md) before committing to the direction. Establish the requested platform, generation and degree of inheritance through [brand discovery](references/brand-discovery.md#research-the-selected-language-for-this-project). Inventory applicable source sections and component families; distinguish documented rules, inspected visuals and observed interactions. Translate them into project rules with requirements and acceptance links, prove demanding examples, then verify every affected usage. Do not inherit a previous project's presets. Keep concrete reference names, URLs, observations and comparisons in the target project's private evidence, outside this reusable package.

Discover existing role/admin visibility, supported languages, light/dark/system choices, density preferences, graphs and operational thresholds relevant to the requested scope. For design or implementation, maintain an [old-to-new feature map](assets/feature-map.template.md) covering that scope plus all transitively affected shared usages and dependencies. A full-product redesign maps every discovered capability, including those outside its current prototype. A focused fix maps its affected capabilities without turning unrelated areas into a product-wide design task. Preserve behavior and supported variants unless specifically changed. A general aesthetic approval does not authorize feature loss; retirement requires an actual user decision identifying the affected capability and consequences. Audit-only work records the current baseline and coverage; it does not require proposed destinations or a redesign map.

Before applying a shared component treatment, classify each affected action by task and owning workspace using [component-states.md](references/component-states.md#choose-behavior-before-styling-its-shell). Record its direct result, interaction surface and return path. Consistency applies within a task family; an agreed editor placement does not turn command menus or display toggles into editors.

Map existing controls at action and state level, including hidden menus, edit modes, independent overlays, preferences and supported simultaneous panels. A page or feature-group label cannot account for its unfinished child actions. For moved capabilities, demonstrate their new entry, result and return with the [capability walkthrough](assets/capability-walkthrough.template.md). Preserve familiar user terminology in the comparison so users can find their existing work again.

Preserve established vocabulary, brand, working flows, and framework choices unless the requested change justifies replacing them. A familiar control is a useful default when it fits the task. Visual distinctiveness comes from an intentional, product-specific system, not universal bans on a font, color, radius, or layout.

Use this conflict order: explicit product requirements and applicable constraints; verified accessibility/security obligations; approved concept and existing system; task evidence; relevant platform guidance; stylistic preference. If an approved design conflicts with an obligation, expose the conflict and propose the smallest compliant revision; do not silently change either. Verify legal applicability separately rather than inventing it.

## Route to the necessary references

Read only the branches relevant to the current work. For a whole-product audit, cover every applicable branch over successive passes; persist progress rather than loading everything at once.

| Decision or task | Read |
| --- | --- |
| Full audit, coverage, findings, severity, evidence, completion | [audit-method.md](references/audit-method.md) |
| Company/product identity, supplied brand guidelines, selective visual and layout inheritance | [brand-discovery.md](references/brand-discovery.md) |
| Early preference discovery, twenty tailored questions, evidence versus taste | [discovery-and-preferences.md](references/discovery-and-preferences.md) |
| Binding requests and answers, conflicting decisions, acceptance obligations, changed requirements and completeness claims | [requirements-conformance.md](references/requirements-conformance.md) |
| Existing functions, old-to-new mapping, role/theme/locale/density and chart parity | [feature-parity.md](references/feature-parity.md) |
| Concept, alternatives, refinement, approval, exact implementation | [concept-to-code.md](references/concept-to-code.md) |
| User goals, information architecture, usability evidence | [product-thinking.md](references/product-thinking.md) |
| Hidden work, confusing navigation, incomplete primary tasks, live investigation and return | [task-flow-design.md](references/task-flow-design.md) |
| Layout, hierarchy, color, type, shapes, iconography, motion, tokens | [visual-systems.md](references/visual-systems.md) |
| Component anatomy, interaction states, selectors, messages, icons and consistent dialog/drawer families | [component-states.md](references/component-states.md) |
| Navigation hierarchy, overloaded settings, panels, selected materials, shape and motion | [navigation-and-materials.md](references/navigation-and-materials.md) |
| Desktop/tablet/phone, input modes, navigation and adaptation | [platform-adaptation.md](references/platform-adaptation.md) |
| Self-explanatory surfaces, expected click results, scoped loading, failure and success feedback | [interaction-comprehension.md](references/interaction-comprehension.md) |
| Forms, wizards, settings, search, editing, asynchronous flows | [workflows.md](references/workflows.md) |
| Existing or requested conversations, message composition, embedded messenger panels and delivery states | [messaging-workflows.md](references/messaging-workflows.md) |
| Redundant facts, repeated labels/help, conflicting summaries and unnecessary reading | [workflows.md](references/workflows.md#information-economy-in-the-actual-task) |
| Account and access workflows: sign-in, recovery, sessions, role selection and scope | [identity-permissions.md](references/identity-permissions.md) |
| Personal/org/project settings, invitations, roles, billing and governance | [business-administration.md](references/business-administration.md) |
| API credentials, service accounts, webhooks and OpenAPI documentation | [developer-platforms.md](references/developer-platforms.md) |
| Keyboard, screen reader, zoom, touch, contrast, WCAG distinctions | [accessibility.md](references/accessibility.md) |
| Business meaning, KPI definitions, decision support, missing context and analytical drill paths | [analytical-meaning.md](references/analytical-meaning.md) |
| Charts, dashboards, widgets, tables, network graphs | [data-visualization.md](references/data-visualization.md) |
| HTML/CSS/React, state, performance, component engineering | [web-engineering.md](references/web-engineering.md) |
| Machine-checkable requirement/stage bindings, stale results and optional evidence-file integrity | [delivery-ledger.md](references/delivery-ledger.md) |
| Text growth, wrapping, clipping, unintended overlaps, floating layers and responsive stress checks | [layout-integrity.md](references/layout-integrity.md) |
| Behavioral, visual, accessibility and concept-conformance checks | [verification.md](references/verification.md) |
| Substantial delivery, role handoffs, creative direction, independent review and acceptance | [delivery-workflow.md](references/delivery-workflow.md) |
| Current project research, reference authority, freshness and private evidence | [project-research.md](references/project-research.md) |

## Run the appropriate workflow

For substantial concept, redesign and design-system work, follow [delivery-workflow.md](references/delivery-workflow.md). It defines stage exits and responsibilities for requirements/UX, visual design, design engineering, independent review, integration and the product owner. Keep one current brief and component contract; link answers to decisions, affected usages and observable acceptance evidence. Use the [delivery record](assets/delivery-plan.template.md) when coordination benefits from it.

Produce actual creative and interactive artifacts, not only an audit or plan. Separate direction exploration, component specimens and complete journeys; each has a different reviewable scope. Use available subagents for bounded independent work and a reviewer separate from the author when supported. A single agent can perform sequential specialist passes when needed, but must not describe them as independent review or invent owner approval.

Audit-only work follows [audit-method.md](references/audit-method.md): reconcile inventory and obligations, observe the requested scope, record findings and gaps, and verify that evidence supports the completion claim. A focused fix uses the affected contract, implementation and verification without requiring the substantial-project ceremony. Existing authorization and user instructions govern which steps are necessary.

## Quality rules that apply throughout

- Treat loading, empty, error, success, offline, denied, partial, stale, and interrupted states as conditional product behavior, not decorative variations. Cover the ones the feature can reach.
- Adapt to usable space, content, input capability, and user preferences. Before claiming rendered layouts are ready, execute the affected-usage stress checks in [layout-integrity.md](references/layout-integrity.md); preserve intentional wrapping, scrolling and overlays while finding lost content or blocked actions.
- For every decision-bearing metric, table, chart, widget and drill path in scope, verify meaning, purpose/duplication, useful exploration/action and cross-surface consistency in distinct passes. Follow [data-visualization.md](references/data-visualization.md#trace-selection-drill-and-return-as-separate-transitions) through actual filter results; a destination label or URL is not proof of correctly scoped data. Unknown domain definitions remain gaps; proposed filters, comparisons or actions need a stated user benefit and data/permission dependencies. Established patterns are candidates, not mandatory features for every product.
- Check visual craft and task performance separately. Use [interaction-comprehension.md](references/interaction-comprehension.md) to compare what an affected surface communicates before action with its observed outcome and recovery. Record hypotheses separately from observed user understanding.
- Propagate confirmed design decisions to every affected usage and relevant context, with rendered evidence or explicit gaps. Review work/preservation, composition, information economy and interaction/adaptation in separate passes, then verify corrections on the latest artifact as specified in [concept-to-code.md](references/concept-to-code.md). A token, specimen or single successful screen is not proof of global consistency.
- Reconcile requirements in both directions before a readiness claim: each active requirement reaches its artifact and checks, and each consequential artifact choice has a requirement or authorized design discretion. Inspect the reference interpretation before scaling a selected language; inspect the approved concept again against the integrated result. Neither a source inventory nor a technical test pass establishes reference fidelity.
- Before presenting a substantial concept as ready, walk its critical tasks from a visible entry through real proposed detail, outcome and return using [task-flow-design.md](references/task-flow-design.md). A feature-map entry, dead button or placeholder does not establish a working journey. Keep the original full scope and unfinished branches visible. Translate feedback into a concrete change and fresh rendered evidence; preserve the owner's rejection until resolved.
- Accessibility needs semantic implementation and manual checks as well as automated scans. Client-side permission visibility does not establish server-side authorization.
- Label statements as standards, vendor guidance, research/heuristics, product decisions, or hypotheses when the distinction affects a recommendation. “Latest” and “best for this user” are different claims.
- Inspect visual changes on their actual delivery surface as described in [verification.md](references/verification.md), including surrounding content, visible name/version consistency, spacing and the selected responsive asset at the inspected revision. Size checks to the actual content column and affected variants. If that surface is unavailable, inspect the strongest available preview and state the limit; code/CI passes do not establish visual acceptance. Never invent screenshots, tests, scores, usage data, or user approval.
- Keep user data and secrets out of evidence artifacts. Use safe test fixtures for destructive or externally consequential journeys.

## Deliver the result

Use the smallest useful package for the mode: an audit with coverage and prioritized findings; a concept with its preference brief, feature map, visual and interaction artifacts plus open decisions; or an implementation with conformance and parity evidence and remaining gaps. Link artifacts and name what is ready for the next decision.

For full audits, and scoped audits where a ledger is useful, copy [audit.template.json](assets/audit.template.json) and follow the schema-2 format in `audit-method.md`. Run `python3 scripts/audit_coverage.py PATH --require-complete` from this skill directory. Separate valid records, agreed scope reviewed, original full scope reviewed and checks passed; percentages concern planned checks only. Version-1 ledgers require migration and fresh reconciliation. The script validates self-declared records; it cannot inspect the app, authenticate evidence, establish discovery completeness or certify UX/security. The [design contract template](assets/design-contract.template.md) records approved concepts.

For substantial delivery with changed requirements or contributor handoffs, use [delivery-ledger.md](references/delivery-ledger.md) to bind the current decisions and due-stage obligations before execution, then reconcile results and available local evidence with `scripts/delivery_check.py`. Reuse existing requirement and audit IDs; this helper supplements actual observation and review. A small focused task can retain its bounded record.

For version-dependent APIs, browser support, identity rules, or a claim about the newest platform guidance, verify the current primary source before applying it. Maintain project-specific decisions in the project; change this reusable skill only when the user requests an update.
