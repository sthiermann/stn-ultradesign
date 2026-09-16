# Product thinking and evaluation

Load this reference when the problem, audience, task, information structure, success measure, or design direction is unsettled; also when an audit proposes structural changes. The procedures below are original working methods to adapt to the project’s tasks and evidence.

## 1. Establish the problem before the screen

Before choosing a substantial layout, create a short **mission, task and evidence brief** from the actual product. This is required for a substantial concept, not an optional introduction added after drawing the screen. Explain what the application helps people accomplish, what occupies their attention while doing it, and what a wrong or late result would cost. Read existing behavior and confirmed decisions before asking for meaningful unknowns. Follow [discovery and preferences](discovery-and-preferences.md) for the interview; a completed style questionnaire cannot substitute for understanding the work.

Record:

| Field | Required content |
| --- | --- |
| People | Actual roles, relevant experience, access needs, language and organizational context |
| Mission | The useful activity the application supports, expressed independently of its current screen layout |
| Trigger | What causes the person to begin, including events outside the application |
| Desired outcome | Observable change in the person's world, beyond clicking a button |
| Primary work unit | The object being observed, compared, changed or communicated: for example, a feed, incident, record, drawing, decision or conversation |
| Simultaneous work | How many objects must remain identifiable or comparable at once; observed normal and difficult cases, not an invented universal count |
| Temporal needs | Required freshness, response expectations, interruption tolerance and how stale or missing information must be recognized |
| Existing approach | Current product, workaround, colleague, document, or competing service |
| Constraints | Device, time, connectivity, permissions, data quality, interruption and handoff conditions |
| Cost of failure | Lost work, wrong decisions, exposure, financial consequences, or extra effort |
| Evidence | Observation, support record, analytics, interview, stakeholder claim, or assumption |
| Success | A measurable completion condition and the unacceptable failure conditions |

Example: “A project administrator gives a contractor access to one project, verifies the effective scope, and can revoke it later.” “Redesign the permissions modal” describes a proposed solution, not this outcome. Keep unsupported assumptions explicitly marked. A stakeholder's request and an analytics event establish different kinds of evidence.

Investigate the complete activity and its operating context before optimizing a component. A local screen improvement can move difficulty to another person or later step.

For example, in a camera observation task the work unit is the selected camera feed. A layout that replaces feeds with decorative summaries can undermine that task even when the summaries look polished. Establish whether the operator needs to notice changes across many identifiable sources or inspect detail in one image; those activities need different scales and a reliable transition between them. In an editor the work unit may instead be the document or drawing; in an access review it may be the person-resource-capability decision. Do not impose a monitoring layout on these different activities.

Ask targeted follow-ups where evidence is missing: how many objects need simultaneous attention; what delay is tolerable; which failures must remain visible during focused work; what distinguishes normal conditions from exceptions; and what context must survive interruption. Discover the product's existing refresh behavior and object counts yourself when possible. Ask about their adequacy and real use, rather than asking the owner to recite implementation facts.

**Done when:** every critical journey has a named audience, mission, primary work unit, trigger, outcome, failure cost and evidence status. Capacity and timing needs are confirmed, evidenced or explicitly open. Missing research remains a stated uncertainty; it is never filled with invented interviews or personas.

## 1a. Identify the workflow's operating pattern

Use the following original comparison aid to reason about the active task. These are overlapping workflow patterns, not mandatory page templates, fixed visual styles or claims that one industry uses only one pattern. A product can move from monitoring to triage to administration within one incident; recognize the change in task before reorganizing its interface.

| Operating pattern | Primary activity and work unit | Structural question | Example contexts and useful checks |
| --- | --- | --- | --- |
| Monitor | Maintain awareness of changing objects or processes | Which objects and critical states must remain simultaneously recognizable, and what can open on demand? | Video operations, manufacturing, logistics: object identification, freshness, exception detection and return from inspection |
| Triage | Prioritize, classify and route incoming work | Can the person distinguish urgency, ownership and the next safe action while retaining queue context? | Service desks, incident operations, moderation: correct prioritization, assignment, deferral and escalation |
| Analyze | Compare evidence to answer a question | Which views, time ranges, units and filters must remain coordinated? | Research, finance, product analysis: correct comparisons, traceable sources, missing-data interpretation and reproducible filters |
| Create or edit | Produce or modify an artifact | Does the artifact retain useful working space while tools, properties, validation and history remain reachable? | Writing, CAD, code, content production: edit accuracy, undo/recovery, save state and context retention |
| Review or decide | Assess a proposal, difference or case | Can the reviewer connect evidence, changes, consequences and the decision without losing place? | Contract review, publishing, quality assurance: explainable decisions, exceptions, version comparison and return to unresolved items |
| Administer | Change configuration, access or lifecycle state | Are target, effective scope, authority, pending changes and result unambiguous? | Business accounts, infrastructure, education platforms: correct resource selection, permission comprehension and recoverable errors |
| Communicate | Exchange information with the right people in context | Are recipients, shared context, delivery state and the distinction between draft and sent clear? | Team messaging, support, collaboration: correct audience, preserved draft, thread context and failed-send recovery |

Name the pattern for each important phase rather than assigning one fashionable archetype to the entire application. Reuse an appropriate existing arrangement when it supports the task. A pattern may suggest information relationships; it does not dictate cards, drawers, sidebars, color, density or ornament.

## 2. Describe the entire activity

Start by mapping a representative journey from entry through completion and later return to understand the product. For a full audit, continue until every defined in-scope journey and transition is mapped and inspected. Include the actual work before and after the application: collecting information, obtaining permission, explaining an outcome to another person, undoing a mistake, exporting, and resuming an interruption. Identify where information or responsibility crosses a boundary.

For each step, write what the person knows, what they must decide, what they must supply, what the system does, and what feedback proves the result. Mark duplicated entry, hidden prerequisites, unfamiliar vocabulary, ambiguous ownership, irreversible transitions and steps added only because of the current implementation. Preserve useful safeguards when removing unnecessary effort.

Separate novice discoverability from expert throughput. The same product may need visible entry points, meaningful defaults, saved views and shortcuts. A desktop specialist inspecting many records may benefit from density; an occasional phone user may need a guided sequence. Neither audience justifies breaking the other's essential tasks. Treat tablet use as its own combination of available space, touch, keyboard and multitasking.

**Done when:** each critical outcome can be traced through the full journey, including recovery and handoff; each proposed shortcut states which effort it removes and which safeguard it preserves.

## 3. Structure information around decisions

Inventory the objects people manipulate and the relationships between them. Distinguish product-wide navigation, location within the current object, and actions on that object. Use labels that describe those distinctions. Validate competing grouping options with representative tasks, not a preference poll about menu appearance.

For each decision-bearing region, establish **user question → data meaning → interpretation → next action**. A KPI, chart or record is not understood merely because its title is readable. Verify its population, units, aggregation, time and comparison where relevant; ask the domain owner when the contract is unknown. Preserve strengths, identify missing context or useful exploration as evidence-backed proposals, and never invent thresholds or business meaning. Follow [analytical-meaning.md](analytical-meaning.md).

For a navigation proposal, test whether a participant can predict where to begin without following a tutorial. For a detail page, test whether the object's identity, current state and available next action remain clear after entering from a deep link. For a workflow, check that information needed for a decision remains available at that decision point.

Use progressive disclosure for information that is genuinely conditional, with a discoverable route back. Frequent, consequential information deserves visibility. A shorter page that hides important dependencies can increase effort. Conversely, an exhaustive page that forces everyone to inspect irrelevant options can also increase effort. Choose using task frequency, consequence and research.

Give every persistent region a reason to consume working space. For navigation, headers, side panes, summaries, legends, inspectors and alerts, record the task it supports, when its information is needed, the primary work it displaces, and how people reach it when collapsed. Keep the information necessary for the current decision available. Move secondary tools on demand only when discovery, keyboard and touch access, and return are defined. Do not hide a critical failure with the optional diagnostic detail that explains it.

Compare a full-context arrangement with a focused or maximum-content arrangement when chrome competes with the primary work. Define entry, a visible exit, keyboard operation and restoration of selection, filters, time position, scroll, zoom and meaningful focus as applicable. Identify which critical alerts or state changes remain perceivable while focused. A fullscreen image that strands the person or conceals a consequential disconnection is not a completed focus workflow.

Dense layouts should reduce avoidable framing, repetition and travel before reducing text or control size. Keep the supported density choices and accessibility constraints. For imagery, distinguish thumbnails that let people identify a source and notice change from views suitable for detailed inspection. Test both scales with difficult but safe content. A larger DOM count or a greater number of tiny tiles is not proof that more useful information is visible.

Use heuristics as inspection prompts adapted to the domain. Explain the observed consequence; a familiar rule name cannot establish that a preferred layout is universally correct.

**Done when:** navigation, terminology, persistent regions and disclosure each have a task-based rationale; consequential hidden information is accounted for. Focus modes have a complete return contract and do not silently reduce required awareness.

## 4. Form and compare concepts

When the user's requested mode is concept first, make the concept reviewable before implementation. Offer meaningfully different structures only where a real decision exists. An option should state its target task, information hierarchy, interaction sequence, representative content, responsive changes and tradeoffs. Changes to hue alone are visual variations, not alternative workflow concepts.

Use the lowest fidelity that answers the uncertainty. A rough sequence can test ordering; an interactive prototype can test focus, transitions and behavior; a rendered visual sample can test hierarchy, spacing and tone. Clearly identify which states are simulated. A polished mockup does not establish technical feasibility, accessibility, data correctness or user success.

Compare alternatives under the same task, safe dataset, role, viewport, input method and relevant presentation preferences. Include realistic object counts, long labels and an adverse state. State the expected benefit in observable terms: more identifiable sources remain visible, a comparison requires less context switching, or a reviewer retains the evidence while inspecting a change. Also name the cost, such as smaller previews, a less persistent inspector or another action to reach a secondary tool. Do not select the winner solely because it looks more modern.

For data-heavy or media-heavy surfaces, connect the composition to a provisional performance budget: useful visible objects, update frequency, acceptable staleness, interaction response, rendering/decoding work, memory and network demand where relevant. Derive targets from the product's actual tasks and supported environments; an unmeasured target is a proposal. Lower preview quality, change media rate, virtualize a long list or defer offscreen work only after checking what that does to selection, keyboard access, find-in-page, comparison and monitoring. Determine whether hiding or unmounting an item also stops its data subscription. Preserve the required awareness or state the limitation before adopting the tactic. Never promise smooth performance from a static concept alone. Follow [web-engineering.md](web-engineering.md) for implementation and measurement.

Keep a concept decision log: requirement, selected option, rejected alternative, reason, open risk, and evidence. After refinement, present the concrete concept for the approval required by the user's chosen process. Record its version and approved scope. Implementation must preserve the approved hierarchy, interactions, content and visual intent; map changes back to the concept and surface meaningful deviations. This approval applies to that concept-to-implementation boundary, not unrelated work the user has already authorized. Follow the main skill's concept-to-code contract.

Evaluate reusable parts in complete pages with representative content. Use working prototypes to test behavior and interpretation; component consistency alone cannot establish a coherent product.

**Done when:** the chosen concept answers the important uncertainty, its evidence limits are visible, and any required approval has a traceable version.

## 5. Distinguish obligations, evidence and taste

Classify every significant recommendation:

| Kind | How to justify it |
| --- | --- |
| Applicable requirement | Cite the actual normative requirement and scope |
| Established platform convention | Identify the target platform and relevant guidance |
| Observed usability problem | Describe the person, task, behavior and consequence |
| Research-informed hypothesis | Name the source, context, expected benefit and local validation needed |
| Product or brand choice | Explain the expressive intent and test for functional regressions |

A design can be distinctive through typography, composition, imagery and controlled motion while remaining predictable in its behavior. Choose a coherent direction; do not average unrelated design systems into a new visual language. A particular radius, gradient, font or animation duration is not “world standard” simply because a prominent company uses it.

Judge visual changes by usefulness, comprehensibility, honest feedback and durability as well as appearance. Aesthetic resemblance to a reference is not proof of improved task performance.

**Done when:** a reviewer can distinguish a requirement, a supported finding, an assumption and a stylistic choice without inferring the distinction.

## 6. Run a study that matches the claim

Plan a small formative study to find task problems. Recruit people who match the actual role and task; include relevant access needs and a spread of experience. Give realistic scenarios without naming the interface control the participant should use. Start from a believable state and use realistic, safe data. Pilot the task wording before collecting observations.

Observe first. Record independent completion, wrong turns, critical errors, assistance, recovery, comprehension and the participant's explanation. Ask neutral follow-up questions. A preference rating cannot replace observed task success. Think-aloud can explain confusion but changes timing; use comparable conditions when making time comparisons.

Observe representative participants performing realistic tasks. Small qualitative sessions can expose common problems within a defined group; they cannot establish a population success rate.

Choose additional methods by uncertainty:

| Uncertainty | Suitable next evidence |
| --- | --- |
| Is the problem real? | Contextual observation, interviews about recent behavior, support evidence |
| Can people find the destination? | Task-based navigation or tree testing |
| Can they complete the proposed sequence? | Moderated or unmoderated task study with realistic state |
| Does a change improve outcomes at scale? | Planned controlled experiment or carefully bounded longitudinal evidence |
| Can people use assistive technology successfully? | Task tests with actual supported combinations and relevant users |
| Does the result remain useful over time? | Follow-up or field study, repeat-use outcomes and support burden |

Determine sample size from the method, audience diversity, expected effect and decision risk. Do not present “five users” as universal coverage. Quantitative superiority claims require adequate design and uncertainty analysis; an expert walkthrough alone cannot make them.

**Done when:** findings include observation, affected task, consequence, evidence strength and limitations; untested scenarios remain explicitly untested.

## 7. Measure improvement without rewarding friction

Define measures before redesign to prevent selecting only favorable results. For each measure record the goal, observable signal, event or data source, denominator, eligible population, time window, exclusions and owner. Use existing consented data; avoid collecting sensitive content solely to make a dashboard richer.

Connect product goals to observable signals and then to measurable outcomes. Select measures appropriate to the task, such as successful completion, avoidable errors, time, adoption or satisfaction; do not require every category to become a dashboard metric.

| Product goal | Candidate measure | Guardrail |
| --- | --- | --- |
| Complete an administrative task correctly | Independent correct completions / eligible attempts | Critical mistakes, accidental scope, support-assisted completion |
| Reduce repeated effort | Completion time distribution for comparable successful tasks | Accuracy and confidence in the result |
| Improve first meaningful use | Eligible newcomers achieving a defined useful outcome | Forced setup, abandoned work, inaccessible steps |
| Make recovery reliable | Successful resumption after representative interruption | Data loss, duplicate actions, repeated authentication |
| Improve analytical decisions | Correct answers to domain questions with supporting evidence | Misread uncertainty, stale data, confidence without correctness |
| Maintain useful monitoring coverage | Identifiable required objects visible under the agreed viewport/content case; response to a specified event | Missed critical status, stale imagery, illegible previews and obscured controls |
| Inspect without losing context | Successful detail inspection followed by restoration of the relevant overview state | Lost selection, changed time range, unexpected playback or inaccessible return |
| Increase useful workspace | Primary task completed with the proposed allocation of screen area | A higher area percentage alone is insufficient; retain legibility, controls and required context |

Report baseline, change, sample and limitations together. Segment where aggregate success can hide exclusion. A longer session might mean engagement or confusion; a shorter one might mean success or abandonment. Interpret using the intended outcome. Treat click count as a diagnostic, not a goal to minimize at any cost. State numerical improvement only when measured; “5000% better” is an ambition, not a test result.

**Done when:** the release or proposal has explicit outcome measures, guardrails and a follow-up method, and its evidence supports the exact claim being made.
