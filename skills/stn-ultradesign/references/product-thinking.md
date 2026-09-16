# Product thinking and evaluation

Load this reference when the problem, audience, task, information structure, success measure, or design direction is unsettled; also when an audit proposes structural changes. The procedures below are this skill's synthesis, not a claim that one author prescribes the entire method. Source access date: 2026-09-16.

## 1. Establish the problem before the screen

Create a short task brief from project evidence. Record:

| Field | Required content |
| --- | --- |
| People | Actual roles, relevant experience, access needs, language and organizational context |
| Trigger | What causes the person to begin, including events outside the application |
| Desired outcome | Observable change in the person's world, beyond clicking a button |
| Existing approach | Current product, workaround, colleague, document, or competing service |
| Constraints | Device, time, connectivity, permissions, data quality, interruption and handoff conditions |
| Cost of failure | Lost work, wrong decisions, exposure, financial consequences, or extra effort |
| Evidence | Observation, support record, analytics, interview, stakeholder claim, or assumption |
| Success | A measurable completion condition and the unacceptable failure conditions |

Example: “A project administrator gives a contractor access to one project, verifies the effective scope, and can revoke it later.” “Redesign the permissions modal” describes a proposed solution, not this outcome. Keep unsupported assumptions explicitly marked. A stakeholder's request and an analytics event establish different kinds of evidence.

Don Norman and Eli Spencer connect human-centered work to underlying problems, local context, complete activities and iterative testing. This supports investigating the activity before optimizing an isolated component. Their community-design essay is not a prescriptive web component standard. [Primary source](https://jnd.org/community-based-human-centered-design/)

**Done when:** every critical journey has a named audience, trigger, outcome, failure cost and evidence status. Missing research remains a stated uncertainty; it is never filled with invented interviews or personas.

## 2. Describe the entire activity

Start by mapping a representative journey from entry through completion and later return to understand the product. For a full audit, continue until every defined in-scope journey and transition is mapped and inspected. Include the actual work before and after the application: collecting information, obtaining permission, explaining an outcome to another person, undoing a mistake, exporting, and resuming an interruption. Identify where information or responsibility crosses a boundary.

For each step, write what the person knows, what they must decide, what they must supply, what the system does, and what feedback proves the result. Mark duplicated entry, hidden prerequisites, unfamiliar vocabulary, ambiguous ownership, irreversible transitions and steps added only because of the current implementation. Preserve useful safeguards when removing unnecessary effort.

Separate novice discoverability from expert throughput. The same product may need visible entry points, meaningful defaults, saved views and shortcuts. A desktop specialist inspecting many records may benefit from density; an occasional phone user may need a guided sequence. Neither audience justifies breaking the other's essential tasks. Treat tablet use as its own combination of available space, touch, keyboard and multitasking.

**Done when:** each critical outcome can be traced through the full journey, including recovery and handoff; each proposed shortcut states which effort it removes and which safeguard it preserves.

## 3. Structure information around decisions

Inventory the objects people manipulate and the relationships between them. Distinguish product-wide navigation, location within the current object, and actions on that object. Use labels that describe those distinctions. Validate competing grouping options with representative tasks, not a preference poll about menu appearance.

For a navigation proposal, test whether a participant can predict where to begin without following a tutorial. For a detail page, test whether the object's identity, current state and available next action remain clear after entering from a deep link. For a workflow, check that information needed for a decision remains available at that decision point.

Use progressive disclosure for information that is genuinely conditional, with a discoverable route back. Frequent, consequential information deserves visibility. A shorter page that hides important dependencies can increase effort. Conversely, an exhaustive page that forces everyone to inspect irrelevant options can also increase effort. Choose using task frequency, consequence and research.

Jakob Nielsen's heuristics are broad inspection aids rather than specific layout laws. Ben Shneiderman explicitly calls for adaptation to each domain. Apply them to explain an observed problem, not to give an unsupported design preference the status of a universal rule. [Nielsen](https://www.nngroup.com/articles/ten-usability-heuristics/), [Shneiderman](https://www.cs.umd.edu/users/ben/goldenrules.html)

**Done when:** navigation, terminology and disclosure each have a task-based rationale; consequential hidden information is accounted for.

## 4. Form and compare concepts

When the user's requested mode is concept first, make the concept reviewable before implementation. Offer meaningfully different structures only where a real decision exists. An option should state its target task, information hierarchy, interaction sequence, representative content, responsive changes and tradeoffs. Changes to hue alone are visual variations, not alternative workflow concepts.

Use the lowest fidelity that answers the uncertainty. A rough sequence can test ordering; an interactive prototype can test focus, transitions and behavior; a rendered visual sample can test hierarchy, spacing and tone. Clearly identify which states are simulated. A polished mockup does not establish technical feasibility, accessibility, data correctness or user success.

Keep a concept decision log: requirement, selected option, rejected alternative, reason, open risk, and evidence. After refinement, present the concrete concept for the approval required by the user's chosen process. Record its version and approved scope. Implementation must preserve the approved hierarchy, interactions, content and visual intent; map changes back to the concept and surface meaningful deviations. This approval applies to that concept-to-implementation boundary, not unrelated work the user has already authorized. Follow the main skill's concept-to-code contract.

Brad Frost's component model links reusable parts with complete pages containing representative content. Julie Zhuo's 2025 essay advocates learning through working prototypes. The latter is a practitioner position, not experimental proof that documentation or specialist review is obsolete. [Frost](https://atomicdesign.bradfrost.com/chapter-2/), [Zhuo](https://lg.substack.com/p/the-death-of-product-development)

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

Dieter Rams provides a philosophy of useful, understandable, honest and durable design. Bruce Tognazzini argues that aesthetic changes should be assessed against user performance. Neither source proves that all software should look like a Braun product or an Apple interface. [Rams](https://www.vitsoe.com/us/about/good-design), [Tognazzini](https://asktog.com/atc/principles-of-interaction-design/)

**Done when:** a reviewer can distinguish a requirement, a supported finding, an assumption and a stylistic choice without inferring the distinction.

## 6. Run a study that matches the claim

Plan a small formative study to find task problems. Recruit people who match the actual role and task; include relevant access needs and a spread of experience. Give realistic scenarios without naming the interface control the participant should use. Start from a believable state and use realistic, safe data. Pilot the task wording before collecting observations.

Observe first. Record independent completion, wrong turns, critical errors, assistance, recovery, comprehension and the participant's explanation. Ask neutral follow-up questions. A preference rating cannot replace observed task success. Think-aloud can explain confusion but changes timing; use comparable conditions when making time comparisons.

NN/g describes qualitative usability testing as observation of realistic participants performing realistic tasks. Its small-study guidance concerns discovering common problems in a defined group, not proving a population success rate. [Usability Testing 101](https://www.nngroup.com/articles/usability-testing-101/)

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

Google researchers Rodden, Hutchinson and Fu present HEART and a goals-to-metrics process for user-centered measurement. Use its categories selectively rather than treating every category as a required KPI. [Original publication page](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/)

| Product goal | Candidate measure | Guardrail |
| --- | --- | --- |
| Complete an administrative task correctly | Independent correct completions / eligible attempts | Critical mistakes, accidental scope, support-assisted completion |
| Reduce repeated effort | Completion time distribution for comparable successful tasks | Accuracy and confidence in the result |
| Improve first meaningful use | Eligible newcomers achieving a defined useful outcome | Forced setup, abandoned work, inaccessible steps |
| Make recovery reliable | Successful resumption after representative interruption | Data loss, duplicate actions, repeated authentication |
| Improve analytical decisions | Correct answers to domain questions with supporting evidence | Misread uncertainty, stale data, confidence without correctness |

Report baseline, change, sample and limitations together. Segment where aggregate success can hide exclusion. A longer session might mean engagement or confusion; a shorter one might mean success or abandonment. Interpret using the intended outcome. Treat click count as a diagnostic, not a goal to minimize at any cost. State numerical improvement only when measured; “5000% better” is an ambition, not a test result.

**Done when:** the release or proposal has explicit outcome measures, guardrails and a follow-up method, and its evidence supports the exact claim being made.
