# Analytical experiences: meaning, comparison, and action

**Research date:** 2026-09-16. **Scope:** primary Microsoft Power BI, Tableau, Qlik, IBM Carbon, and American Statistical Association material. **Purpose:** extend STN Ultradesign beyond chart appearance to the business interpretation of every analytical surface.

The operational result is [Analytical meaning](../../skills/stn-ultradesign/references/analytical-meaning.md), used with [Data visualization](../../skills/stn-ultradesign/references/data-visualization.md) and the [analytical surface template](../../skills/stn-ultradesign/assets/analytical-surface.template.md). This note is an original synthesis. It includes no third-party skill text, copied product assets, private application data, or vendor implementation code.

## What changes in the audit

A polished representation can faithfully display a misleading calculation. The extended audit therefore asks what each value represents, which population it describes, what comparison is valid, how reliable and current the evidence is, and which real decision follows. It covers ordinary business tables and small widgets as well as dedicated dashboards. It does not assume that every application needs more KPIs or predictive features.

The sources establish different kinds of evidence. Vendor documentation explains how a particular product behaves. Carbon offers design-system conventions. The ASA provides methodological guidance on statistical interpretation. None establishes universal business targets, a mandatory cross-industry dashboard layout, or proof that this skill improves outcomes. The new review procedure and its synthetic examples are this project's own application of those distinctions.

## Primary findings and their design implications

### Microsoft: a visible value depends on the model

[Star schema guidance](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema) separates observations, dimensional context, and calculated measures. The important implication is that an interface label and a numeric database type cannot establish the intended aggregation. The audit needs the metric definition and the actual observation grain. A missing definition becomes an evidence gap rather than an opportunity to guess.

[Many-to-many relationship guidance](https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many) discusses facts at different levels of detail, including targets coarser than actuals. Our procedure requires a valid comparison level or an approved allocation method; it does not fabricate fine-grained goals to make a chart look complete.

[KPI visual documentation](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-kpi) exposes direction-of-improvement configuration. This supports a basic semantic check: upward movement and favorable movement are independent. The component's configuration cannot determine whether a target is appropriate or who authorized it.

[Data refresh documentation](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-data) distinguishes underlying data refresh from refreshing report visuals. The resulting interface requirement is to report the relevant freshness evidence. A newly rendered page is not proof of newly observed business conditions.

[Filters and highlighting](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-reports-filters-and-highlighting) distinguish changing the included data from emphasizing a subset. [Visual interactions](https://learn.microsoft.com/en-us/power-bi/create-reports/service-reports-visual-interactions) further show that related views need not react identically. The review must inspect actual source/target behavior rather than assume every chart click applies one global filter.

### Tableau: context changes the answer

[Data aggregation](https://help.tableau.com/current/pro/desktop/en-us/calculations_aggregation.htm) explains the relationship between aggregation and the level represented by marks. Our module treats totals, ratios, distinct counts, and distributions as different calculations rather than interchangeable options in a chart menu.

[Order of operations](https://help.tableau.com/current/pro/desktop/en-us/order_of_operations.htm) provides concrete cases where filter order changes a top-N question or a percentage denominator. This motivates independent fixtures for “within this selection” versus “of the whole population.” Both may be useful; an interface must distinguish them.

[How Explain Data works](https://help.tableau.com/current/pro/desktop/en-us/explain_data_explained.htm) limits generated explanations to exploring relationships and explicitly distinguishes them from causal proof or hypothesis testing. This is also relevant to AI-generated summaries: an explanation should expose its evidence and limits rather than acquire authority through fluent wording.

### Qlik: selection, evaluation, and color are separate

[The associative selection model](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Selections/associative-selection-model.htm) distinguishes several states around selected and excluded values. An excluded value can retain analytical meaning; it is not the same as missing data, zero, or denied access. The portable principle is explicit state semantics, not adopting Qlik's particular selection colors.

[Creating KPIs](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/KPI/create-kpis.htm) documents conditional ranges, symbols, and expressions. The page displayed an update date of **2026-09-15** when retrieved. These configurable facilities demonstrate implementation flexibility, not evidence that a chosen cutoff is correct. Our procedure therefore adds threshold provenance and boundary checks.

[Assigning colors to measure values](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Colors/assigning-colors-to-measure-values.htm) distinguishes ways to map measure ranges to color. An audit must establish whether a color expresses relative position, fixed magnitude, or an approved operational condition. Similar appearances can convey materially different claims.

### IBM Carbon: attention should follow meaning

[Status indicators](https://carbondesignsystem.com/patterns/status-indicator-pattern/) relates indicators to severity and other states, with labels and shapes supporting interpretation. It also leaves status choices dependent on product needs. The audit therefore separates urgency, lifecycle, selection, and data quality, instead of applying one unexplained red/amber/green scale across a business application.

[Chart anatomy](https://carbondesignsystem.com/data-visualization/chart-anatomy/) identifies the roles of chart text, labels, and supporting values. Essential context belongs near the comparison it qualifies. This page explicitly identifies itself as work in progress; its guidance does not establish that every depicted widget or implementation is accessible or complete.

### ASA: importance and statistical significance differ

The [ASA's March 7, 2016 announcement of its p-value statement](https://www.amstat.org/docs/default-source/amstat-documents/p-valuestatement.pdf) separates statistical significance from practical importance and cautions against decisions based only on a cutoff. The audit therefore distinguishes measured change, business materiality, statistical evidence, and causality. An older methodological source can remain relevant; its age must not be disguised as a newly published design trend.

## Independent procedures derived from this research

The module introduces a reusable meaning contract: question, definition, unit, grain, time, population, reference, interpretation, trust, and continuation. Each usage points to the authoritative definition while retaining its own filters and comparison context. This prevents a shared component from being treated as proof that every dataset and role interprets it identically.

It uses successive review passes over the full inventory: meaning; comparison; trust and attention; exploration; then decision usefulness and presentation. Changes trigger a review of affected dependencies. This is a practical ordering for the skill, not a sequence claimed to be prescribed by any one source.

Missing features are classified by feasibility: existing evidence that needs presentation; a derivation that needs validation; a new data or workflow dependency; or an unproven idea. A useful proposal names the decision it improves, its inputs, its owner, and how its behavior could be verified. It does not imply that a backend, forecasting model, transaction, or permission already exists.

Domain examples cover operations, inventory, finance, customer service, and projects. They are prompts for investigation, not universal KPI catalogs or specialist policy recommendations. The synthetic aggregation example has deliberately unequal group sizes so that a misleading average is easy to detect. It is original instructional data and was not taken from a real application.

## Retrieval and validation limits

- Public documentation bodies and the ASA PDF text were retrieved through web research. Product behavior was not tested in signed-in Power BI, Tableau, or Qlik environments; no enterprise tenant or customer dataset was accessed.
- The links use current documentation routes where available. Continuously updated documentation is not a pinned software release. Retrieval date is **2026-09-16**; a date shown by a search engine was not treated as a publication date.
- The ASA PDF itself dates the announcement to 2016, despite newer crawler metadata. Carbon's chart-anatomy page declares work-in-progress status. These limits remain attached to the findings.
- A singular Qlik `create-kpi.htm` URL did not retrieve. The canonical plural `create-kpis.htm` page was subsequently found and its body read; only that working source is cited.
- The research validates the rationale for audit questions. It does not establish the correctness of a project's formulas, thresholds, permissions, or source data. Those require project evidence and, where needed, an accountable domain owner.
- The new procedure has no completed cross-industry effectiveness benchmark. Structural validation of the package and declared coverage cannot establish analytical correctness, usability gains, aesthetic quality, or production readiness.

## Practical acceptance evidence

An application review should produce reproducible, authorized examples: a value recalculated from known inputs; a changed selection with a verified denominator; a comparison at its supported grain; a stale-data state that does not claim current health; and a detail route that preserves the intended subject and period. Use synthetic fixtures when sensitive data is unnecessary.

For user evaluation, ask people to state what a measure covers, explain its comparison, identify a meaningful exception, and reach the correct supporting detail or permitted next step. Observe wrong conclusions as well as completion time. A faster route to the wrong interpretation is not an improvement. Full-audit completion still requires evidence for every inventoried in-scope usage and defined transition, not a successful demonstration of these examples alone.
