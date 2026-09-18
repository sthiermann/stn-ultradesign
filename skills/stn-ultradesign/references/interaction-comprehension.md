# Understand the surface, predict the action, verify the outcome

Read for task discovery, review of widgets and controls, or findings about confusing navigation, drilldowns, feedback or state. Apply this pass to the affected usages and real task context. Link results to existing task-flow and acceptance records; a new document per button is unnecessary. Use [analytical-meaning.md](analytical-meaning.md) for business definitions, [component-states.md](component-states.md) for interaction families, and [workflows.md](workflows.md) for state and recovery contracts.

## Establish what the person can understand

Inspect the rendered surface before reading implementation details that reveal its intended behavior. Record the intended audience and the information available at this point. Ask these questions of the actual interface:

- What object, population or activity is this about, and what is its current scope and state?
- What can I learn or decide here? For a number, where can I find its unit, period, comparison and freshness when relevant?
- What is actionable, what is selected, and what merely reports a status? Can those meanings be distinguished without color alone?
- What do I expect to happen after activating the control, and where will I remain or arrive?
- What can I do if the expected result fails, and how do I resume the previous task?

Write a concrete prediction for consequential or ambiguous actions before activation. Then exercise the action and compare that prediction, the agreed task contract and the observed result. A successful click handler does not resolve a misleading label or unexpected scope change. Expert inspection produces a reasoned finding or hypothesis; only observed participants can establish how those participants understood it. Record disagreements instead of inventing user quotations or a comprehension score.

Prefer clear structure, familiar domain language, useful labels and appropriate defaults. Add concise contextual help for genuine uncertainty. Avoid explaining every control with repeated prose or making critical meaning depend on a hover-only tooltip. A specialist may understand established terminology that a first-time user does not; test the actual audience and use case rather than rewriting all technical language indiscriminately.

## Compare the promise with the transition

Use the existing action-to-surface record. Name the verb, stable target identity, scope, immediate result and return path. Check the complete visible target and applicable keyboard/touch path, not just the small icon used in a test selector.

| Surface or action | Expectation to verify |
| --- | --- |
| Table, KPI or chart drilldown | The selected object or measure determines the destination population; visible filters, actual records and totals agree. Preserve or explicitly change the existing context. Follow [data-visualization.md](data-visualization.md#trace-selection-drill-and-return-as-separate-transitions). |
| Local tab or filter | The advertised local content changes without silently discarding unrelated work, resetting the workspace or impersonating a new global destination. |
| Link or new browser tab | The destination and meaningful scope match the label; an unexpected context switch or loss of draft is a finding. Test actual navigation and return. |
| Menu, inspector or editor | The surface matches the task, belongs to the correct workspace and opens with coherent focus, dismissal and save semantics. |
| Toggle or selection | Current and pending values are distinguishable; the control changes the object and scope it appears to govern. |
| Commit or destructive action | Target, consequence and completion state are clear; cancellation, retry or undo matches what the underlying system can actually do. |

## Observe the lifecycle rather than only the finished screen

Plan reachable states and deliberately exercise the transitions with authorized fixtures. For each operation record the state before action, immediate feedback, retained content or draft, authoritative result, recovery and accessible announcement. Distinguish these cases where they exist:

- Initial loading versus background refresh: retain useful context when safe; communicate freshness and which region is pending.
- Incremental loading versus a complete result: distinguish loaded items from matching totals and make continuation/retry understandable.
- No records versus no matches, denied access or a failed request: each has a different explanation and recovery path.
- Accepted work versus completed work: success reflects the promised authoritative milestone. A started request, optimistic display or queued job is not proof of a committed result.
- Failure versus unknown outcome: preserve work, identify affected scope and offer a safe next action. A timeout may require checking status before retrying a consequential operation.
- Changed selection versus an older response: the current object owns the visible data and feedback. Test a slow earlier request followed by a newer selection, including an older failure arriving late.

Inspect what remains actionable while pending, repeated activation, partial success and recovery after navigation where applicable. Loading feedback must not erase the task or make a local update appear to block the whole application. Check that visual feedback and assistive-technology announcements convey the same outcome without unnecessary focus movement or repeated interruption. Use [accessibility.md](accessibility.md) for applicable requirements.

## Return findings that can be resolved

For each finding record the usage and state, visible promise, observed result, affected task, evidence type and revision, consequence, proposed correction and a reproducible acceptance condition. Separate an observed defect, a domain question, a visual judgment and an optional opportunity. A proposed extra filter or widget needs a user benefit, data availability and authority; novelty alone is insufficient.

Recheck the original path after correction and the affected shared usages. Use a counterexample: a similar label with different meaning, an intentional context change, a useful repeated widget or an allowed local scroll region. Confirm that the correction preserves those valid cases. Keep comprehension, layout, state behavior and data correctness as separate outcomes; one passing result cannot close the others.
