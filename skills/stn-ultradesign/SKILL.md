---
name: stn-ultradesign
description: Audit application UI/UX, discover individual design preferences, preserve existing features through traceable redesigns, and implement approved concepts faithfully across desktop, tablet, and mobile. Use for substantial frontend reviews, workflow redesigns, design-system work, and concept-to-code projects; a small unrelated code fix does not trigger a whole-product audit.
---

# STN Ultradesign

Turn observed user needs into coherent interfaces and complete workflows. Produce evidence, a reviewable design, and verified behavior. Match the user's language in discussion and deliverables. The reference material is in English; that does not set the product's language.

## Select the work mode

- **Audit:** Inspect the requested scope, produce findings and coverage. An audit request alone does not authorize a redesign.
- **Concept first:** For a new design or substantial redesign, discover individual preferences, map existing capabilities within the requested scope and its affected dependencies, present a concrete concept, refine it with the user, then implement the approved version. This is the owner's preferred default for substantial design changes. Read [brand-discovery.md](references/brand-discovery.md), [discovery-and-preferences.md](references/discovery-and-preferences.md), [feature-parity.md](references/feature-parity.md) and [concept-to-code.md](references/concept-to-code.md) before developing the direction. Preparation, research, and isolated prototypes can proceed before approval; changes to the production implementation wait for concept approval. An explicit instruction to implement directly overrides this implementation boundary; existing features and confirmed preferences still apply.
- **Implement agreed concept:** Find the actual approved artifacts and decisions in this conversation or project; translate them into acceptance checks and implement them without reopening settled choices. Approval already given remains valid for that scope.
- **Focused improvement:** Address the specified component, workflow, or defect with proportional investigation. Preserve the rest of the product.

Do not turn a scoped request into a full audit. **A requested full audit must inspect every discovered page, component usage, widget, dialog, drilldown level and defined workflow transition in scope.** Representative screens are insufficient. Test each item's relevant states, roles, input and responsive configurations. Shared-component review must be accompanied by checks in every usage context. Reconcile static routes with runtime navigation, overlays, lazy content and permission-dependent surfaces. Track inaccessible or untested items as gaps; do not claim full completion until resolved. A reduced sample is a scope change requiring the user's agreement.

For full audits, maintain the schema-2 inventory and planned obligations from `audit-method.md` before recording results. Link usages to their surfaces/families and transitions to endpoints/workflows. Plan finite, justified behavior classes per entity; do not multiply every global dimension onto every screen. Newly discovered entities, contexts or branches reopen reconciliation. Source inspection cannot close runtime obligations; missing access is blocked, not inapplicable. An approved sample can finish its agreed scope but never completes the original full-audit coverage claim.

## Keep account and access reviews about the experience

Account and access work means reviewing the layout, language, navigation, states and recovery of sign-in, personal settings, roles, API access and related journeys. It is not permission to collect credentials, inspect secret stores, bypass access controls or conduct a penetration test.

Use user-controlled sign-in, an already authenticated session, or authorized synthetic test accounts. Do not ask the user to paste passwords, one-time codes, recovery codes, private keys or live API tokens into the conversation. Do not search password managers, credential files, `.env` secrets, browser cookies or session storage for access. Inspect safe configuration contracts and redacted fixtures instead. If a secret is unexpectedly visible, exclude it from notes, screenshots, prototypes and published artifacts; do not reveal or copy it to prove a design point.

An audit may inspect a form without submitting it. Creating or revoking real credentials, changing real permissions, sending test webhooks/messages, ending sessions or deleting data is a consequential product action, not implicit audit authorization. Exercise those paths only with explicitly authorized actions and safe fixtures. Missing access remains a recorded gap. Backend security enforcement is a dependency to identify, not a security certification this design skill can supply.

## Establish the product contract

Read project instructions, the existing design system and component library, supported browsers, app routes, localization, available tests, and any approved designs. Identify the users, their main tasks, roles, platform constraints, and current data states. Before allocating layout space, establish the application’s purpose, primary unit of work, operating conditions and observable success criteria using [product-thinking.md](references/product-thinking.md). Require a task reason for each persistent region; explore hiding secondary chrome when useful without hiding critical state or the return path. Distinguish evidence from assumptions. Ask only for missing decisions that materially affect the result; continue independent work while waiting.

For a substantial concept, cover at least **twenty distinct, product-specific preference questions early**, and more whenever an unresolved decision materially affects the result, before committing to a visual direction. Carry forward already confirmed answers without re-asking them; ask the remaining questions in digestible batches. Record explicit delegation if the user waives the remaining interview. Do not pad the count with discoverable facts, apply it to a narrow fix, or turn unanswered optional preferences into an approval gate. Use the [design brief](assets/design-brief.template.md) and distinguish confirmed answers, pending preferences and hypotheses.

During audits as well as concept work, ask as many focused questions as necessary to resolve material uncertainty about meaning, work practices and direction. Offer reasoned choices that distinguish applicable requirements, established vendor patterns and taste. Reuse confirmed answers; keep a decision queue and continue independent inspection while dependent conclusions remain provisional. An audit has no arbitrary question quota or ceiling. Follow [discovery-and-preferences.md](references/discovery-and-preferences.md).

Establish the company/product brand and the authority of supplied guidelines or assets. Ask how much to inherit separately for typography, colors, shapes, icons, imagery, voice, layout/navigation, motion and materials. Record preserve/evolve/reinterpret/explore decisions with concrete limits in the [brand inheritance matrix](references/brand-discovery.md); do not infer that keeping brand colors also freezes the old layout. Reuse existing answers and authorization.

Remain neutral to design language. When the user chooses a vendor language, company identity or visual reference, follow the [reference research and translation method](references/brand-discovery.md#research-the-selected-language-for-this-project): investigate current primary guidance and actual examples, derive project-specific rules, demonstrate them with real task content, and verify every affected usage. Do not inherit a previous project's palette, material, typography or platform generation. Keep research evidence project-local under [project-research.md](references/project-research.md); publish original methods rather than provider catalogues or copied source material.

Discover existing role/admin visibility, supported languages, light/dark/system choices, density preferences, graphs and operational thresholds relevant to the requested scope. For design or implementation, maintain an [old-to-new feature map](assets/feature-map.template.md) covering that scope plus all transitively affected shared usages and dependencies. A full-product redesign maps every discovered capability, including those outside its current prototype. A focused fix maps its affected capabilities without turning unrelated areas into a product-wide design task. Preserve behavior and supported variants unless specifically changed. A general aesthetic approval does not authorize feature loss; retirement requires an actual user decision identifying the affected capability and consequences. Audit-only work records the current baseline and coverage; it does not require proposed destinations or a redesign map.

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
| Existing functions, old-to-new mapping, role/theme/locale/density and chart parity | [feature-parity.md](references/feature-parity.md) |
| Concept, alternatives, refinement, approval, exact implementation | [concept-to-code.md](references/concept-to-code.md) |
| User goals, information architecture, usability evidence | [product-thinking.md](references/product-thinking.md) |
| Hidden work, confusing navigation, incomplete primary tasks, live investigation and return | [task-flow-design.md](references/task-flow-design.md) |
| Layout, hierarchy, color, type, shapes, iconography, motion, tokens | [visual-systems.md](references/visual-systems.md) |
| Component anatomy, interaction states, selectors, messages, icons and consistent dialog/drawer families | [component-states.md](references/component-states.md) |
| Navigation hierarchy, overloaded settings, panels, selected materials, shape and motion | [navigation-and-materials.md](references/navigation-and-materials.md) |
| Desktop/tablet/phone, input modes, navigation and adaptation | [platform-adaptation.md](references/platform-adaptation.md) |
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
| Behavioral, visual, accessibility and concept-conformance checks | [verification.md](references/verification.md) |
| Skill evaluation, regression evidence, maintenance | [skill-evaluation.md](references/skill-evaluation.md) |
| Current project research, reference authority, freshness and private evidence | [project-research.md](references/project-research.md) |

## Execute with traceability

1. **Discover.** Establish scope, related inventory, critical journeys, existing conventions, and test access. For substantial concepts, complete the early preference record and feature map for the requested scope and its affected dependencies before developing the direction. For an audit, reconcile the current inventory, entity/context obligations and interaction graph using `audit-method.md`; do not invent a proposed design to complete discovery. Done when known surfaces and usages in scope are accounted for, obligations are planned and inaccessible areas remain explicit gaps.
2. **Observe.** Exercise the planned journeys and behavior classes with actual roles, sizes and adverse states. Match evidence to its method, revision, environment and context. Link data-changing transitions to the UI/API response and persistence contract. Screenshots alone cannot establish behavior or authorization. Done when planned checks have appropriate evidence or explicit unresolved status; a defect report alone does not finish audit coverage.
3. **Decide.** For audit-only work, deliver ranked findings. For design work, use the concept workflow and approval boundary: express important decisions as component, layout, state, and workflow contracts; show old/new navigation and explain feature moves, retained variants and prototype omissions within the mapped scope. Done when the requested decision artifact is concrete enough to review, not merely adjectives or a mood board.
4. **Implement when authorized.** Reuse or improve shared primitives before repeating fixes across screens. Make a complete thin slice of a real journey, verify it, and propagate the agreed rules. Track contract IDs to code and checks. Done when the agreed scope is implemented and remaining dependencies are visible.
5. **Verify.** Compare the implementation to its baseline, agreed concept, target tasks, and applicable requirements, including mapped features and relevant role/theme/locale/density variants. Separate code inspection, automation, visual inspection, manual interaction, and actual user research. Done when the evidence supports the claims and remaining failures are reported.

Delegation can split independent surfaces or specialist passes. Give each worker the same scope and approved contract. Reconcile conflicting recommendations before reporting or implementing them. Do not allow independent agents to invent competing token systems.

## Quality rules that apply throughout

- Treat loading, empty, error, success, offline, denied, partial, stale, and interrupted states as conditional product behavior, not decorative variations. Cover the ones the feature can reach.
- Adapt to usable space, content, input capability, and user preferences. “Mobile” is not simply a scaled-down desktop screenshot.
- For every decision-bearing metric, table, chart, widget and drill path in scope, verify meaning, useful exploration/action and cross-surface consistency in distinct passes. Unknown domain definitions remain gaps; proposed filters, comparisons or actions need a stated user benefit and data/permission dependencies. Established patterns are candidates, not mandatory features for every product.
- Check visual craft and task performance separately. A polished screen can still be confusing; a usable screen can still need typographic and compositional refinement.
- Propagate confirmed design decisions to every affected usage and relevant context, with rendered evidence or explicit gaps. Review work/preservation, composition, information economy and interaction/adaptation in separate passes, then verify corrections on the latest artifact as specified in [concept-to-code.md](references/concept-to-code.md). A token, specimen or single successful screen is not proof of global consistency.
- Before presenting a substantial concept as ready, walk its critical tasks from a visible entry through real proposed detail, outcome and return using [task-flow-design.md](references/task-flow-design.md). A feature-map entry, dead button or placeholder does not establish a working journey. Keep the original full scope and unfinished branches visible. Translate feedback into a concrete change and fresh rendered evidence; preserve the owner's rejection until resolved.
- Accessibility needs semantic implementation and manual checks as well as automated scans. Client-side permission visibility does not establish server-side authorization.
- Label statements as standards, vendor guidance, research/heuristics, product decisions, or hypotheses when the distinction affects a recommendation. “Latest” and “best for this user” are different claims.
- Inspect visual changes on their actual delivery surface as described in [verification.md](references/verification.md), including surrounding content, visible name/version consistency, spacing and the selected responsive asset at the inspected revision. Size checks to the actual content column and affected variants. If that surface is unavailable, inspect the strongest available preview and state the limit; code/CI passes do not establish visual acceptance. Never invent screenshots, tests, scores, usage data, or user approval.
- Keep user data and secrets out of evidence artifacts. Use safe test fixtures for destructive or externally consequential journeys.

## Deliver the result

Use the smallest useful package for the mode: an audit with coverage and prioritized findings; a concept with its preference brief, feature map, visual and interaction artifacts plus open decisions; or an implementation with conformance and parity evidence and remaining gaps. Link artifacts and name what is ready for the next decision.

For full audits, and scoped audits where a ledger is useful, copy [audit.template.json](assets/audit.template.json) and follow the schema-2 format in `audit-method.md`. Run `python3 scripts/audit_coverage.py PATH --require-complete` from this skill directory. Separate valid records, agreed scope reviewed, original full scope reviewed and checks passed; percentages concern planned checks only. Version-1 ledgers require migration and fresh reconciliation. The script validates self-declared records; it cannot inspect the app, authenticate evidence, establish discovery completeness or certify UX/security. The [design contract template](assets/design-contract.template.md) records approved concepts.

For version-dependent APIs, browser support, identity rules, or a claim about the newest platform guidance, verify the current primary source before applying it. Maintain project-specific decisions in the project; change this reusable skill only when the user requests an update.
