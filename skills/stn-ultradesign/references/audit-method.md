# Evidence-based frontend audit

This is an original audit method for this skill. Its inventory and severity conventions are project tools, not international UX standards. Use the other references for the underlying requirements and design decisions.

## Establish the audit boundary

Record application revision, environment, available roles, supported devices/browsers, locales, themes, main tasks, authorized test data and excluded areas. Distinguish production behavior from mocks. Find routes from source, navigation, feature flags, redirects, documentation and the running app; none is a complete inventory alone.

Assign every entity a stable ID. The ledger uses these kinds and relationships:

| Kind | What belongs here | Required relationships beyond ID, name and location |
| --- | --- | --- |
| `surface` | Page, route family, overlay, embedded experience, responsive shell | None; a route family cannot conceal different implementations |
| `component-family` | Shared primitive, composite or explicitly local component | None; identify the implementation in `location` |
| `component-usage` | Every page-context usage and material variant | `surface_id`, `family_id` |
| `widget` | Chart, table, graph or widget with its own data/interaction contract | `surface_id`, `family_id`; a local family is allowed |
| `state` | A reachable view such as expanded detail or save rejection | `surface_id` |
| `workflow` | End-to-end user goal across views and roles | Connect at least one transition through its `workflow_id` |
| `transition` | Drilldown, nested tab, disclosure, menu, context switch, submission, browser return or other defined action | `from_id`, `to_id` referencing surfaces/states, `workflow_id`, `trigger`, `preconditions`, `api` contract |

Map shared components to their usages. A root defect should have one finding linked to every affected use, not dozens of duplicate findings. A representative component test does not automatically prove every usage correct: clipping, order, content and overrides are integration properties.

Done with discovery means every known surface is in the inventory, every visible element belongs to a component family with a recorded usage or a local exception, and dynamic/role-restricted surfaces are explicitly accounted for. Unknown access remains a coverage gap.

### Full-audit traversal contract

When a complete frontend audit is requested, inspect every discovered entity and usage; do not silently replace this with a representative-page review. Build a navigation/interaction graph with nodes for views and states and edges for actions. Traverse every defined reachable transition, including every drilldown level, and reconcile the visited graph against routes, menus, feature flags, component usages, stories/tests and product documentation.

On each page enumerate all visible regions, controls, widgets and links; open relevant menus, tabs, disclosures and non-destructive overlays; inspect revealed content and track where each drilldown leads. Include filtered/empty results, paginated/virtualized views, nested details, breadcrumbs, deep links and return context. Use safe fixtures to exercise consequential actions. If authorization or test data is missing, mark the edge and its target blocked.

Reconcile each toolbar and menu action with its handler, role conditions and reachable states. Include controls revealed by hover/focus, selection, editing or available data. Separate selecting, creating, editing, reordering, configuring and sharing the same object where these exist. Record independent display preferences and allowed simultaneous panels; a main view, on-object overlay and supporting inspector may each have a distinct state contract. Test meaningful coexistence, closing, switching and persistence, not only one panel at a time. For messaging, use [messaging-workflows.md](messaging-workflows.md). An audit records baseline evidence and gaps; proposed destinations are needed only when redesign is in scope.

Give each usage a specific context: a shared button may be correct in isolation and clipped inside one toolbar. Inspect every usage for local layout, content, focus, permission and responsive behavior even when its shared primitive already passed. Repeated data rows can share an implementation-level contract, but inspect meaningful row variants, extremes and custom renderers; distinguish repeated data instances from different UI implementations.

Finite coverage means every discovered implementation surface, relevant state and defined transition, not every possible user-entered string or infinite repetition of a loop. Declare the actual roles/configurations/data boundaries and test interactions between them where they can alter behavior. Discovery is revisited whenever a new branch appears.

## Construct the coverage matrix

Cover the dimensions that can alter the result:

| Dimension | Candidate values |
| --- | --- |
| Role and scope | Signed out, member, administrator, viewer, tenant, object owner; use actual roles |
| Space | Compact, medium, expanded, short height, zoomed/reflow, split pane |
| Input | Keyboard, mouse/trackpad, touch, stylus when relevant, assistive technology |
| State | Initial, loading, populated, empty, filtered empty, error, retry, success, stale, offline, partial, denied |
| Content | Short/long text, unbreakable identifier, many/few rows, missing assets, extremes, locale and RTL |
| Preference | Theme, reduced motion, contrast/forced colors, text size |
| Lifecycle | New user, returning user, interrupted task, expired session, changed permission, concurrent edit |

Build finite behavior classes **per entity**. Record actual values and relevance, reachability constraints, boundaries and why two cases can share one implementation-level check. Equivalence requires the same implementation, guards, data transformation and layout behavior; visual resemblance alone does not establish it. Exercise independently implemented variants and coupled conditions separately. Check allow/deny, own/foreign tenant or object, and permission change/revocation when those boundaries exist. Include supported layout/input variants where behavior changes. Document a dimension as inapplicable rather than multiplying it onto unrelated screens.

For example, 1,000 rows using the same renderer do not require 1,000 separate entities. They do require the meaningful row variants, extreme content and each different renderer. A special administrator toolbar or a mobile replacement renderer creates another case. A bounded set of justified equivalence classes can completely cover the declared implementation model; an unverified assumption of equivalence cannot. There is no requirement to form a global Cartesian product of every browser, role, theme and data value.

Test every reachable class and defined transition in the full scope, working in resumable batches. A reduced or pairwise sample may be proposed when constraints require it, but it changes the scope and needs actual user agreement. Never present it as exhaustive. Pairwise coverage alone is insufficient for permission or irreversible-action risk. Expand the model after discovered coupling or failures.

Plan obligations before recording results. Each obligation binds one entity, one declared context, a specific question and required evidence methods. Results reference obligations and use `not-tested`, `pass`, `fail`, `blocked` or `not-applicable`. A missing result is automatically untested. Mark pass only for the check actually executed. Do not delete blocked obligations or overwrite the original mode to improve coverage.

`not-applicable` means a feature is absent, a state is unreachable by design, or a capability is outside the supported product contract. It requires `na_basis`, a reason and evidence. Missing credentials, tools, fixtures, time or authorization to perform a test are **blocked**, never a factual nonapplicability. An entity/context whose only checks are inapplicable stays unresolved: correct its model with evidence or record an approved exclusion, visibly changing full mode to scoped/sample mode.

Use `assets/audit.template.json` and `scripts/audit_coverage.py` for every full audit; they are optional for a small focused review. A clean ledger establishes record consistency only. The completeness and truth of discovery still require judgment and cross-checking.

### Ledger record format

Schema version 2 deliberately rejects version 1 instead of inheriting its completion claims. Start from the template and populate the following records. Keep actual application data and private evidence inside the audited project's private workspace; the reusable skill contains no real audit results.

1. **Scope:** set `product`, exact `revision`, `environment`, `boundary`, `requested_mode` and `audit_mode` (`full`, `scoped` or `sample`), plus `evidence_level` (`source` or `runtime`). Preserve the original requested mode. A changed mode needs `scope_change_approval`, a reference to actual user agreement. The boundary describes included functionality and supported conditions; a silent narrower boundary is not a valid completion strategy.
2. **Discovery:** reconcile `scope.inventory_sources.source`, `runtime`, `roles-and-flags` and `product-docs`. Each has `status` (`reconciled`, `blocked`, `not-applicable`) and `evidence_ids`; blocked/inapplicable entries need a reason. Inapplicability refers to the agreed review method or a genuinely absent source, not inaccessible application areas. For example, a requested source-only review does not require running navigation; a full runtime audit does. Full runtime discovery needs application runtime evidence. Keep unknown areas in `discovery_gaps`; set `inventory_complete` only after the reconciliation is done.
3. **Contexts:** each record has `id`, `name`, `dimensions` and `coverage_reason`. Dimensions require explicit `role`, `scope`, `state`, `layout` and `input` values; add content, configuration, lifecycle, locale and preference dimensions when relevant. State why a value is inapplicable, such as “no tenant model.” `coverage_reason` explains the class and any evidence-backed equivalence, not simply “representative.”
4. **Plan:** `entity_contexts` assigns `entity_id`, `context_ids` and a relevance `reason`; this is the finite coverage boundary per entity. `obligations` contain `id`, `entity_id`, `context_id`, `question` and `required_methods`. Keep all planned obligations, including those still lacking results. Reconcile the graph, inventory, contexts, applicable specialist passes and obligation list together, reference the reconciliation record in `reconciliation_evidence_ids`, then set `reconciled: true`. A new entity, context, branch or finding that changes the plan reopens reconciliation; record why the plan changed.
5. **Evidence:** records have `id`, `method`, `reference`, `revision`, `environment`, `target` (`application`, `mock`, `prototype`) and `context_ids`. Methods are `source`, `rendered`, `interaction`, `assistive-technology` and `api-observation`. One evidence artifact can cover several checks when it actually records each one. Discovery-only artifacts can have an empty context list. Check evidence must include the check's context, match revision/environment and supply its required methods. References are pointers for a human reviewer, not authenticated measurements. Mock/prototype behavior does not establish application runtime behavior.
6. **Results and findings:** one current `checks` record per obligation, with `id`, `obligation_id`, `status` and `evidence_ids` for pass/fail/inapplicable. Blocked and inapplicable results need a reason. Inapplicable results also need `na_basis`: `unreachable-by-design`, `feature-absent` or `not-supported-by-contract`. Failed results and findings link reciprocally through `finding_ids` and `check_ids`. Preserve superseded results separately when retesting; do not create two current answers for one obligation.

These are abbreviated record fragments, not a complete audit. Expand them for every discovered implementation and reachable class:

```json
{
  "entity": {"id": "screen.settings", "kind": "surface", "name": "Settings", "location": "/settings"},
  "obligation": {
    "id": "obligation.settings.keyboard", "entity_id": "screen.settings",
    "context_id": "member.compact.keyboard",
    "question": "Can the member reach Save by keyboard, with visible unclipped focus?",
    "required_methods": ["rendered", "interaction"]
  },
  "check": {
    "id": "check.settings.keyboard", "obligation_id": "obligation.settings.keyboard",
    "status": "fail", "evidence_ids": ["evidence.settings.render", "evidence.settings.keyboard"],
    "finding_ids": ["UX-001"]
  },
  "finding": {
    "id": "UX-001", "title": "Save action cannot receive keyboard focus",
    "severity": "high", "check_ids": ["check.settings.keyboard"],
    "impact": "Keyboard users cannot save their settings.",
    "recommendation": "Use a correctly named native button and preserve feedback.",
    "acceptance": "Save and retry work using the keyboard; focus remains meaningful."
  }
}
```

Place entities, contexts, evidence, results and findings in their named top-level arrays; obligations belong to `plan.obligations`. A source-only scoped review requires source obligations for every planned entity/context. A runtime review requires rendered evidence for surfaces, states, usages and widgets, interaction evidence for workflows/transitions, and API observations for API-backed transitions. These are minimum consistency gates, **not** a sufficient list of questions: add applicable visual, content, keyboard, screen-reader, responsiveness, permission, resilience, analytical meaning, exploration/action and cross-surface consistency obligations. A single broad question must not replace independently verifiable behaviors.

An intentionally excluded discovered entity retains its record with `exclusion: {"reason": "…", "approval_ref": "…"}`. It has no active context plan; exclusions remain visible in output. Full mode permits no excluded entity. Keep a reduced scope's limitations visible even if its own planned checks are all investigated.

Run `python3 scripts/audit_coverage.py PATH --require-complete`. Exit 0 means valid records and, with this option, reviewed original scope; exit 1 means invalid records; exit 2 means unresolved original coverage. An approved sample can finish its agreed deliverable while this original-full gate still fails. The summary distinguishes `agreed_scope_reviewed`, `original_full_scope_reviewed`, `original_request_reviewed` and `all_planned_applicable_checks_pass`. An investigated defect counts as reviewed coverage, not success. Inspect `completion_gaps`, unresolved entity/context pairs, per-kind counts and exclusions alongside planned-check coverage; that percentage is neither a design-quality score nor proof that discovery is exhaustive.

When migrating version 1, retain evidence and findings as candidate material, explicitly rebuild usages/transition relationships, context classes and planned obligations, classify evidence methods, then reconcile. Do not change only the schema number or reuse an old “100 %” conclusion.

## Inspect in connected passes

### Understand meaning, exploration and consistency

For every in-scope page and independently meaningful metric, table, widget, chart or graph, connect three distinct passes. Trace each drilldown and return path as well. A full audit covers every discovered usage; a focused change retains its bounded scope and affected dependencies.

1. **Meaning and decision.** Establish the user's question and the represented entity, population, unit, calculation, aggregation, timeframe, timezone, comparison, freshness and missing-data meaning where applicable. Identify the decision this information supports. Unknown definitions or thresholds are discovery gaps; do not invent them from color or appearance.
2. **Exploration and action.** Examine existing filters, search, sorting, comparisons, drilldown, linked detail and actions against that question. Test their actual scopes, discoverability, context transfer, empty/error cases, role-dependent availability and return path. Identify helpful missing capabilities as proposals with expected benefit, dependencies and tradeoffs; do not fabricate existing transitions for proposed features.
3. **Consistency across views.** Reconcile the same fact from headline through filtered chart, table, record and export when present. Check population, aggregation, unit, time and role scope; make intentional differences understandable. A correct individual chart does not establish a coherent analytical journey.

Repeat the affected pass after a discovery, contradiction, domain answer or design change, and record fresh evidence. This means different lines of inquiry and targeted reassessment, not three identical checklist runs. Preserve successful existing patterns alongside findings. Use [analytical-meaning.md](analytical-meaning.md), [data-visualization.md](data-visualization.md) and the [surface record](../assets/analytical-surface.template.md).

Plan independently verifiable obligations per entity/context using the existing ledger. A passed render or keyboard check cannot close an unexamined meaning or decision question. Ask focused domain questions throughout the audit using [discovery-and-preferences.md](discovery-and-preferences.md); continue independent inspection while dependent recommendations remain provisional.

### Task and structure

Start a real task at its expected entry point. Can the target user identify the relevant destination and next action? Check navigation names, information scent, task continuity, context changes, deep links, browser Back/Forward, search, scope and exit routes. Trace accidental dead ends and loops.

Assess cognitive work: recall demands, hidden dependencies, redundant entry, misleading defaults, ambiguous units, unexplained permissions and choices offered before the user has context. Record evidence, not a diagnosis of the user's psychology from a screenshot.

### Visual composition

Review each screen at full size, then inspect detail. Name the intended reading order and compare it to the visual emphasis. Check aligned edges, grouping, spacing rhythm, density, type hierarchy, optical balance, text measure, icon consistency, surface hierarchy, status meaning and primary/secondary action distinction.

Challenge repeated patterns: Is a card encoding a meaningful object or merely adding a border? Is whitespace separating groups or breaking a relationship? Are secondary labels too weak to read? Are nested controls creating competing focus targets? Evaluate within the product's aesthetic direction, not the auditor's preferred style.

### Components and states

For every component family inspect its behavioral contract, variants and real usages. Buttons, links, form fields, selection controls, tabs, menus, dialogs, popovers, navigation, badges, notifications, tooltips, tables, empty states and progress indicators require different semantics. Check content and layout under each reachable state.

### Workflow resilience

Follow the complete journey, not just the happy-path screenshots. Submit invalid input, change upstream choices, go Back, interrupt, resume, lose connectivity, retry and return with another role where safe. Verify whether the user can tell what happened and what remains to do. See `workflows.md` and `identity-permissions.md`.

### Access and implementation

Cross-check keyboard, screen reader where available, text resizing, motion preference, contrasts, pointer target behavior and meaningful sequence. Inspect the code for root causes and unsupported assumptions. Test backend permission enforcement only within the authorized audit scope; otherwise record the dependency instead of declaring security proven.

### UI/API consistency

For every defined data-loading or state-changing transition, including initial load and asynchronous completion, record `api.kind`: `none`, `read`, `write` or `job`. Purely local navigation needs a reason for `none`. Other kinds require `operation`, `scope` (user, tenant, object and environment), `outcomes` and `persistence`. Describe observable success, validation/rejection, denial, error/retry and conflict behavior where reachable. List job progress/cancel/retry outcomes where relevant; do not count every internal network call as a separate user journey.

Use authorized fixtures to compare the UI with actual responses and subsequent state. A saved toast before rejection, a stale role after reload, an incorrect tenant in a request or a retry that duplicates work is a contract failure. Plan API-observation plus interaction evidence for these transitions. Checking that a button is hidden does not establish server authorization. Record security dependencies outside the authorized scope separately, and limit security claims; do not silently turn an interface audit into penetration testing. Mocks may support planning but cannot close actual integration obligations.

### Data and performance

Apply the meaning, exploration and consistency passes above to every relevant data surface. Verify chart semantics, units, range, missingness, source, freshness and interactions. Test actual task response on representative data/device conditions. Separate lab performance measurements from production field metrics.

## Report an actionable finding

Every finding includes:

1. Stable ID and concise problem statement.
2. Entity, route, component/file and affected role/context.
3. Steps to reproduce, expected and observed behavior.
4. Evidence reference: screenshot, recording, measured styles, code location, test result or observation.
5. User consequence and affected task.
6. Basis: exact standard criterion, vendor guidance, empirical evidence, approved decision, or contextual design judgment.
7. Confidence: observed / strongly inferred / needs validation.
8. Recommended change, tradeoff, dependencies and observable acceptance criteria.
9. Severity and breadth; mark repeats by root cause.

Do not label a preference as a defect. A finding such as “use a more modern font” lacks impact, evidence and acceptance criteria. A usable finding is “In the account picker, truncation hides the organization suffix for three fixtures; two organizations become visually indistinguishable. Preserve the suffix or reveal the full label on keyboard focus and touch. Verify both organizations can be selected correctly at the compact width.”

## Prioritize without false precision

Use this local severity scale consistently:

| Level | Consequence | Typical response |
| --- | --- | --- |
| Critical | Credible unauthorized disclosure/action, irreversible loss, or comparable severe impact | Address the affected release/task immediately; verify security dependencies |
| High | Critical task blocked for a relevant user group, serious accessibility barrier, repeated severe error | Fix before claiming that critical journey ready |
| Medium | Task completes with substantial confusion, rework or avoidable effort | Schedule ahead of decorative polish |
| Low | Limited inconsistency or visual refinement with minor task impact | Bundle into relevant component work |

Judge frequency, reach, severity, recoverability, confidence and effort together. An infrequent destructive error can outrank a frequent cosmetic issue. Keep unknown exposure separate from known severity. A computed score can support local prioritization only when its weights and limits are visible; never present it as a universal design-quality percentage.

## Deliverables and honest completion

For an audit, deliver the scope/revision, critical journeys, prioritized findings, coverage matrix, source basis, and a sequenced improvement plan. Separate immediate fixes, shared-system changes, workflow redesigns and hypotheses requiring research. If concept design is requested, carry the selected findings into the design contract.

For each entity and relevant context report whether applicable checks passed, failed, were blocked or untested. Report pages, usages, widgets and transitions separately, with explicit exclusions and discovery gaps. Say “24 of 31 discovered routes exercised; 4 inaccessible by role; 3 not yet tested,” not “the entire frontend audited” while gaps remain. Source review completion, runtime coverage, a narrower approved deliverable and product quality are separate statements. An interim report can be delivered with gaps; the full-audit task remains incomplete. A fully covered audit can still report product defects.

For implementation, verify the changed journey and affected shared usages. Preserve a resumable backlog when work spans contexts. On resume, read the contract, inventory, open findings and latest evidence before changing scope or closing items.

Conclude with what the evidence establishes, the remaining uncertainty and the next useful action. Do not promise a percentage improvement before comparable task measurements exist.
