---
name: stn-ultradesign
description: Audit application UI/UX, develop and refine reviewable design concepts, and implement approved designs faithfully across desktop, tablet, and mobile. Use for substantial frontend design reviews, workflow redesigns, design-system work, and concept-to-code projects; a small unrelated code fix does not trigger a whole-product audit.
---

# STN Ultradesign

Turn observed user needs into coherent interfaces and complete workflows. Produce evidence, a reviewable design, and verified behavior. Match the user's language in discussion and deliverables. The reference material is in English; that does not set the product's language.

## Select the work mode

- **Audit:** Inspect the requested scope, produce findings and coverage. An audit request alone does not authorize a redesign.
- **Concept first:** For a new design or substantial redesign, present a concrete concept, refine it with the user, then implement the approved version. This is the owner's preferred default for substantial design changes. Read [concept-to-code.md](references/concept-to-code.md) before making concepts. Preparation, research, and isolated prototypes can proceed before approval; changes to the production implementation wait for concept approval. An explicit instruction to implement directly overrides this default.
- **Implement agreed concept:** Find the actual approved artifacts and decisions in this conversation or project; translate them into acceptance checks and implement them without reopening settled choices. Approval already given remains valid for that scope.
- **Focused improvement:** Address the specified component, workflow, or defect with proportional investigation. Preserve the rest of the product.

Do not turn a scoped request into a full audit. **A requested full audit must inspect every discovered page, component usage, widget, dialog, drilldown level and defined workflow transition in scope.** Representative screens are insufficient. Test each item's relevant states, roles, input and responsive configurations. Shared-component review must be accompanied by checks in every usage context. Reconcile static routes with runtime navigation, overlays, lazy content and permission-dependent surfaces. Track inaccessible or untested items as gaps; do not claim full completion until resolved. A reduced sample is a scope change requiring the user's agreement.

For full audits, maintain the schema-2 inventory and planned obligations from `audit-method.md` before recording results. Link usages to their surfaces/families and transitions to endpoints/workflows. Plan finite, justified behavior classes per entity; do not multiply every global dimension onto every screen. Newly discovered entities, contexts or branches reopen reconciliation. Source inspection cannot close runtime obligations; missing access is blocked, not inapplicable. An approved sample can finish its agreed scope but never completes the original full-audit coverage claim.

## Establish the product contract

Read project instructions, the existing design system and component library, supported browsers, app routes, localization, available tests, and any approved designs. Identify the users, their main tasks, roles, platform constraints, and current data states. Distinguish evidence from assumptions. Ask only for missing decisions that materially affect the result; continue independent work while waiting.

Preserve established vocabulary, brand, working flows, and framework choices unless the requested change justifies replacing them. A familiar control is a useful default when it fits the task. Visual distinctiveness comes from an intentional, product-specific system, not universal bans on a font, color, radius, or layout.

Use this conflict order: explicit product requirements and applicable constraints; verified accessibility/security obligations; approved concept and existing system; task evidence; relevant platform guidance; stylistic preference. If an approved design conflicts with an obligation, expose the conflict and propose the smallest compliant revision; do not silently change either. Verify legal applicability separately rather than inventing it.

## Route to the necessary references

Read only the branches relevant to the current work. For a whole-product audit, cover every applicable branch over successive passes; persist progress rather than loading everything at once.

| Decision or task | Read |
| --- | --- |
| Full audit, coverage, findings, severity, evidence, completion | [audit-method.md](references/audit-method.md) |
| Concept, alternatives, refinement, approval, exact implementation | [concept-to-code.md](references/concept-to-code.md) |
| User goals, information architecture, usability evidence | [product-thinking.md](references/product-thinking.md) |
| Layout, hierarchy, color, type, shapes, iconography, motion, tokens | [visual-systems.md](references/visual-systems.md) |
| Desktop/tablet/phone, input modes, navigation and adaptation | [platform-adaptation.md](references/platform-adaptation.md) |
| Forms, wizards, settings, search, editing, asynchronous flows | [workflows.md](references/workflows.md) |
| Authentication, sessions, permissions, roles, organizations | [identity-permissions.md](references/identity-permissions.md) |
| Personal/org/project settings, invitations, roles, billing and governance | [business-administration.md](references/business-administration.md) |
| API credentials, service accounts, webhooks and OpenAPI documentation | [developer-platforms.md](references/developer-platforms.md) |
| Keyboard, screen reader, zoom, touch, contrast, WCAG distinctions | [accessibility.md](references/accessibility.md) |
| Charts, dashboards, widgets, tables, network graphs | [data-visualization.md](references/data-visualization.md) |
| HTML/CSS/React, state, performance, component engineering | [web-engineering.md](references/web-engineering.md) |
| Behavioral, visual, accessibility and concept-conformance checks | [verification.md](references/verification.md) |
| Skill evaluation, fair comparison, maintenance | [skill-evaluation.md](references/skill-evaluation.md) |
| Source authority, freshness, research provenance | [sources.md](references/sources.md) |

## Execute with traceability

1. **Discover.** Establish scope, related inventory, critical journeys, existing conventions, and test access. For an audit, reconcile inventory sources, entity/context obligations and the interaction graph using `audit-method.md`. Done when known surfaces and usages are accounted for, obligations are planned and inaccessible areas remain explicit gaps.
2. **Observe.** Exercise the planned journeys and behavior classes with actual roles, sizes and adverse states. Match evidence to its method, revision, environment and context. Link data-changing transitions to the UI/API response and persistence contract. Screenshots alone cannot establish behavior or authorization. Done when planned checks have appropriate evidence or explicit unresolved status; a defect report alone does not finish audit coverage.
3. **Decide.** For audit-only work, deliver ranked findings. For design work, use the concept workflow and approval boundary. Express important decisions as component, layout, state, and workflow contracts. Done when the requested decision artifact is concrete enough to review, not merely adjectives or a mood board.
4. **Implement when authorized.** Reuse or improve shared primitives before repeating fixes across screens. Make a complete thin slice of a real journey, verify it, and propagate the agreed rules. Track contract IDs to code and checks. Done when the agreed scope is implemented and remaining dependencies are visible.
5. **Verify.** Compare the implementation to its baseline, agreed concept, target tasks, and applicable requirements. Separate code inspection, automation, visual inspection, manual interaction, and actual user research. Done when the evidence supports the claims and remaining failures are reported.

Delegation can split independent surfaces or specialist passes. Give each worker the same scope and approved contract. Reconcile conflicting recommendations before reporting or implementing them. Do not allow independent agents to invent competing token systems.

## Quality rules that apply throughout

- Treat loading, empty, error, success, offline, denied, partial, stale, and interrupted states as conditional product behavior, not decorative variations. Cover the ones the feature can reach.
- Adapt to usable space, content, input capability, and user preferences. “Mobile” is not simply a scaled-down desktop screenshot.
- Check visual craft and task performance separately. A polished screen can still be confusing; a usable screen can still need typographic and compositional refinement.
- Accessibility needs semantic implementation and manual checks as well as automated scans. Client-side permission visibility does not establish server-side authorization.
- Label statements as standards, vendor guidance, research/heuristics, product decisions, or hypotheses when the distinction affects a recommendation. “Latest” and “best for this user” are different claims.
- Inspect rendered results when a browser or renderer is available. If execution is unavailable, deliver a code-based review and state the limit. Never invent screenshots, tests, scores, usage data, or user approval.
- Keep user data and secrets out of evidence artifacts. Use safe test fixtures for destructive or externally consequential journeys.

## Deliver the result

Use the smallest useful package for the mode: an audit with coverage and prioritized findings; a concept with visual and interaction artifacts plus open decisions; or an implementation with conformance evidence and remaining gaps. Link artifacts and name what is ready for the next decision.

For full audits, and scoped audits where a ledger is useful, copy [audit.template.json](assets/audit.template.json) and follow the schema-2 format in `audit-method.md`. Run `python3 scripts/audit_coverage.py PATH --require-complete` from this skill directory. Separate valid records, agreed scope reviewed, original full scope reviewed and checks passed; percentages concern planned checks only. Version-1 ledgers require migration and fresh reconciliation. The script validates self-declared records; it cannot inspect the app, authenticate evidence, establish discovery completeness or certify UX/security. The [design contract template](assets/design-contract.template.md) records approved concepts.

Research snapshot: 2026-09-16. For version-dependent APIs, browser support, identity rules, or a claim about the newest platform guidance, verify the current primary source before applying it. Maintain project-specific decisions in the project; change this reusable skill only when the user requests an update.
