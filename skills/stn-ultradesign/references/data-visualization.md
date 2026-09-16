# Charts, graphs, dashboards and data grids

Load for analytical screens, numerical widgets, maps, relationship diagrams, data tables and visual editors. These are operational design procedures synthesized for this skill. They are not a universal chart specification. Source access date: 2026-09-16.

## 1. Write the analytical contract

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

Prefer direct series labels when feasible. Place units where a reader needs them, use locally appropriate number formatting and sensible precision, and keep labels readable at supported sizes. Write a descriptive title for exploration; a takeaway title is appropriate only when supported by the data. Put methodological qualifications near the claim they qualify. Remove ornament that competes with interpretation while retaining useful reference lines and explanatory annotations.

Edward Tufte's sparklines put compact trends beside related words and values. Use them with enough context to interpret the measure and period; removing all scale context is not a general mandate. [Tufte's original discussion](https://www.edwardtufte.com/notebook/sparkline-theory-and-practice-edward-tufte/)

**Done when:** the intended distinctions survive theme changes, reduced color discrimination, resizing and representative label lengths.

## 6. Provide equivalent interaction and understanding

Give a chart an accessible identity and a concise summary of its purpose and important patterns. Provide a discoverable detailed description or structured data view appropriate to its complexity. A data table helps exact lookup but does not automatically explain the trend, relationships or uncertainty. W3C's complex-images tutorial distinguishes short identification from a fuller equivalent description. [WAI tutorial](https://www.w3.org/WAI/tutorials/images/complex/)

Every essential operation must have a usable keyboard route and a touch route: choosing a series, filtering, revealing values, changing range, drilling down and returning. Avoid thousands of sequential tab stops. Define a navigable grouping or companion control/data view suited to the task. Focus and selection remain visibly distinct and survive data updates where the same item remains available.

Provide a non-hover way to inspect details. Dismissible overlays must not obstruct the inspected point or trap the person. Use visible controls as alternatives to dragging, lassoing, pinching or precision gestures. Explain when chart interaction changes a global filter versus highlighting locally. Preserve browser scrolling and zooming unless the user deliberately enters a canvas interaction mode.

Test the chosen library's actual behavior. Labels on SVG marks do not by themselves provide a complete keyboard model or useful screen-reader sequence. Observable Plot exposes ARIA labeling options, illustrating that authors still supply meaningful descriptions. [Plot accessibility](https://observablehq.github.io/plot/features/accessibility)

**Done when:** representative analytical tasks can be completed with keyboard, touch and the supported assistive technologies; record any gap rather than declaring accessibility from markup alone.

## 7. Compose dashboards and widgets around decisions

Define the dashboard's recurring questions and the action each answer enables. Group related evidence so comparison is spatially easy. Give critical exceptions stronger prominence than routine summaries. Avoid giving every metric equal visual weight or surrounding every number with a large empty card. Support density that serves the audience while preserving legibility and interaction space.

A numerical widget needs a label, value, unit, relevant period and meaningful comparator. Include whether higher is better, where ambiguity exists. Distinguish a target from the previous period and a forecast. A sparkline may explain trajectory; it does not replace the value definition. Show stale or partially refreshed data explicitly and identify refresh time semantics.

Few distinguishes at-a-glance monitoring from analytical exploration. Apply that distinction when deciding what belongs in the overview and what merits a deeper destination. His historical single-screen framing is not a mandate to shrink a responsive dashboard into an unreadable phone screen. [Dashboard Confusion Revisited](https://perceptualedge.com/articles/visual_business_intelligence/dboard_confusion_revisited.pdf)

Give filters visible scope, current values and a reset path. Coordinated widgets must use compatible time ranges or show exceptions. Preserve relevant state on drill-down and return. Customization needs a recoverable default, clear persistence and a non-drag reordering method. Test realistic alert volume; perpetual red states and decorative green deltas undermine interpretation.

**Done when:** each widget has a decision purpose, the overview exposes priority conditions, and cross-widget comparisons are semantically valid.

## 8. Choose tables and grids consciously

Use semantic HTML tables for tabular reading. Use an interactive grid when spreadsheet-like navigation or editing warrants the additional interaction model. WAI-ARIA APG distinguishes grids from static tables and describes the focus management they require. Adding a grid role without implementing the expected behavior is insufficient. [APG grid pattern](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)

Keep column names, units and row identity available while inspecting relevant values. Align comparable numbers and precision consistently. Support sorting and filtering with visible current state, stable results and clear reset. Distinguish selection of the current page from selection of all matching records; explain batch-action scope before consequential actions.

For editing, define start, commit, cancel, validation, pending save, conflict and recovery behavior. Preserve a recoverable draft through an error. For large data, evaluate pagination or virtualization against keyboard movement, assistive technology, find-in-page, copy and export. Make the dataset scope explicit when the browser contains only a subset.

On narrow screens, choose between essential columns with disclosure, a labeled scrollable region, task-specific cards or a separate comparison view. Preserve column relationships when comparing rows is the task. Do not assume that converting every row to a card preserves the table's utility.

**Done when:** users can locate, compare and act on the intended records with clear scope, including at supported narrow widths.

## 9. Treat relationship graphs as a distinct problem

A node-link graph represents relationships; “graph” also colloquially means a quantitative chart. Establish which is required. Define node identity, edge meaning, direction, weight, multiplicity and whether absence means no relationship or unknown data. A process diagram additionally needs valid states, transitions, branches and completion conditions.

For dense networks, compare an adjacency matrix, search-plus-neighbor list, filtered subgraph or hierarchical view. A force layout can reveal structure but becomes useless when labels and edges overlap. Keep the layout stable during inspection, explain what geometric proximity means, and expose hidden node/edge counts. Provide search, selection, neighbors, path inspection and return-to-overview where those support the contract.

An editor needs explicit creation and deletion semantics, validation, undo, zoom controls and non-drag alternatives for moving or connecting objects. Preserve the user's position after opening a properties panel. Provide a textual relationship or dependency view that can answer equivalent questions.

**Done when:** a representative path, dependency or neighbor task succeeds, and the view does not imply unencoded meaning through incidental geometry.

## 10. Verify the whole visualization

Choose render technology based on data volume, interaction and accessibility needs. Use the project's existing supported library when it can meet the contract. SVG, canvas and WebGL have different operational costs; selecting one does not settle the semantic or accessibility design. Keep data transformation and interaction state inspectable.

Mike Bostock describes configurable reusable charts; current Plot documentation offers both server and client integration approaches for React. Consult the installed library's version before copying an example, and manage chart lifecycle, updates and cleanup explicitly. [Bostock](https://bost.ocks.org/mike/chart/), [Plot integration](https://observablehq.github.io/plot/getting-started)

Verify with fixtures containing all-zero, one-point, constant, negative, extreme, missing, duplicate, dense and long-label data. Test resize, zoom, theme, loading, failure, refresh and filter races. Check that export retains units, filters, date range and relevant caveats. Validate permissions independently; hiding a series is not authorization.

Ask a representative person to answer the contract's question and explain their conclusion. Record correctness, time where meaningful, confidence and misinterpretations. Report task validity, numerical correctness, accessibility and rendering performance separately. A smooth animation or screenshot cannot substitute for those outcomes.

**Done when:** data correctness, comprehension, equivalent interaction and performance have explicit evidence, with remaining limits identified.
