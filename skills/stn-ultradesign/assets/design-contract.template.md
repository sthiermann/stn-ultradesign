# Design contract

Complete only sections relevant to this project. Remove unused sections with an explicit scope reason. This file records decisions; filling it in does not create user approval.

## Identity and approval

- Project / scope:
- Contract version:
- Status: draft / in-review / approved / superseded
- Approved artifact paths and revisions:
- Approval message reference, date and approved scope:
- Superseded contract:
- Implementation revision:

## Discovery and preference basis

- Design brief path and version:
- Twenty-or-more tailored preference questions covered before the substantial direction, or narrow-scope exception:
- Confirmed answers carried forward and explicit delegation reference, if any:
- Optional preferences still treated as proposals:
- Outstanding decisions that block dependent work:
- Recommendation classes and applicability: normative requirements / platform or implementation guidance / research or heuristics / product choices / hypotheses:

## Users, tasks and constraints

- Primary actors, roles and organization scope:
- Main tasks and expected outcomes:
- Existing brand, component system, framework and browser constraints:
- Target platforms, inputs, locales, themes and accessibility target:
- Evidence supporting decisions:
- Assumptions requiring later validation:
- Explicit exclusions:

## Brand inheritance contract

- Brand brief / inheritance matrix version and applicable sources:
- Binding assets and identity rules, with actual approval/delegation scope:
- Decisions per dimension: typography, color, shape, icons, imagery, voice, layout, motion and materials:
- Exact preservation boundaries, permitted evolution and proposed departures:
- Theme-specific semantic tokens and accessible alternatives:
- Asset provenance, documented use conditions and unresolved dependencies:
- Component/surface exceptions and associated acceptance IDs:

An approved visual reference does not authorize copying its assets. Preserving corporate typography or colors does not automatically preserve a legacy layout. Record those choices separately and retain the real authorization scope.

## Agreed visual and structural rules

- Product-specific visual thesis: task, dominant work region, supporting context, density and intended character:
- Structural alternatives considered with the same task/content, and reason for the chosen composition:
- Rendered evidence for each target device class and meaningful content/state variation:
- Self-critique: consequential visible weaknesses found, revisions made and remaining craft checks:
- Owner's visual assessment: accepted / revision requested / rejected / not yet assessed; message and affected decisions:

| Decision ID | Decision | Artifact / reason | Fixed or allowed variation |
| --- | --- | --- | --- |

Include tokens, typography, icon family, layout regions, hierarchy, density, spacing, shape, elevation, motion and responsive transformation rules where relevant.

## Journeys and component states

| Flow/state ID | Actor and entry | Action and transition | Validation / side effect | Back, cancel, failure and recovery |
| --- | --- | --- | --- | --- |

## Feature preservation and supported variants

- Baseline revision, runtime context and known source changes:
- Complete old-to-new feature map path, version and reconciliation status:
- Existing functions outside this concept, their retained destinations and next stage:
- Old/new navigation map and matched comparison artifacts:
- Individually approved feature retirements: capability IDs, consequences and actual user decision references:
- Existing chart types, graph interactions and thresholds retained or specifically redesigned:
- Added capabilities and backend dependencies, separately identified:

| Feature / variant ID | Current actor, capability and resource scope | Approved destination and behavior | Locale / theme / density rules and preference persistence | Allowed variation | Acceptance IDs |
| --- | --- | --- | --- | --- | --- |

Record navigation visibility, data visibility and action authority separately where they differ. Carry supported language, light/dark/system and density choices into the contract rather than inferring their removal from a single screenshot. Broad aesthetic approval does not approve feature retirement, changes to effective permissions or loss of supported preferences. Features outside the current prototype remain required unless specifically retired.

## Acceptance and traceability

| Acceptance ID | Observable expectation | Source decision | Route/component | Test environment and method | Result and evidence |
| --- | --- | --- | --- | --- | --- |

For screenshot comparisons record browser, CSS viewport size, zoom, data fixture, fonts, locale, theme, expected scroll position and justified tolerance.

Report visual/craft assessment separately from behavioral, accessibility and syntax results. A technical pass does not satisfy an unapproved or rejected visual direction.

Report mapping completeness, depicted concept scope, implemented scope and verified feature parity separately. Verify the relevant actor/state/theme/locale/density contracts for each included feature; justify equivalence classes and retain blocked or untested variants as gaps.

## Refinement log

| Revision | User feedback | Decisions changed | Artifacts updated | Status |
| --- | --- | --- | --- | --- |

## Deviations and unresolved decisions

| ID | Conflict / reason | Proposed alternatives and impact | User decision | Affected acceptance IDs |
| --- | --- | --- | --- | --- |
