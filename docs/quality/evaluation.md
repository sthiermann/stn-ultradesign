# Evaluation status of version 0.2.0

As of September 16, 2026. This version has been checked for package consistency, audit-validator behavior and selected skill decisions. This does not establish universal design superiority, complete WCAG conformance or a particular improvement factor.

## Technical package checks

| Check | Result | What it establishes |
| --- | --- | --- |
| Repository-specific validator | Passed after the English documentation update, including local Markdown references | File destinations and package consistency; no online link validation or content certification |
| 10 release/artwork consistency regression tests | Passed locally | Current README release vs. manifests, referenced image existence and labelled SVG version text; no visual spacing test |
| 24 behavioral tests for `audit_coverage.py` | Passed | Handling of ledger records, not the behavior of an actual application |
| Skill validator supplied with Codex | Passed | Frontmatter, name and format; no measurement of recommendation quality |
| Plugin validator supplied with Codex | Passed | Package manifest and skill metadata; no installation test |
| Claude Code plugin manifest, `--strict` | Passed without warnings | Formal plugin validation |
| Claude Code marketplace, `--strict` | Passed without warnings | Formal marketplace validation |

The recorded final Python checks used Python 3.12.14; Claude manifest validation used Claude Code 2.1.263. The 24 tests cover successful coverage, investigated defects versus passing product behavior, blocked/untested cases, incomplete discovery, context obligations, graph references, API contracts, evidence methods, older formats, scope changes, legitimate nonapplicability, invalid references/duplicates and malformed data types. They test observable validator behavior rather than mirroring implementation details.

The repository-specific validator also checks package names, versions, expected files, local Markdown references, Python syntax and JSON. It is a small project tool, not a substitute for complete client schemas. Both commands run from the repository root without additional Python packages:

```sh
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

GitHub Actions runs the same two commands with Python 3.12. The first [published CI run](https://github.com/sthiermann/stn-ultradesign/actions/runs/35088621779), for commit `31ed66c026eb0c5a15fc63ab2b23767963348c6a`, completed successfully. The subsequent [verified CI run](https://github.com/sthiermann/stn-ultradesign/actions/runs/35088920740), for commit `a11cec8`, also succeeded. The [English 0.2 publication run](https://github.com/sthiermann/stn-ultradesign/actions/runs/35093327247), for commit `4294fe0`, also completed successfully. These results belong to those published revisions; they do not pre-validate later changes. Official Codex validators were run separately in the development environment with Python 3.12 and PyYAML; their source code and dependencies are not distributed in this package.

The independently authored repository artwork was also rendered with librsvg and visually inspected at wide and narrow presentation widths: 1280px for the wide versions and 390px for the compact versions. All four SVGs passed XML checks and contain no scripts, images, `foreignObject`, `use`, `href`, external assets or fonts. Local picture sources and alternative text were checked. These checks establish local artwork rendering, not aesthetic acceptance or client installation. The published GitHub README was subsequently inspected at measured CSS viewports of 1280px and 390px. English text, version 0.2.0, loaded SVGs and the mobile picture sources were verified. At 390px all three tables stayed within the 324px article width and the document had no horizontal overflow. Review found a stale artwork version and undersized captions at intermediate widths; those were corrected, with a wider breakpoint for the compact artwork and reduced repeated copy. These checks do not establish owner acceptance.

### Owner-reported README regression

A subsequent owner review identified contradictory release labelling in the displayed artwork and insufficient space between the hero and release metadata. The earlier visual pass did not adequately verify the complete published composition; successful package checks did not catch this defect.

The hero artwork is now version-free. README images use content-specific filenames for both wide and compact sources, and each picture has its own paragraph. The introduction and entry links precede release metadata; the package-check badge is a separate paragraph. The reusable verification method now requires inspection of the actual delivery surface, matching visible release information, adjacent spacing, the usable content width and the loaded asset revision. The published correction at `0af3e4f` was inspected on GitHub at 1280, 768 and 390 CSS pixels. Content columns measured 838, 406 and 324 pixels. The selected hero and method artwork loaded at each width; the wide hero displayed no version label, compact sources selected at the two smaller widths, and no document-level horizontal overflow was observed. Image-to-following-paragraph gaps measured 22 CSS pixels; release metadata now follows the introduction and entry links. This describes the inspected result, not a universal spacing rule or owner acceptance.

## Independent synthetic audit run

The evaluating agent received the skill, a bounded task and an independently created three-page application. Its [audit report](../../evals/audit-result.md) records browser interactions, source locations and outstanding checks. The [fixture](../../evals/audit-fixture/index.html) contains invented content and simulated actions only. These independent tasks ran during development, before the subsequent revision of machine-readable coverage validation. They are not fresh end-to-end tests of that later version.

According to the recorded observations, Microsoft Edge on macOS was used to open all three main pages, both project drilldowns, webhook details and all three dialog exits. The report contains ten prioritized findings, including a keyboard-inaccessible save action, lost draft content on error, incomplete dialog behavior and a misleading chart scale. It distinguishes direct observations, source-based inferences and untested assumptions. Accessibility-tree observations are explicitly not represented as screen-reader listening tests.

Later visual inspection was blocked by a locked session. Responsive states, a complete keyboard matrix, actual touch/screen-reader use and the full WCAG criteria register remained unresolved. Screenshots were viewed during the run but not archived as files. No complete-audit claim is made. Ten findings are an output count from this one run, not measured detection accuracy against a blinded reference catalog.

## Independent synthetic concept run

A second task requested a reviewable settings concept for an invented museum product. Production implementation was not approved. The agent created an [isolated HTML prototype](../../evals/concept-output/index.html), [discussion notes](../../evals/concept-output/review.md) and a [design contract](../../evals/concept-output/design-contract.md).

The result separates personal notifications, member permissions and integrations. It labels assumptions, simulated data, unknown backend rules and pending user decisions. No production project was changed, and approval was not fabricated.

The [concept verification record](../../evals/concept-output/verification.md) reports passing HTML-structure and JavaScript-syntax checks. Browser startup and local preview were blocked in the original test environment. That independent run established no rendered screenshot, measured viewport, runtime journey or assistive interaction.

Subsequently, the coordinating agent viewed the notification-settings screen in a browser with a 1280 × 720 view. The interface was visible and coherently arranged in that single state. This was a limited visual check of one view, not a separately measured CSS viewport. Other states, saving, keyboard behavior, responsive adaptation and screen-reader use were not checked during that follow-up. It established no concept or production approval.

**Aesthetic outcome: rejected by the owner; revision remains open.** The owner rated the visible synthetic concept 5/6 and criticized generic components and unconvincing layout, arrangement, colors, shapes, structure and workflows. The limited rendering check is therefore explicitly not a design-quality pass. This concept is retained as a development finding, not as an endorsed example of the skill's intended quality.

In response, the concept and visual-design instructions were substantially expanded: a product-specific visual thesis, structural alternatives, deliberately designed information relationships, typography and density, plus rendered review at target sizes with concrete self-critique. Revising instructions does not prove that a new design will satisfy the owner. A fresh evaluation remains necessary; individual colors, fonts or effects were not elevated into universal quality rules.

## Review of the skill instructions

A separate review found a material contradiction: two specialist modules could require additional concept approval and implementation during audit-only work. The modules now distinguish audit, concept and already authorized implementation. Existing approval is respected; full audits retain mandatory review of every usage and every defined relevant transition. This correction was checked by rereading the instructions, not by another independent application run.

Another review identified five gaps in the original machine-readable coverage validation. Free-form evidence strings and one combined percentage could overstate source-only reviews, samples or concealed access gaps. **Schema 2** now separates inventory, contexts, planned obligations and results. It checks usage and transition relationships, requires suitable declared evidence methods including API observations for relevant transitions, and distinguishes an agreed partial scope from the original full request. An approved sample does not complete the original full audit. Missing access remains unresolved; it is not legitimate nonapplicability. Schema-1 ledgers are explicitly rejected and require fresh reconciliation.

An independent countercheck confirmed the 24 tests and additional cases involving exclusively source-classified evidence, approved sampling, a blocked administrator context and downgraded transition/API obligations. Each prevented full completion. An additional local robustness exercise produced structured results without exceptions for 1,862 data-type mutations. These checks do not authenticate evidence or discover unknown application pages: the inventory, behavior classes and actual observations still need professional review. A valid ledger does not establish aesthetic excellence.

The later discovery/preferences and feature-parity additions require tailored early questions, explicit distinction between evidence and preferences, and a mapping from existing to proposed capabilities. Existing actions, roles, states, languages, themes and density choices must not disappear without an agreed change. An independent read-only review examined these modules, their templates, skill routing, privacy boundaries and README claims. It found a scope contradiction: unqualified feature-mapping instructions could expand a focused change into a whole-product exercise.

The skill, parity reference, feature-map template and README now distinguish full-product redesigns from bounded changes. A full-product redesign still maps every discovered capability; a focused change maps its requested scope plus transitively affected shared usages and dependencies. Audit-only work records the current baseline without requiring invented destinations. The corrected wording was reread and the repository validator passed. These are instruction and package checks, not a new independent application run. The new rules still require that practical evaluation; adding modules does not increase the count of successfully evaluated workflows.

The purpose-first, navigation/materials and web implementation references were expanded using current primary documentation, including Apple WWDC26 transcripts. The brand-discovery module received an independent read-only review for selective inheritance, source authority, existing user decisions, asset provenance, accessible variants and approval scope. No material contradiction was found in that review. These are research and instruction checks; they do not establish successful application of every new rule to a complete product.

The component-state module and deeper Apple material research extend the method with state composition, control-pattern selection and brand-bound materials. These additions were source-reviewed and linked into the skill and design contract. They have not yet completed an independent application evaluation across all component families.

The analytical-meaning method, analytical surface template and adaptive audit interview received an independent read-only consistency review across the specialist modules, audit method, product-thinking rules, skill routing, README and discovery reference. It found no material scope or approval contradiction. The rules preserve authorized populations, require threshold authority, distinguish vendor patterns from standards and apply to each in-scope usage and relevant drill/return path. This was a document review, not an independent application run or fresh validation of every external source. The reference-fidelity extension likewise requires rendered comparison and honest owner feedback; it is not itself evidence of successful visual fidelity.

## Not yet demonstrated

There is no controlled comparative study against other skills, no study with representative users, and no recorded installation test across every supported client version. A complete concept-to-code run with actual user approval and subsequent conformance evidence also remains outstanding. The [evaluation procedure](../../skills/stn-ultradesign/references/skill-evaluation.md) describes the next verifiable steps.

Published evaluation files are synthetic development examples only. They contain no data from a real user's application. Paths in archived tasks and reports were normalized for this repository; the audit fixture itself was left unchanged. Account and access-control sections evaluate the user experience of legitimate product workflows. These runs do not claim penetration testing, collection of credentials or certification of backend security.


## Fresh task-flow evaluation — 2026-09-16

A separate agent received only the current skill, an original logistics task and its deliberately incomplete HTML source. It did not receive an expected answer, earlier evaluation reports, research notes or the private development concept. The [archived report](../../evals/flow-review.md) identifies seven grouped findings, including unreachable scan/statistics detail, inert filters, missing search, unrelated animated measurements, ineffective pause, lost return context and undisclosed scope gaps. It preserves known capabilities, distinguishes uncertainty from defects, and proposes fourteen acceptance checks. The [input task](../../evals/flow-fixture/task.md) and fixture are available for repeat runs. Source hashes identify the evaluated snapshot; subsequent documentation additions do not retroactively change that run.

This was a source-only forward application, not a rendered concept, usability test, performance benchmark or proof of visual quality. The fixture is intentionally defective and does not represent product-wide generalization. A separate adversarial review of the public working changes found no actionable contradictions or catalogue reconciliation errors at its recorded snapshot. It did not revalidate external sources or render the application. These checks add evidence of instruction use and package consistency; they do not establish world-leading results or owner acceptance.
