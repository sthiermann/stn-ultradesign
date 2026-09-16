# Analytical surface record — [surface name]

Use one record per actual widget, chart, table, graph or detail usage. Link shared definitions instead of duplicating them; a shared component does not erase differences in data or context. Duplicate the metric section for materially different measures. Apply only relevant capabilities, with a reason for `not applicable`; missing knowledge/access is `unknown`/`blocked`, not inapplicable.

Read [analytical meaning](../references/analytical-meaning.md) for interpretation and [data visualization](../references/data-visualization.md) for representation and interaction. This record supplements the audit ledger and feature map; it does not independently certify complete coverage. In audit-only mode, record observed behavior and findings without inventing proposed destinations. Keep real confidential data and credentials out of the artifact.

## Record and scope

| Field | Project entry |
| --- | --- |
| Surface ID / usage ID / shared family | |
| Parent surface and every applicable detail/transition ID | |
| Route, panel/widget name and entry point | |
| Mode and requested scope | Audit / concept / implementation / focused fix; link the actual request |
| Current revision, data snapshot, environment | |
| Approved design/feature contract, if applicable | |
| Actor, permitted role and tenant/account scope | Use safe fixture identities |
| Supported locales, themes, densities, input and space classes | List relevant contexts; justify shared behavior classes |
| Evidence owner/date and unresolved access limits | |

## User question and existing value

- What exact question should this surface answer?
- What decision or next action does that answer support, and for whom?
- What can the user already understand or accomplish reliably? What evidence supports retaining it?
- What representation and interactions exist now? What is confirmed, inferred or not observed?
- Which information must be immediately visible, and which can be disclosed without interrupting the task?

## Metric/data meaning — repeat per materially different measure

For each entry, distinguish the verified definition from an assumption. State where essential meaning is visible or discoverable by keyboard, touch and assistive technology. A technical identifier alone is not a user-facing explanation.

| Meaning | Definition and authority | Where the user learns it / evidence |
| --- | --- | --- |
| Name and domain concept | | |
| Observation unit/grain and stable record identity | | |
| Unit, scale, currency/conversion and displayed precision | | |
| Aggregation/formula and grouping dimensions | Link the authoritative definition; note valid rollup levels | |
| Population, denominator, exclusions and duplicate treatment | | |
| Time field, window, bucket boundaries and timezone | Include partial periods and relevant calendar rules | |
| Baseline/comparator and whether populations are comparable | | |
| Desired direction | Higher / lower / target range / contextual / neutral, with reason | |
| Threshold or qualitative-band authority | Owner/source, effective version, boundaries including equality; or none | |
| Freshness and completeness | Observation time, ingestion/refresh time, expected delay, stale rule | |
| Missing/unknown/zero/not applicable/suppressed/estimated | Distinct meanings and representations | |
| Source and transformations | Safe query/API/definition reference; do not expose secrets | |
| Access constraints | Which rows, dimensions and totals this actor may see | |
| Uncertainty, forecast or revised-value status | Where relevant; otherwise reason for inapplicability | |

Expected answer from a safe, known fixture: **[answer, calculation and source reference]**.

Unresolved semantic questions and their owners: **[list]**. Do not present a guessed interpretation as a verified metric.

## Representation and user-visible context

| Element | Current behavior | Required or proposed behavior, with basis |
| --- | --- | --- |
| Encoding, scale and ordering | | |
| Visible title, unit, period and comparison | | |
| Status color/shape/text and its authority | Separate brand, selection, trend and status | |
| Missing, stale, empty, no-results, loading and error | | |
| Summary or alternative data/relationship view | Equivalent question and operations, not merely an unstructured dump | |
| Container adaptation and long content | Preserve comparison, labels, controls and relevant context | |

## Scope of each supported operation

Record the actual dataset boundary, visible feedback, persistence and verification. Do not add every operation automatically.

| Operation | Data/field scope and current rules | Feedback, reset and persistence | Expected fixture outcome / evidence or N/A reason |
| --- | --- | --- | --- |
| Sort | Type, direction, ties, nulls, multiple keys; client/server | | |
| Search | Fields, matching, loaded subset versus authorized dataset | | |
| Filter | Draft/applied, combinations, locked constraints, time basis | | |
| Page/load more | Parent/child counting, total known/unknown, cursor behavior | | |
| Selection/batch action | Page/loaded/all matching, exclusions, eligible count | | |
| Totals/group summaries | Population and aggregation; reaction to filter/page/selection | | |
| Expand or drill | Source identity, target grain and inherited context | | |
| Cross-filter/highlight | Targets, field mapping, exclusions and clear behavior | | |
| Export/copy | Rows/columns, filter/sort, raw/formatted, metadata, access | | |
| Edit or domain action | Actual commit, pending/failure/recovery contract | | |

Explicit differences among **displayed rows**, **matching records**, **selected records**, **eligible records** and **exported records**: [record or explain equivalence].

## Follow every defined detail path in scope

Add a row for each transition and meaningful branch, including nested drilldowns, direct links, clear/reset and return. Link existing ledger obligations. A disabled, denied or unavailable target remains an observed state or gap rather than silently disappearing from the map.

| Transition ID | Source + trigger | Target and retained/replaced context | Loading, failure or access change | Return/history + focus destination | Evidence/status |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Context to retain or intentionally change: tenant/role, selected identity, search, filters, time range/timezone, hierarchy level, sort, page/cursor, expanded groups, selection, chart zoom and scroll. Record a logical focus successor if the original row/mark disappears. Explain breadcrumbs separately from browser Back.

Reconcile aggregate → contributing records → detail → export where supported:

| Fixture + context | Expected identities/values at each level | Actual result | Explanation of legitimate differences or defect | Evidence |
| --- | --- | --- | --- | --- |
| | | | | |

A total need not equal the sum of one visible page or a nonadditive measure. It must follow the declared meaning and authorized population. Use permitted role/tenant fixtures; do not seek unauthorized data to perform the comparison.

## Preservation, findings and opportunities

| Type | Observation or proposal | Evidence / confidence | User consequence | Preservation/change decision | Validation |
| --- | --- | --- | --- | --- | --- |
| Existing strength | | | | Preserve unless specifically changed | Regression condition |
| Observed defect or missing interpretation | | | | | Reproduction and expected correction |
| Opportunity hypothesis | | | | No commitment until scope/contract permits | Useful question, required data, comparison and success criterion |

An opportunity may be a clearer explanation, benchmark, breakdown or detail path. Record unavailable data and dependencies. Do not fabricate a benchmark or remove an existing function merely to simplify the layout.

## Proportionate acceptance evidence

Plan applicable cases before claiming completion: ordinary fixture; zero versus unknown; partial/stale period; equal/negative/extreme values; duplicate names; empty filter intersection; restricted authorized scope; changed selection after refresh; late response; nested-detail failure; return after the source changes; and export of a partly loaded dataset. Explain omissions. Cover keyboard, touch and supported assistive technology with an equivalent analytical task.

| Obligation/contract ID | Context, method, revision and fixture | Expected result | Actual result and evidence | Pass / fail / blocked / not tested / reasoned N/A |
| --- | --- | --- | --- | --- |
| | | | | |

Report independently:

- Business meaning and numerical reconciliation: [status and gaps].
- User comprehension and useful action: [observed result; distinguish hypothesis from user evidence].
- Interaction/context continuity and accessibility: [tested paths and remaining gaps].
- Visual acceptance and actual delivery surface: [inspected revision/context].
- Original audit coverage, feature parity and user approval: [link their separate records; no implied completion].
