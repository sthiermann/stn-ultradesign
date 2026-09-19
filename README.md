# STN Ultradesign

<p>
<picture>
  <source media="(max-width: 1000px)" srcset="assets/brand/hero-compact-a0752e694d.svg">
  <img src="assets/brand/hero-14faef40a2.svg" alt="STN Ultradesign. Design the whole experience. Product-specific design across desktop, tablet and phone." width="1280">
</picture>
</p>

**AI UI/UX design skill for Codex and Claude Code.**

Turn an application into a coherent product experience. STN Ultradesign gives your coding agent a complete design workflow: understand the product, audit its interface, develop a distinctive interactive concept, and verify implementation against the agreed design.

Bring your brand. Set the direction. Review the experience before it ships. Use it to redesign existing software, shape a new product or improve one focused workflow across desktop, tablet and mobile.

[**Explore the interactive website →**](https://sthiermann.github.io/stn-ultradesign-website/) · [Install the skill](docs/installation.md) · [Start a redesign](#put-it-to-work) · [Explore the workflow](#a-complete-path-from-requirements-to-delivery) · [Read the skill](skills/stn-ultradesign/SKILL.md)

Release **v0.8.0** · [MIT license](LICENSE) · Codex + Claude Code

[![Package checks](https://github.com/sthiermann/stn-ultradesign/actions/workflows/validate.yml/badge.svg)](https://github.com/sthiermann/stn-ultradesign/actions/workflows/validate.yml)

## What your redesign gains

- **A direction that belongs to your product.** Your brand, preferences and chosen references become shared rules for layout, typography, color, components and motion.
- **Guided decisions, at your pace.** Questions include a reasoned recommendation and its tradeoff. One active question or agreed small batch keeps your answers connected to the work.
- **A clear place for existing capabilities.** A feature map connects current actions, role-specific controls and workflows to their proposed destinations. Unresolved coverage stays visible.
- **An experience you can review.** Interactive concepts expose navigation, editing, menus, data, drilldowns and recovery paths across relevant devices and states.
- **A design that carries into the code.** Accepted decisions guide frontend implementation; separate review and verification check the result against those decisions.

Built for the complexity of business applications: dashboards, settings, tables, charts, permissions, account flows and more. Apply the workflow to HTML, CSS, React and other frontend stacks while working with the project's existing architecture. The skill follows the language of your request.

## Put it to work

[Install for Codex or Claude Code](docs/installation.md), open your application project and start a new task. Use this prompt for an audit followed by a complete redesign concept:

> $stn-ultradesign Audit the entire frontend of this existing application using its current source code and running interface. Ask me about my requirements and design preferences, preserve existing capabilities, and develop a complete interactive design concept. Clarify which earlier design decisions still apply. Independently review and refine the concept with me. Implement production changes only after my approval.

In Claude Code, replace `$stn-ultradesign` with `/stn-ultradesign:stn-ultradesign` after plugin installation, or `/stn-ultradesign` for an individual skill installation.

<details>
<summary>More starting points: audit only, concept, or implementation</summary>

**Audit only**

> $stn-ultradesign Audit the entire frontend. Inventory every page, component usage, widget, drilldown, workflow and relevant state. Prioritize findings with evidence and preserve unresolved coverage as gaps.

**Develop a complete design concept**

> $stn-ultradesign Develop a design concept for this application. Clarify requirements and preferences, establish a creative direction, build the system and components, and render the complete concept. Have it independently reviewed, refine it with me, and obtain my acceptance of the specific scope before production implementation.

**Implement an accepted design**

> $stn-ultradesign Implement the accepted concept. Trace the changes to its design decisions and verify behavior, accessibility and visual fidelity.

</details>

Starting fresh? Follow the [new design review instructions](docs/installation.md#start-a-new-design-review). Previous concepts do not need to be deleted. Public package documentation is English.

## A complete path from requirements to delivery

<p>
<picture>
  <source media="(max-width: 1000px)" srcset="assets/brand/method-compact-65eb6420ab.svg">
  <img src="assets/brand/method-11693d013f.svg" alt="Requirements → Creative direction → System and components → Complete concept → Independent review → Human acceptance → Implementation → Verification. Review and refine before scoped acceptance; verify the implemented result." width="1280">
</picture>
</p>

Substantial concept, design-system and redesign work follows a connected sequence. Each stage produces decisions that the next stage can use and check.

| Stage | What you receive |
| --- | --- |
| **1. Requirements** | A traceable record connecting your requests, preferences and product constraints to affected capabilities and observable acceptance criteria. |
| **2. Creative direction** | A researched interpretation of your chosen identity, a product-specific visual thesis and structural alternatives where the direction remains open. |
| **3. System & components** | Shared visual and interaction rules, demonstrated with demanding content, open controls and relevant states before the pattern expands. |
| **4. Complete concept** | A rendered, reviewable experience covering the agreed views, core journeys, device sizes, difficult content and recovery paths. |
| **5. Independent review** | A separate critical review of requirements, visual craft, usability, consistency, preserved capabilities and available evidence. Findings feed into revision. |
| **6. Human acceptance** | Your acceptance of a specific concept revision, scope, decisions and known gaps, recorded in a design contract. |
| **7. Implementation** | Frontend changes traced to accepted layouts, components, behavior and acceptance criteria. |
| **8. Verification** | Observed checks of behavior, accessibility, responsiveness and visual fidelity, with remaining gaps stated plainly. |

The [delivery workflow](skills/stn-ultradesign/references/delivery-workflow.md) makes those handoffs explicit. Existing acceptance remains valid for its agreed scope. An explicit request to implement directly takes precedence. Focused fixes use proportionate checks; audit-only work delivers findings and coverage without requiring a concept or implying approval to redesign.

## Choose the starting point

| Your task | The skill's focus |
| --- | --- |
| **Audit the entire frontend** | Reconcile the inventory, inspect all usages and journeys in scope, prioritize findings and preserve unresolved coverage as gaps. |
| **Develop a design concept** | Establish requirements and preferences, explore a direction, build the component system, render the concept and refine it through review. |
| **Build or evolve a design system** | Translate the product's identity and tasks into coherent tokens, components, states and usage rules. |
| **Implement an accepted concept** | Preserve the agreed decisions and capabilities, then verify the implemented result. |
| **Improve one component or flow** | Trace affected usages and dependencies, make the bounded change and check its consequences. |

## Your product defines the direction

A monitoring workspace needs useful image coverage and fast exception detection. An editor needs room to work. An administrative change needs clear consequences and recovery. The skill establishes the main task, meaningful unit of work and operating conditions before allocating screen space.

Substantial concept work covers **at least 20 meaningful preference questions** tailored to the product, including answers you have already given. Questions arrive one at a time or in an agreed small batch, with a recommendation, its basis and its tradeoff. Further questions address material unknowns as they emerge. The brief covers character, density, hierarchy, typography, color, shape, motion and device behavior. It distinguishes your preferences from product constraints and applicable standards.

Existing identity becomes a deliberate input. Decide what to preserve, evolve or replace across typography, palette, shapes, icons, imagery, voice, layout, motion and materials. Those boundaries carry into the component system and design contract. See [discovery and preferences](skills/stn-ultradesign/references/discovery-and-preferences.md) and [brand discovery](skills/stn-ultradesign/references/brand-discovery.md).

## Your requirements stay connected to the result

Every consequential request follows a traceable path: **your intent → a scoped decision → affected components and journeys → observable checks → current evidence**. A requirement can be recorded without being satisfied. The skill keeps concept coverage, implemented behavior and verified outcomes distinct.

When you choose a design language, the skill investigates its relevant platform and generation, component families, visual rules and interactions. It records what was read, visually inspected or actually exercised, then translates those findings into project-specific rules. Difficult examples test the interpretation before it spreads. Final review follows every affected usage in the agreed scope.

Changing a decision reopens the checks that depend on it. Existing answers remain valid elsewhere. Missing evidence, untested behavior and proposed exceptions stay visible; a broad approval or a successful code check cannot silently close them. Concrete reference research stays with your project, outside this reusable package.

Explore [requirements and conformance](skills/stn-ultradesign/references/requirements-conformance.md) and [reference research](skills/stn-ultradesign/references/project-research.md).

For work spanning sessions or contributors, [bounded work items](skills/stn-ultradesign/references/delivery-workflow.md#execute-bounded-work-items) connect decisions, concept or implementation tasks, and verification. Each has an outcome, dependencies, an owner and precise acceptance criteria checked against actual results. Completed decisions stay distinct from completed features; unresolved work remains visible when the design changes. Local Markdown is the default, with existing design records or an explicitly required tracker reused. No tracking-service setup is required.

## Visual craft belongs in the system

A coherent experience needs more than attractive isolated screens. The skill connects composition, hierarchy, rhythm and density to the user's next decision. Where a structural decision remains open, alternatives use the same task and content so their consequences are visible.

Buttons, fields, selectors, switches, menus, badges, messages and icons receive a consistent anatomy and the states their tasks require. Focus, hover, selection, pending work, errors and state combinations must remain understandable. Interaction checks compare the whole visible action surface with what actually responds, including labels, icons, padding and edges. Spatial review includes resting, expanded and transitioning states. Shared rules connect surfaces without forcing a dense workspace, a permissions editor and an API reference into the same layout.

Rendered concepts undergo [layout stress checks](skills/stn-ultradesign/references/layout-integrity.md): long text, wrapping buttons, constrained containers, open overlays, zoom and changing content. Checks distinguish intentional scrolling or layering from clipped content and blocked actions. Results stay tied to the actual usage, conditions and revision. Visual criticism and revision remain part of the work; an automated check does not establish aesthetic acceptance. See [visual systems](skills/stn-ultradesign/references/visual-systems.md) and [component states](skills/stn-ultradesign/references/component-states.md).

## Complete tasks, preserve capabilities

Every critical task needs a discoverable path from entry to useful action, object and context, outcome and return. Opening a detail should preserve enough context to resume the work. Navigation, local views, commands and independent overlays have different jobs and receive appropriate interactions.

A redesign maintains an **old → new feature map**. It accounts for affected capabilities, role access, behavior, states and destinations, including toolbar overflow, object menus, edit modes, saved preferences and simultaneous panels. Moving a capability requires a usable new home; dropping one requires an agreed scope change.

Existing themes, supported languages, density options, charts and graph types remain part of that mapping. A full-product redesign covers every discovered capability. A focused change covers its requested scope plus affected shared usages and dependencies. See [task-flow design](skills/stn-ultradesign/references/task-flow-design.md) and [feature preservation](skills/stn-ultradesign/references/feature-parity.md).

## Make data understandable and actionable

For dashboards, tables, charts and widgets, the skill examines what each value means: definition, unit, population, timeframe, aggregation, comparison and freshness. Missing data must remain distinguishable from zero. Status colors need an explainable rule.

Review checks whether widgets serve a distinct purpose, repeat information usefully or should share an implementation. Drilldowns are followed from the clicked record through effective filters to actual included and excluded data, visible scope and return. A correct filter label alone is not a passing result. Filters, comparisons, explanations and drilldowns should help people make the actual decision. Uncertain domain meaning stays explicit and becomes a focused question. See [analytical meaning](skills/stn-ultradesign/references/analytical-meaning.md).

## Evidence you can follow

A full audit covers every discovered page, component usage, widget, dialog, drilldown and defined relevant workflow, state and transition in scope. Large products are covered in resumable batches. Inaccessible areas stay visible as gaps; sampling requires an agreed scope change.

The package includes templates for requirements, briefs, reference translation, feature maps, task flows, design contracts and audit evidence. Its local Python coverage validator checks the consistency of a declared audit inventory, obligations and evidence. A separate [delivery checker](skills/stn-ultradesign/references/delivery-ledger.md) connects requirements, decisions, stage obligations, artifacts and observed runs. It detects stale bindings and can verify explicitly listed local evidence files. Both check the supplied records; neither inspects the application automatically or certifies observation truth, discovery completeness, design quality or security.

Comprehension review compares what a widget or control communicates before activation with its actual scope, result and recovery. Loading, background refresh, failure and success are checked as behavior. Geometric and motion review includes alignment, optical balance and complete transition cycles where relevant.

Independent review challenges the current artifact against the requirements and design intent. It uses a separate reviewer when the host supports one; otherwise, self-review is identified as such and the limitation remains explicit. Human acceptance records the revision and scope that may proceed. Verification then checks the implementation itself. See [verification](skills/stn-ultradesign/references/verification.md).

## Package and privacy

The package contains the skill, its reusable references and templates, local validators, automated checks and installation metadata. It configures no hooks, telemetry, MCP servers or external services. The skill instructions, templates and code are covered by the [MIT License](LICENSE). The ST monogram and branded presentation assets have a separate [brand rights notice](assets/brand/LICENSE).

Account, access, messaging and administrative reviews examine interfaces and user journeys. Use an already authenticated session, user-completed sign-in or authorized test data. An audit does not authorize collecting secrets, changing real permissions or sending messages. Project-specific evidence stays with the user's project. See [privacy and audit scope](PRIVACY.md).

Created by [Sven Thiermann](https://github.com/sthiermann). [Contributing](CONTRIBUTING.md).
