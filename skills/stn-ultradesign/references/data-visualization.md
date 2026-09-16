# Charts, graphs, dashboards and data grids

Load for analytical screens, numerical widgets, maps, relationship diagrams, data tables and visual editors. These are operational design procedures synthesized for this skill. They are not a universal chart specification. Source access date: 2026-09-16.

## 1. Write the analytical contract

Use [analytical-meaning.md](analytical-meaning.md) to establish business meaning before choosing an encoding or interaction. Record each actual widget, chart, table and detail usage with the [analytical surface template](../assets/analytical-surface.template.md), linking its surface/usage and transition IDs to the audit inventory. Reusing the same chart component does not prove that two datasets, aggregation levels or role contexts have the same meaning. A full audit follows every discovered analytical surface and defined detail transition; the template does not reduce that obligation to a sample.

For every visualization, record the question, intended decision, audience, data source, observation unit, dimensions, measures, units, aggregation, time range, timezone, refresh behavior and meaningful comparison. Identify sampling, uncertainty, missingness and access restrictions. Define the correct answer to a representative question using the underlying data before selecting the visual.

Specify whether the surface explains a known result, supports open exploration, monitors changing conditions or edits a model. Those purposes demand different amounts of interaction and context. A chart that looks convincing but answers the wrong question fails the contract.

Tamara Munzner separates problem characterization, data/task abstraction, encoding/interaction and algorithm design. Each layer requires appropriate validation; faster rendering cannot establish that the represented task is useful. [Original paper](https://www.cs.ubc.ca/labs/imager/tr/2009/NestedModel/NestedModel.pdf)

**Done when:** the question has a verifiable answer and each displayed measure has an unambiguous meaning and provenance.

## 2. Select a representation by question

The following decision matrix is this skill's starting procedure. Compare alternatives on the actual data and user task; do not select a chart to fill an empty card.

| Analytical question | Candidate representation | Required check |
| --- | --- | --- |
| Which category is larger or ranked highest? | Sorted horizontal bars or aligned dots | Preserve natural category order when it matters; allow ties |
| How did a quantity change over time? | Line or step chart | True time spacing, gaps and valid interpolation |
| How much changed between two points? | Paired dots, slope chart or explicit difference bars | Same entities and units; distinguish relative from absolute change |
| What is the distribution? | Histogram, dot plot, box plot or ECDF | Explain bins or summary statistics; retain relevant outliers and sample size |
| Are two quantitative variables associated? | Scatterplot, then density or bins for overlap | Represent occlusion and exclusions; correlation is not causation |
| How does a value compare with a target? | Dot/bar plus reference marker, or bullet chart | Correct comparison period, target provenance and direction of improvement |
| How is a total composed? | Stacked bars or a simple part-to-whole chart | Categories must belong to the same meaningful whole; expose denominator |
| How does composition change across groups? | 100% stacked bars or aligned small multiples | Percentages can conceal large differences in absolute totals |
| Where does a geographic pattern occur? | Map with suitable normalization and legend | Geography must be part of the question; distinguish rates from counts |
| What is the exact value for an item? | Table | Search, units, precision and column relationships |
| What relates to what? | Node-link graph, matrix or neighbor list | Relationship semantics, direction, density and path task |
| What depends on what over time? | Timeline, dependency diagram or Gantt view | Dependencies, duration, status and time semantics remain distinct |

Use common-scale small multiples when overlapping series become unreadable. Use a table when exact lookup dominates. Pie or donut charts can support a simple part-to-whole message; compare against bars when differences are subtle or categories numerous. A gauge is a deliberate domain metaphor, not the default for every KPI. Three-dimensional decoration must not distort quantitative judgment.

Stephen Few's bullet chart places a main measure alongside comparison values and optional qualitative ranges in compact space. It is an available design pattern, not a requirement to replace every radial display. [Original specification](https://www.perceptualedge.com/articles/misc/Bullet_Graph_Design_Spec.pdf)

**Done when:** the selected encoding makes the contract's comparison possible, and a simpler alternative was considered where complexity is substantial.

## 3. Make scales and transformations honest

Use a zero baseline for bars and filled areas that encode magnitude from a baseline. Negative values extend across zero. For point or line displays, a narrower domain may reveal meaningful variation; expose the domain and avoid implying exaggerated absolute magnitude. Keep comparable panels on consistent domains unless a documented task requires otherwise. Clearly label independent scales.

Use nonlinear scales only for a justified analytical purpose. Label the transformation and ticks intelligibly; define treatment of zero and negative values. Prefer aligned separate panels over an arbitrary dual axis. The ONS guidance explains these scale pitfalls for its public statistical communication context. [Axes and gridlines](https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines)

Inspect the data pipeline, not only the rendered axes. Check denominator changes, duplicated observations, weighted versus unweighted averages, date buckets, currency conversion, unit conversion, seasonal adjustment, rounding and filters. Show whether “change” means percentage points or percent. Compare equivalent partial periods or identify the mismatch.

If visual area represents magnitude, calculate area from the value rather than mapping the value directly to radius. Explain cumulative versus period values. Keep chosen chart order stable during inspection; offer sorting deliberately. Show the number of omitted categories and how an “Other” group is calculated. Explain any smoothing or downsampling; preserve spikes when they drive the user's decisions.

**Done when:** fixture data can reproduce visible values and transformations, including negative, zero, extreme and partial-period cases.

## 4. Represent uncertainty and absence

Distinguish observed zero, unknown, not applicable, suppressed, estimated and not yet collected. A null value must not silently become zero. Use a visible gap for missing time observations unless an interpolation method is intentional and disclosed. Separate the absence of records from a failed request and from a filter that matched nothing.

When uncertainty affects interpretation, show it in an appropriate form, such as intervals, bands or distributions. Identify the interval type, coverage level, source and what it does and does not express. Distinguish a confidence interval for an estimate from a prediction interval for a future observation. Do not treat interval overlap alone as a statistical test. Validate scientific interpretations with the domain owner.

ONS recommends displaying uncertainty when omitting it would alter interpretation and explains how it adds complexity. Its preferred visual treatments are editorial conventions for its audience; this skill does not elevate them to universal scientific rules. [Uncertainty guidance](https://service-manual.ons.gov.uk/data-visualisation/guidance/showing-uncertainty-in-charts)

Mark forecast boundaries, model assumptions, revised observations and incomplete periods. An estimated value should not acquire false precision through extra decimals. If the evidence cannot support a directional conclusion, state that limitation rather than using a persuasive trend label.

**Done when:** a reader can distinguish what is known, estimated, missing and uncertain without relying on a hidden tooltip.

## 5. Use color, text and shape deliberately

Assign semantic colors separately from categorical series colors. The same entity keeps its color across coordinated views. Use sequential palettes for ordered magnitude and diverging palettes around a meaningful midpoint. Arbitrary categories need distinguishable identities rather than an implied high-to-low scale. Reserve alert emphasis for conditions that warrant attention.

Support distinctions with labels, position, line style, symbols or patterns where needed. Check text and essential graphical contrast against the actual background in each theme. WCAG non-text contrast concerns graphical parts required to understand content and applicable component states; it does not mean every decorative gridline must meet the same test. [W3C explanation of SC 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)

Keep status, trend and selection separate. A rising value is not automatically good, and a neutral brand accent is not a threshold. Bind any qualitative band to a named rule, owner/source, unit, effective period and boundary behavior. Check equality at the boundary, missing observations and stale values before assigning an alert color. If no justified threshold exists, show a neutral value or comparison and label a proposed interpretation as a hypothesis; do not invent red/amber/green cutoffs to fill a design.

Prefer direct series labels when feasible. Place units where a reader needs them, use locally appropriate number formatting and sensible precision, and keep labels readable at supported sizes. Write a descriptive title for exploration; a takeaway title is appropriate only when supported by the data. Put methodological qualifications near the claim they qualify. Remove ornament that competes with interpretation while retaining useful reference lines and explanatory annotations.

Edward Tufte's sparklines put compact trends beside related words and values. Use them with enough context to interpret the measure and period; removing all scale context is not a general mandate. [Tufte's original discussion](https://www.edwardtufte.com/notebook/sparkline-theory-and-practice-edward-tufte/)

**Done when:** the intended distinctions survive theme changes, reduced color discrimination, resizing and representative label lengths.

## 6. Provide equivalent interaction and understanding

Give a chart an accessible identity and a concise summary of its purpose and important patterns. Provide a discoverable detailed description or structured data view appropriate to its complexity. A data table helps exact lookup but does not automatically explain the trend, relationships or uncertainty. W3C's complex-images tutorial distinguishes short identification from a fuller equivalent description. [WAI tutorial](https://www.w3.org/WAI/tutorials/images/complex/)

Every essential operation must have a usable keyboard route and a touch route: choosing a series, filtering, revealing values, changing range, drilling down and returning. Avoid thousands of sequential tab stops. Define a navigable grouping or companion control/data view suited to the task. Focus and selection remain visibly distinct and survive data updates where the same item remains available.

Provide a non-hover way to inspect details. Dismissible overlays must not obstruct the inspected point or trap the person. Use visible controls as alternatives to dragging, lassoing, pinching or precision gestures. Explain when chart interaction changes a global filter versus highlighting locally. Preserve browser scrolling and zooming unless the user deliberately enters a canvas interaction mode.

Test the chosen library's actual behavior. Labels on SVG marks do not by themselves provide a complete keyboard model or useful screen-reader sequence. Observable Plot exposes ARIA labeling options, illustrating that authors still supply meaningful descriptions. [Plot accessibility](https://observablehq.github.io/plot/features/accessibility)

**Done when:** planned analytical tasks for every audited usage in the declared scope can be completed with keyboard, touch and the supported assistive technologies; record any gap rather than declaring accessibility from markup alone.

## 7. Compose dashboards and widgets around decisions

Define the dashboard's recurring questions and the action each answer enables. Group related evidence so comparison is spatially easy. Give critical exceptions stronger prominence than routine summaries. Avoid giving every metric equal visual weight or surrounding every number with a large empty card. Support density that serves the audience while preserving legibility and interaction space.

A numerical widget needs a label, value, unit, relevant period and meaningful comparator. Include whether higher is better, where ambiguity exists. Distinguish a target from the previous period and a forecast. A sparkline may explain trajectory; it does not replace the value definition. Show stale or partially refreshed data explicitly and identify refresh time semantics.

Few distinguishes at-a-glance monitoring from analytical exploration. Apply that distinction when deciding what belongs in the overview and what merits a deeper destination. His historical single-screen framing is not a mandate to shrink a responsive dashboard into an unreadable phone screen. [Dashboard Confusion Revisited](https://perceptualedge.com/articles/visual_business_intelligence/dboard_confusion_revisited.pdf)

Give filters visible scope, current values and a reset path. Coordinated widgets must use compatible time ranges or show exceptions. Preserve relevant state on drill-down and return. Customization needs a recoverable default, clear persistence and a non-drag reordering method. Test realistic alert volume; perpetual red states and decorative green deltas undermine interpretation.

**Done when:** each widget has a decision purpose, the overview exposes priority conditions, and cross-widget comparisons are semantically valid.

### Trace selection, drill and return as separate transitions

Distinguish expanding a row, moving through a hierarchy, navigating to a filtered detail page, filtering sibling widgets and highlighting a subset without excluding others. Name the interaction and its scope visibly. A decorative hover effect must not be the only clue or route to detail. Power BI explicitly separates drillthrough to another filtered page from drill mode inside a visual. [Power BI drillthrough](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-drillthrough)

For each transition specify source mark/row identity, active tenant and role, filters, time range, target grain, inherited versus replaced constraints, loading/failure behavior and the return destination. Show the selected entity and effective context on the target. Preserve relevant search, sort, page/cursor, expanded groups, chart range, selection and scroll on Back; restore focus to the invoking control or a documented successor if it disappeared. Breadcrumbs describe location; they do not replace browser-history behavior or prove context preservation. Test direct entry into a detail link as well as arrival from the parent.

For coordinated views, record source fields, target fields, affected widgets and what clearing the selection does. Tableau exposes explicit source/target field mapping and different clearing policies; this is a reason to decide the contract, not to choose a policy by accident. [Tableau filter actions](https://help.tableau.com/current/pro/desktop/en-us/actions_filter.htm) Make the effect discoverable with active context and reset controls, and provide keyboard/touch alternatives to hover or right-click. Test multiple selections, independent local filters, a target with no data and a late response to an older selection.

Reconcile summary, detail and export against the same authorized fixture and data revision. Explain legitimate differences in grain, time, denominator or aggregation instead of forcing a total to equal the visible page's arithmetic sum. A row expansion can be deferred and fail independently of the parent. Carbon recommends a separate destination or panel when expanded detail becomes cramped; that is a task-based alternative, not permission to remove the detail. [Carbon data table](https://carbondesignsystem.com/components/data-table/usage/)

## 8. Choose tables and grids consciously

Use semantic HTML tables for tabular reading. Use an interactive grid when spreadsheet-like navigation or editing warrants its additional interaction model. Adding a grid role without the expected focus and keyboard behavior is insufficient. [APG grid pattern](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)

Select capabilities from the actual task and existing feature contract. The following is a decision/check matrix, not a demand to add search, pagination or export to every table.

| Capability | Contract to establish | Counterexample to exercise |
| --- | --- | --- |
| Row and column identity | Observation grain, stable key, label, unit, precision and grouping level | Duplicate names, reformatted identifiers, group rows mistaken for records |
| Sort | Actual value/type, direction, multi-sort priority, tie rule and null order; client versus server scope | Numeric-looking text, equivalent values, missing values, next page after sorting |
| Search | Searched fields, matching rules, selected dataset and search versus column-filter scope | Hidden field matches, no results, accents/case, a response to an older query |
| Filter | Applied versus draft values, combination rules, time basis, active indicators and reset | Empty intersection, timezone boundary, locked role filter, changed denominator |
| Pagination or incremental loading | What a page counts, known/unknown total, cursor stability and loaded versus complete scope | Expanded child at a boundary, changed page size, deletion of the last row, stale cursor |
| Selection and batch action | Current page, loaded rows or all matching authorized records; exclusions and reset/persistence | Filter or refresh after selecting, ineligible row, mixed permissions, partial failure |
| Totals and summaries | Population, aggregation and whether filters/grouping/paging affect the result | Visible rows differ from the total, nonadditive measure, restricted detail |
| Expand/detail | Distinct expansion, selection and navigation targets; loading and return contract | Nested detail failure, long content, row moved or removed while open |
| Export/copy | Chosen rows/columns, filter/sort scope, raw versus displayed values, time/unit metadata and permissions | Hidden columns, collapsed groups, unloaded rows, stale export and missing values |

AG Grid documents different select-all scopes and separate export options for selected versus filtered/sorted rows. Its defaults are library configuration, not proof of the application's intended dataset. [Selection scope](https://www.ag-grid.com/javascript-data-grid/row-selection-multi-row/), [CSV export](https://www.ag-grid.com/javascript-data-grid/csv-export/) Inspect the installed row model and actual application configuration. Do not describe a loaded subset as “all results,” or imply that a selected count equals the batch action's eligible count.

Keep column names, units and row identity available while inspecting values. Align comparable numbers and precision. Expose current sort/filter state and recovery from a query yielding no rows without conflating it with a fetch failure. If updates move the inspected row, maintain intelligible focus and identity; avoid silently applying an action to the new occupant of an old visual position.

For editing, define start, commit, cancel, validation, pending save, conflict and recovery. Preserve recoverable drafts. For large datasets, evaluate pagination or virtualization against keyboard movement, assistive technology, browser find, copy and export. AG Grid's child-row pagination options illustrate how expanding a parent can place its children on another page; test the actual chosen behavior rather than assuming expansion reveals visible detail. [Pagination and child rows](https://www.ag-grid.com/javascript-data-grid/row-pagination/)

On narrow screens, choose essential columns with disclosure, a labeled scrollable region, task-specific cards or a separate comparison view. Preserve relationships when comparison is the task. All retained capabilities need an equivalent reachable path; converting every row to a card is not evidence of parity. Identify the expanded state programmatically, expose sorting/selection appropriately and keep row actions usable without hover; see [component-states.md](component-states.md).

**Done when:** users can locate, compare, inspect and act on the intended authorized records with truthful scope; applicable sorting, filtering, selection, pagination, detail and export outcomes have evidence at supported sizes.

## 9. Treat relationship graphs as a distinct problem

A node-link graph represents relationships; “graph” also colloquially means a quantitative chart. Establish which is required. Define node identity, edge meaning, direction, weight, multiplicity and whether absence means no relationship or unknown data. A process diagram additionally needs valid states, transitions, branches and completion conditions.

For dense networks, compare an adjacency matrix, search-plus-neighbor list, filtered subgraph or hierarchical view. A force layout can reveal structure but becomes useless when labels and edges overlap. Keep the layout stable during inspection, explain what geometric proximity means, and expose hidden node/edge counts. Provide search, selection, neighbors, path inspection and return-to-overview where those support the contract.

An editor needs explicit creation and deletion semantics, validation, undo, zoom controls and non-drag alternatives for moving or connecting objects. Preserve the user's position after opening a properties panel. Provide a textual relationship or dependency view that can answer equivalent questions.

**Done when:** the planned path, dependency or neighbor tasks across audited usages succeed, and the view does not imply unencoded meaning through incidental geometry.

## 10. Verify the whole visualization

Choose render technology based on data volume, interaction and accessibility needs. Use the project's existing supported library when it can meet the contract. SVG, canvas and WebGL have different operational costs; selecting one does not settle the semantic or accessibility design. Keep data transformation and interaction state inspectable.

Mike Bostock describes configurable reusable charts; current Plot documentation offers both server and client integration approaches for React. Consult the installed library's version before copying an example, and manage chart lifecycle, updates and cleanup explicitly. [Bostock](https://bost.ocks.org/mike/chart/), [Plot integration](https://observablehq.github.io/plot/getting-started)

Verify with fixtures containing all-zero, one-point, constant, negative, extreme, missing, duplicate, dense and long-label data. Test resize, zoom, theme, loading, failure, refresh and filter races. Check that export retains units, filters, date range and relevant caveats. Validate permissions independently; hiding a series is not authorization.

Run a reconciled path from widget/aggregate to contributing rows, a nested detail and an export where those capabilities exist. Keep a safe fixture with expected values and identities, including a restricted role/tenant case; verify displayed totals, counts and destinations against that authorized scope. Do not attempt unauthorized access to obtain a comparison. UI inspection identifies an enforcement dependency, not a security certification. Record source/API evidence separately from observed rendered/interactive results.

For each surface preserve what already works, identify observed missing context or misleading behavior, and separately propose opportunities. A proposed benchmark, new breakdown, filter or drill path is a hypothesis requiring a data source, useful user question and validation method. Do not manufacture unavailable data or remove existing capabilities to make a cleaner screenshot.

Ask a representative person to answer the contract's question and explain their conclusion. Record correctness, time where meaningful, confidence and misinterpretations. Report task validity, numerical correctness, accessibility and rendering performance separately. A smooth animation or screenshot cannot substitute for those outcomes.

**Done when:** data correctness, comprehension, equivalent interaction and performance have explicit evidence, with remaining limits identified.

**Research boundary:** the linked Power BI, Tableau, Carbon and AG Grid pages were readable primary documentation checked on 2026-09-16. Their configurable patterns inform the checks above; they do not require those products or establish the behavior of another application. No vendor demo or production dataset was executed in this research pass. Verify installed versions, row models and server/API contracts before adopting implementation-specific behavior.
