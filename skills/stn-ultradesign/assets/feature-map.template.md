# Current-to-proposed feature map

Use [feature preservation](../references/feature-parity.md). This map records capabilities and redesign decisions; it does not replace a full audit's surface, usage and transition inventory.

For a full-product redesign, map every discovered capability. For a bounded concept or focused fix, map the requested scope and all transitively affected shared usages and dependencies; do not require individual redesign records for unrelated, unchanged areas. For audit-only work, use the current audit inventory instead; proposed paths and dispositions are not required.

## Baseline and discovery

- Requested work mode and change boundary:
- Transitively affected shared usages and dependencies, with impact evidence:
- Unaffected areas outside this assignment, retained without redesign:
- Source revision / relevant working-tree changes:
- Runtime environment / observed date:
- Actors and scopes actually observed:
- Source-only or unavailable areas:
- Audit inventory and reconciliation evidence:
- Concept revision and scope:
- Mapping owner and last reconciliation date:
- Changes discovered after the baseline:

## Capability index

Map every capability in the requested scope and its affected dependencies, including mapped features outside the current prototype. A full-product redesign includes every discovered capability. Give separate IDs to actions with materially different actors, effects or state behavior. Link the detailed records below rather than forcing every detail into this index.

Use [capability-walkthrough.template.md](capability-walkthrough.template.md) for the control-by-control reconciliation, independent state and supported panel combinations. A parent feature group does not cover its unmapped or unverified child actions.

| Feature ID | Capability / outcome | Current path and evidence | Proposed path | Disposition | Decision status / source | Detail record and acceptance IDs |
| --- | --- | --- | --- | --- | --- | --- |

Allowed dispositions: `preserved`, `moved`, `redesigned`, `outside-current-prototype`, `explicitly-approved-retired`. An unconfirmed retirement is an open proposal, not an approved disposition. Outside the prototype still means required unless specifically retired.

## Detailed capability record — repeat per feature or justified group

- Feature ID / associated audit surface, usage, widget and transition IDs:
- User outcome and existing entry points, deep links and drilldowns:
- Existing user-facing label / parent group / individual action IDs:
- Discovery status: runtime-observed / source-observed / documentation-only / unknown:
- Baseline evidence, method and limitations:
- Actor, capability keys, resource scope and conditions:
- Navigation visibility / data visibility / action availability / denial explanation:
- Interaction, inputs, validation, outputs and side effects:
- Back, cancel, interruption, failure and recovery:
- Relevant loading, empty, partial, stale, error and success states:
- Supported locale, theme, density, input and layout variants:
- Preference ownership, persistence and current stored-choice behavior:
- Independent toggles, supported simultaneous panels and cross-control dependencies:
- Closing, reopening, resizing, view switching and reload behavior:
- Proposed entry, destination and behavior delta:
- Disposition and current approval status:
- If outside the prototype: retained destination, next stage and owner:
- If specifically retired: user decision reference, affected actors/data/workflows and agreed transition:
- Added backend or platform dependency, if any:
- Concept artifact, implementation reference and acceptance IDs:
- Verification status and evidence; unresolved gaps:

## Preference and presentation variants

| Variant ID | Existing choice and entry point | Default / scope / persistence | Affected features | Proposed behavior | Relevant verification contexts | Evidence / gap |
| --- | --- | --- | --- | --- | --- | --- |

Include existing languages, light/dark/system modes, density choices, saved filters, columns and views. Do not invent unsupported options. Justify any equivalence used to bound checks.

## Charts, graphs and operational thresholds

| Visualization ID | Feature IDs / existing type and purpose | Series, aggregation, units, domain and missing values | Interactions, exports and drilldowns | Threshold source, boundary, meaning and edit rights | Proposed change / retained contract | Evidence and acceptance IDs |
| --- | --- | --- | --- | --- | --- | --- |

Use a separate detailed record if needed for thresholds, delayed triggers or reset conditions. Do not replace operational values or meanings with decorative examples without clearly identifying the simulation.

## User-facing comparison

- Old/new navigation map:
- Matched screenshots or annotated views, with observed/proposed/simulated labels:
- Important moves explained as concrete journeys:
- Demonstrated retrieval of each moved action, including outcome and return:
- Role-specific differences shown:
- Features not yet depicted, with their retained destinations:
- Specific removal decisions, if any:
- Additions and their implementation dependencies:

## Completion accounting

| Claim | Included IDs / total known | Completed IDs | Gaps and reason | Supporting evidence |
| --- | --- | --- | --- | --- |
| Inventory reconciled | | | | |
| Old-to-new mapping complete | | | | |
| Concept scope depicted | | | | |
| Approved scope implemented | | | | |
| Behavioral and variant parity verified | | | | |

These are different claims. A filled table, approved screenshot or working sample cannot establish full product parity.
