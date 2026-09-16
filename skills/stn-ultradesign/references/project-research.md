# Research the current project

Use when a design depends on a selected reference language, platform generation, unfamiliar workflow or unresolved implementation constraint. Study the applicable system, translate its relationships into the target product, then prove the consequential choices in rendered tasks. This is an original research method, not a reference catalogue or a design preset.

Keep one project evidence record using the [reference translation template](../assets/reference-translation.template.md) when the scope warrants it. A focused component may need only a few linked notes; a substantial reference-led concept needs the coverage and proof described below. Reuse the [requirements register](requirements-conformance.md), brand inheritance decisions, component contracts and usage inventory rather than maintaining competing copies.

## 1. Bound the study and expose unknowns

Record the user's chosen language and exact requested generation, reference products and device families, separately from the implementation's operating system, browser/runtime and supported versions. Preserve a requested older generation. A current publication can explain an older system without making its newer examples applicable. Where the generation is unspecified, establish an evidence-based working interpretation and mark its decision status; research alone does not create user approval.

Link the applicable requirement IDs and [selective inheritance decisions](brand-discovery.md#3-choose-inheritance-separately-for-each-dimension). Identify which visual, structural and behavioral qualities the user values and the limits on changing each. Existing identity, feature and role requirements still govern the translation. A prior project's chosen palette, material or layout contributes no default.

Build a small applicability inventory from the target product's tasks and affected component families. Include foundations and relationships that can change those tasks: navigation and containment, typography and symbols, color roles, geometry and insets, material/depth, state semantics, motion and platform adaptation. Add specialized surfaces only when in scope. For each topic/family, record:

- **Applicability:** required, conditional with its trigger, or excluded with a reason; link affected requirements and usages.
- **Evidence coverage:** prose, visual examples, actual kit contents, demonstration playback and hands-on interaction. Mark each independently with artifact IDs and conditions, even when one table cell groups related methods.
- **Open consequence:** what remains unknown, what decision it could change, and the next inspection or question that can resolve it.

Distinguish an unresolved product requirement from an uncertain reference fact. Resolve discoverable facts through inspection. Carry consequential unanswered requirements into the master register; ask only for decisions that evidence and existing instructions cannot settle. Continue independent work while the dependent conclusion remains provisional. Optional taste can remain a reversible proposal.

**Complete this step when** every relevant family and inherited dimension has an applicability decision, linked requirements and an inspection plan; material unknowns have a stated consequence. The inventory is a bounded study plan, not a whole-product audit or an indiscriminate combination of all contexts.

## 2. Inspect primary evidence beyond the overview

Start with applicable first-party guidance and follow its relevant links into component pages, implementation notes, accessibility guidance, platform differences, release changes and design resources. Open the sections needed to answer the inventory's questions. A landing page or resource listing establishes discoverability, not the contents of its linked pages or kit.

Inspect actual visual specimens as well as prose. Where a component kit is relevant and available, open the kit and inspect the pertinent components, variants, nested parts, states and constraints. Record its independent version and inspected contents. File availability, preview thumbnails and image descriptions do not establish kit inspection. If access or tools prevent it, record the missing evidence and continue with available sources without relabeling them.

For behavior or motion claims, operate an authorized instance, run a safe sample, or inspect an available demonstration sequence. Record initial state, trigger/input, transition, result, dismissal/return and interruption behavior where consequential. A video can demonstrate a transition but does not establish keyboard or assistive-technology behavior unless that behavior was actually inspected. Mark transcripts, isolated frames and playback separately. Use safe fixtures within the existing authorization.

Maintain a private source registry with stable IDs such as `SRC-01`: precise locator/section or kit element, authority, applicable generation/platform, publication/update date, inspection date, actual inspection method and evidence artifact. Keep kit version, runtime/build and source update date distinct. A live guidance page can contain older examples and contradictory sections.

For conflicting sources, compare authority, scope, version and observed conditions. Distinguish a normative requirement, documented implementation behavior, observed example and stylistic suggestion. Preserve both claims and explain the chosen interpretation or unresolved conflict. The newest date alone does not win; a target-specific release change may supersede an older example while leaving its underlying principle applicable. A reference cannot silently override a confirmed product requirement.

Evidence supports particular claims, not a universal confidence score. Prose supports stated guidance; an inspected kit supports the examined specimen; runtime inspection supports observed behavior under recorded conditions. Search snippets, summaries and alt text remain discovery or textual evidence. Exact measurements need a documented value, kit reading or controlled measurement; identify estimates as estimates. A screenshot cannot establish timing, live accessibility, performance or all responsive behavior.

**Complete this step when** the planned applicable sources and linked details have been inspected, each coverage dimension is reconciled to evidence or an explicit gap, and conflicts have a supported resolution or an open consequence. Unavailable evidence is a gap, not an exclusion. Report “study with gaps” when a consequential claim still lacks the evidence it needs.

## 3. Translate relationships into project rules

Assign stable IDs to derived rules, for example `REF-01`, and link each to the existing requirement IDs, source observations, affected families/usages and acceptance checks. Separate what was observed from what the project infers or deliberately changes. Keep the full requirement and component contract in their authoritative records; the research record supplies evidence and translation rationale.

Describe relationships and purpose before isolated values: how content and controls are separated; which visual states indicate selection versus focus; how a nested contour relates to its inset; what prominence means within a task; how navigation preserves context. Translate these into semantic token roles, composition and behavior within the agreed inheritance limits. A single color, corner radius or effect cannot stand in for a language.

For each affected family, link or complete its [component contract](component-states.md). Include the parts and their hierarchy, content slots, semantic role/value/action, visible and hit geometry, enabled/selected/focused distinctions, state transitions, keyboard/pointer/touch behavior and relevant adaptation. Record only reachable states and relevant contexts. Similar silhouettes do not make a command, single selection, multiple selection and immediate setting semantically equivalent.

State the native/web boundary for each consequential translation: what can be preserved, what the target platform supplies, what is an approximation, and what needs a fallback. System rendering, text metrics, native menus, window behavior, input feedback and adaptive materials can depend on unavailable platform services. Specify an achievable acceptance condition in the actual runtime. Preserve semantics, task continuity and accessibility while testing the proposed visual approximation; resemblance alone does not establish native equivalence.

**Complete this step when** every adopted reference relationship has a rule ID, supporting evidence or explicit hypothesis, a linked requirement/contract, and an observable acceptance condition. Unresolved conflicts and departures stay visible. A materially unanswered requirement prevents declaring the dependent translation settled, not continuing unrelated research or isolated experiments.

## 4. Prove consequential choices before expansion

For a substantial unsettled direction, render a primary work surface, linked detail and consequential component state or transition. Use the same task, role, domain content and capability mapping for the proposed direction and its strongest plausible structural alternative. Compare only open choices; preserve settled decisions. A narrow repair needs the affected component in its real surrounding task, not a new direction study.

Make comparisons reproducible: record artifact revision, target runtime/build, viewport or window size, scale/zoom, loaded fonts, theme, locale, content, input and active accessibility preferences relevant to the claim. Match reference and product conditions where possible and disclose mismatches. Compare meaningful relationships and task behavior; state measurable tolerances only where evidence and the agreed goal support them.

Choose proof cases to expose the important uncertainties: long labels or numbers, nested surfaces, busy backgrounds, changed selection, expanded controls, resizing or interrupted motion as applicable. If type or proportion remains open, compare matched titles, values, field/error text and actions at the smallest relevant layout or enlarged text. Verify actual font loading and wrapping. Inspect transitions as sequences, including reduced-motion behavior when relevant; a still render cannot close a movement question.

Review visual fidelity, task fit and interaction/accessibility separately. Record findings by rule and acceptance ID, revise the artifact and inspect the changed result. Keep the user's assessment distinct from technical observations. An unresolved rejection requires a revised artifact and a resolved review finding; new documentation alone cannot close it.

**Complete the experiment when** each consequential hypothesis has been tested in its stated conditions and its result, decision status and remaining gaps are explicit. A falsified hypothesis finishes an experiment, not readiness to expand. Correct or replace the affected rule within existing authority and obtain passing required proof before propagating it. Continue independent work where its own prerequisites are satisfied. Passing the proof establishes readiness for those patterns within existing authorization, not approval by implication or final coverage of the product.

## 5. Carry rules through every affected usage

Connect accepted rules and family contracts to the existing bounded usage plan or full audit ledger. Follow [brand propagation](brand-discovery.md#propagate-decisions-to-every-affected-usage) and [verification](verification.md) for every affected page, component occurrence, nested control and reachable relevant context. Early representative proofs do not replace this final per-usage verification.

**Complete the scoped translation when** requirements, rules, affected usages and acceptance evidence reconcile at the delivered revision. Keep mapped, depicted, implemented and rendered-verified coverage separate. New usages, changed rules or relevant contexts reopen affected checks. Disclose blocked and untested cases, approximations and unresolved decisions; claim only the fidelity and behavior demonstrated in the agreed scope.

## Keep evidence separate from publication

Store source names, URLs, captures, exact source facts and project-specific recipes in the target project's private working evidence unless its owner explicitly requests a research report. This reusable package contains only independently written methods and blank templates: no named inspiration lists, provider catalogues, external reference URLs or copied skill instructions, source text, kits, code or artwork. Use original implementations and authorized assets; preserve required attribution or license notices for any legitimately included dependency. A reference's visibility is not permission to reuse its assets.
