# Feature preservation and old-to-new traceability

Use this module whenever a concept, redesign or implementation changes an existing product. The default is to preserve its capabilities and explain their new presentation. A calmer screen is not an improvement if a needed workflow, graph, permission distinction or preference silently disappears. The rules here are original delivery policy for this skill, not a claim that every product should retain every feature forever.

Establish the requested boundary before mapping. For a full-product redesign, map every discovered capability, including capabilities not shown in the first prototype. For a bounded concept or focused fix, map the requested change and all transitively affected shared usages and dependencies. For example, a local dialog change need not inventory unrelated charts, but a shared dialog primitive change must account for its affected usages. Unchanged areas outside that impact boundary retain their existing behavior; do not turn them into new design deliverables or an unsolicited full audit. If a newly discovered dependency is affected, expand the impact map and its checks accordingly.

For audit-only work, record the current baseline and gaps using `audit-method.md`. No proposed destination, redesign disposition or concept approval is required. A requested full audit still inspects every discovered entity and usage in its full scope; this proportional redesign rule does not reduce that coverage.

## Establish the baseline

Record the source revision, working-tree changes relevant to the UI, runtime environment and date. Reconcile source routes, navigation, dialogs, drilldowns, conditional components, documentation and observed behavior. Identify the available actors and access scopes. If only a normal user's session is available, keep administrative surfaces discovered in source as explicit runtime gaps. Never label them absent merely because that user cannot reach them.

Create a feature map using [the template](../assets/feature-map.template.md). Give each capability a stable ID and link it to the audit's surface, usage, workflow and transition IDs where applicable. A feature is a meaningful user outcome or control with a behavior contract, not just a menu item. Split a row when actors, side effects, state behavior or preservation decisions differ. For example, viewing a chart, editing its threshold and exporting its underlying data can require separate rows even when they share one widget.

### Reconcile controls, states and simultaneous work

Do a control-by-control pass within the requested scope before designing its replacement. A page label such as “dashboard” or “messaging” is not a feature inventory. Cross-check rendered controls with source handlers, conditional branches, stored preferences and documented behavior. Inspect toolbar overflow, object menus, hover/focus controls, keyboard commands, empty states, edit modes and role-dependent entries. Keep source-only findings separate from runtime observations. A feature may exist without appearing in the opening screenshot.

For each actionable control, record its verb, target, scope, preconditions, entry points, result, persistence and reversal. Separate actions with different contracts even when their labels look similar: selecting a saved view, creating one, changing its contents, reordering items, editing its layout, sharing it and deleting it are not one “view management” capability. Preserve the supported subset; do not invent the others.

Identify independently controlled state. A label overlay, status icons, object privacy, recognition filters, on-object metrics and a statistics inspector may have separate controls and different scopes. Do not collapse them into one “details” toggle unless that behavioral change is explicitly agreed. Record whether a choice affects one object, the current view, this user or everyone; visual hiding does not change processing, recording, access or data retention unless the actual contract says so.

Map combinations that users can intentionally use together. Two independently available features can still lose parity when a redesign makes them mutually exclusive. Record whether inspection, inline statistics, messaging, editing and the main workspace may coexist; which selected object each follows; whether opening one closes another; and what survives closing, resizing, switching views or returning. Test the supported combinations that change behavior or available work area, not an arbitrary Cartesian product.

Use the [capability walkthrough](../assets/capability-walkthrough.template.md) to reconcile old controls against proposed controls and supported combinations. Every discovered action gets a mapped outcome or an explicit gap. A feature group is useful for presentation but cannot hide unfinished child actions.

Discover at least these dimensions where the product supports them within the requested scope and its affected dependencies:

- Main destinations, nested views, deep links, command menus, context menus, dialogs, drawers, widgets and all defined drilldown levels.
- Normal user, administrator and other discovered role capabilities; resource scope and conditions; navigation visibility, available actions and permission-denied states.
- All supported locales, the language picker, translated errors and messages, locale-specific formats, text expansion and direction where applicable.
- Light, dark and system-following modes if present; preference scope, persistence, initial rendering and user override.
- Existing density modes, saved views, columns, filters, sorting, panel sizes and other persistent display preferences.
- Existing charts and graph types; data series, units, domains, time ranges, legends, interactions, drilldowns, exports and accessible alternatives.
- Thresholds, reference bands, alert rules and limits; values, units, boundaries, editing rights, validation, persistence and operational consequences.
- Loading, empty, partial, stale, error, denied, interrupted, success and recovery states that each capability can actually reach.

Do not invent organizations, projects, billing, themes or preferences to fill this list. Mark a dimension inapplicable only with evidence or a clearly stated product constraint. An uninspected implementation is unknown, not inapplicable. A full audit still follows [audit-method.md](audit-method.md); this map adds redesign traceability and cannot replace usage-level coverage.

## Map every affected capability before presenting the concept

For every capability in the requested scope or its affected dependencies, record the current location and entry path; actor, permission and resource scope; interactions and outputs; meaningful states; supported variants; and a proposed location. In a full-product redesign, this includes every discovered capability. Include a destination for mapped capabilities even when the answer is “unchanged in the existing application, outside this prototype.” Do not leave a missing feature to be inferred from a beautiful screenshot. Unaffected capabilities outside a bounded assignment do not need individual redesign records.

Use these dispositions consistently:

| Disposition | Meaning | Required evidence or decision |
| --- | --- | --- |
| `preserved` | Capability remains in the same place with its behavior retained | Old/new contract and planned verification |
| `moved` | Capability remains available through a different entry or destination | Old/new path, discoverability and navigation/back contract |
| `redesigned` | Presentation or interaction changes while the required outcome and capabilities remain | Explicit behavioral delta, retained semantics and acceptance checks |
| `outside-current-prototype` | Capability remains required, but this concept artifact does not yet depict or simulate it | Existing or planned destination, reason, next stage and owner; no retirement implied |
| `explicitly-approved-retired` | A specific capability is intentionally removed with the user's informed authorization | Actual decision message, affected capability IDs, consequences and scope |

Keep discovery status, proposed disposition, user decision and implementation verification in separate fields. “Mapped” is not “implemented”; “redesigned” is not “approved”; “outside-current-prototype” is not a pass. A feature still being considered for removal remains required until the user makes the specific decision. Record the proposal in open decisions instead of prematurely labeling it retired.

General aesthetic approval, liking a screenshot, an instruction to simplify, or approval of a partial prototype is not authorization to remove unshown functionality. Before retirement, show what becomes unavailable, to which actors, and the effect on data, saved links, workflows and recovery. Link the actual user decision. If the user already gave an unambiguous, specific instruction to remove that capability, use it without asking again.

## Preserve access meaning while improving its presentation

Build the view from real capabilities rather than guessing that an `admin` role can do everything. Record separately:

1. Whether a destination is discoverable and reachable.
2. Whether data can be read at the current resource scope.
3. Which actions are enabled and under what conditions.
4. What explanation and recovery appear when an action is unavailable.

A redesign may group permission labels into readable domains, but it must retain the individual grants and their actual combinations. Do not merge reading connection details, editing configuration, assigning a role and revealing a secret into an undifferentiated “Manage” permission. A role matrix can have broad comparison columns only if each cell still identifies its real action and underlying contract. Every old permission and condition within the mapped scope needs a mapping, including those not displayed in the current concept.

Keep personal account settings distinct from installation, organization or project administration according to the product's actual scope model. A new navigation label does not change ownership or authority. Explain a moved control's actor and scope in the comparison. See [business-administration.md](business-administration.md) and [identity-permissions.md](identity-permissions.md).

UI inspection establishes presentation behavior, not server-side authorization. Preserve known API contracts and identify backend dependencies. Use the access and privacy boundary in `SKILL.md`; feature discovery is not permission to obtain secrets or alter real roles.

When editing a partially visible collection or configuration, establish whether saving merges changes or replaces the whole collection. Hidden or unauthorized entries must not become implicit deletions merely because they are absent from the editor. Preserve those entries without revealing their contents, or clearly limit editing when the backend cannot safely retain them. Verify save, cancel and concurrent updates under the relevant restricted role with safe fixtures. This applies to saved views, shared lists, group membership and other scoped collections that actually exist in the product.

## Treat supported preferences as product capabilities

Preserve the user's ability to choose each existing language, theme and density mode unless a specific change is approved. A dark concept does not approve removing light mode. An English screenshot does not approve losing translated navigation, errors, dialogs or accessible names. A spacious layout does not approve deleting an expert's compact view.

For each preference, map its entry point, supported choices, default selection, ownership scope, persistence and interaction with other preferences. Record changes explicitly: moving language selection from a header to account settings, for example, changes discoverability even when the translation files remain intact. Do not reset saved user choices merely because their new storage location differs.

Define the approved role/theme/locale/density behavior in the design contract. Enumerate the relevant combinations for each affected surface; do not blindly multiply every global option across the application. Where equivalence is claimed, justify it with implementation and rendered evidence. A distinct compact renderer or an administrator-only toolbar needs its own checks. Test text growth, wrapping, forms, tables, chart legends and dialogs in the supported variants that can change them. Accessible contrast and focus remain necessary in each supported presentation; a token definition alone is not rendered proof.

## Preserve charts, graphs and thresholds by meaning

A different chart type is a redesign decision, not a harmless reskin. Capture the old question it answers, the data/aggregation contract, units, domain, comparison baseline, missing-value meaning and available interactions. Record which of these remain unchanged and explain any intentional difference. Include filters, series toggles, synchronized selection, zoom, history, drilldowns, table alternatives and exports that users can currently reach.

For every threshold or reference band, record the measured quantity, unit, source of the value, inclusive/exclusive boundary where specified, level or severity meaning, and whether it is informational or triggers a real rule. Preserve editing rights, validation, units, save/failure behavior and audit expectations. If hysteresis, delays or reset conditions exist, map them too. Do not invent those mechanisms when the product has none. Do not replace a configured operational threshold with a decorative “healthy” zone or change a numeric boundary to make a graph look better.

Use synthetic data when evidence would otherwise reveal sensitive operational details. Label it and preserve the underlying shape of the test case. Follow [data-visualization.md](data-visualization.md) for chart decisions; record an unavailable real-data check as a gap.

## Make the comparison understandable

Start with the user's own familiar terms and demonstrate “where did it go?” For each moved or redesigned capability in the review scope, begin at the normal destination, locate its new entry without implementation knowledge, perform the proposed action with a safe fixture, show the resulting state and return. Include the relevant role and compact layout when they change access. A tooltip, dead button, navigation label or prose promise does not demonstrate the workflow.

Group the review around real work so the user does not need to read a long ledger: configure a workspace; observe it with selected overlays; inspect a problem while preserving context; coordinate through a conversation; return to monitoring. Use only activities the product actually supports. Keep missing branches in the external review record, never as fake product outages or denials. When a familiar action is still absent, say exactly which one and keep its coverage open.

Include a capability-preservation summary with every substantial concept revision, in the user's language: what stays, what moves and its exact new entry, what changes in interaction, what remains undesigned, and what needs an explicit decision. Link each consequential item to its feature ID and role/variant contract. Make the summary available beside the concept, not only in implementation notes. A user should be able to locate a familiar feature without reverse-engineering the mockup. If a capability appears unnecessary or its meaning is unclear, preserve it provisionally and ask about its actual use before proposing removal. General approval of a cleaner aesthetic is never approval of that removal.

Present a short explanation beside the full feature map. Show an old/new navigation map and matched screenshots or annotated wireframes for consequential moves. Describe a concrete journey in ordinary language: where the person starts, what they can still do, what changed, and how they return. Mark prototype-only omissions visibly, with their mapped destination. Screenshots must use safe content and identify whether they show observed, simulated or proposed behavior.

For each major change, state the benefit and cost. “The export action moves beside the chart it exports; the same roles, fields and formats remain available” is reviewable. “Administration is simpler” does not establish that its functions survived. Demonstrate role-specific views when the distinction affects understanding; do not portray one unrestricted view as everyone's application.

Keep added capabilities separate from preserved ones. An attractive new activity history, permission request flow or chart interaction may require backend work. Mark that dependency and establish whether the addition is already authorized; otherwise obtain approval for its scope. Do not describe it as an existing feature or count it as proof of parity.

## Close parity at the correct stage

Before concept review, every capability within the requested scope and its affected dependencies has a traceable disposition, even if not all are designed yet; a full-product redesign includes every discovered capability. Before implementation, the approved scope and affected shared usages have explicit old-to-new behavior and variant contracts; proposed retirements are either specifically approved or retained. During implementation, link capability IDs to code and acceptance checks.

Before declaring the redesign complete, verify each included capability in its relevant actor, state and presentation contexts. Compare old and new outputs, navigation, recovery and preference persistence. Report separately: inventory completeness, mapping completeness, concept coverage, implemented coverage and verified parity. Do not give all five the same percentage.

Reconcile in both directions: every baseline action must have a destination, and every proposed control must have a baseline capability or an explicitly identified addition. Then check supported combinations and persistence separately. A passing parent group cannot close a missing child action. An interactive concept demonstrates the proposed interaction only; production parity also needs actual backend, permission and persistence evidence.

An unfinished or blocked feature stays visible as such. A scoped prototype can be complete as a prototype while large parts of the existing application remain outside it; say that explicitly. It cannot establish full application parity. If the application changes during the work, record the baseline delta, reconcile new or changed capabilities and reopen affected checks before making a completion claim.
