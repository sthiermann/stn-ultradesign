# Discovery and individual design preferences

Use this module throughout an audit and before a substantial new concept or redesign. Its purpose is to learn the product and the owner's intentions before committing to a recommendation or visual direction. The minimum of twenty tailored questions for a substantial concept is this skill owner's chosen working method, not a research-backed optimum or an international standard. It is a floor, not a ceiling: ask additional relevant questions when the scope exposes important unknowns, without inventing a quota of hundreds. Audits and isolated fixes have no arbitrary twenty-question minimum or maximum; ask as many meaningful questions as the work needs.

## Understand the mission before choosing the composition

Write the mandatory mission, task and evidence brief described in [product-thinking.md](product-thinking.md#1-establish-the-problem-before-the-screen) before selecting a substantial layout. Identify what the application is for, who uses it, the useful outcome, the primary work unit, the simultaneous work demand, important timing constraints and the cost of failure. Distinguish an observed product fact, a user's answer and an untested hypothesis. A generic label such as “business dashboard” does not establish these facts.

If the purpose is to observe a selected set of camera feeds, start by understanding how many feeds must remain identifiable, which changes must be noticed, and how inspection returns to the overview. Do not spend the dominant area on unrelated summary cards. If the purpose is to create a document, investigate the document and its editing tools instead. Use the workflow patterns in `product-thinking.md` to recognize monitoring, triage, analysis, creation, review, administration and communication across different industries; they are reasoning aids, not fixed styles.

For every persistent region in the proposed interface, explain its contribution to the current task and the primary work space it consumes. Identify optional content that can open on demand, a usable focused-work mode where appropriate, and the critical status that remains visible when supporting detail is hidden. Preserve keyboard/touch access and a defined return path. “Hide everything” is not an adequate monitoring or editing strategy.

## Discover facts before asking for preferences

Read project instructions and examine the existing product, routes, components, translations, theme tokens, preference storage, permission declarations and available runtime views. Establish which roles and states are observable. Continue only within the authorized access; use [the account and access boundary](../SKILL.md#keep-account-and-access-reviews-about-the-experience).

Create the current feature map using [feature-parity.md](feature-parity.md). Specifically look for personal versus administrative navigation; conditional controls; locale selection; light, dark and system preferences; compact or comfortable layouts; saved views; charts, diagrams and threshold controls. Their absence from the current screenshot is not evidence that they do not exist. Source evidence can discover a feature without proving its rendered behavior.

Separate four kinds of information:

| Record | Example | What to do |
| --- | --- | --- |
| Observed fact | Two display themes are selectable in the running product | Record environment, entry point and evidence |
| Source contract | A role-gated export action exists in source but is inaccessible in the available session | Map it and retain the runtime gap |
| Confirmed preference | The owner explicitly prefers a dense analysis workspace | Carry forward the message and its scope; do not ask again |
| Hypothesis | Occasional users may need a clearer starting point | Label it, propose how to investigate it and avoid presenting it as user research |

Do not ask whether the application has features that can be discovered. After finding a feature, ask about its importance, desired placement, friction or presentation. Do not ask the owner to select implementation trivia that follows from an established design contract.

Discover the actual dataset sizes, available refresh modes, supported media streams and current state transitions before asking about them. Then ask meaningful unknowns: which objects must be compared simultaneously; whether an observed delay is acceptable for the task; which failure needs immediate attention; and what is hard to recognize at the current preview size. A requirement for higher density is not permission to make controls or text unusably small. Distinguish recognizing an object in an overview from inspecting its details.

For company or product identity, use [brand-discovery.md](brand-discovery.md). Discover the supplied brand sources and their authority, then ask which dimensions to preserve, evolve, reinterpret or explore. Typography, color and shape inheritance do not imply that layout or navigation must remain unchanged. Carry this selective inheritance matrix into the brief and concept contract.

## Keep an adaptive interview open during the audit

Revisit material unknowns during each semantic, visual and workflow pass, and when comparing linked surfaces. The initial interview does not finish discovery. First inspect available evidence and existing answers; ask when the remaining uncertainty can change the interpretation, recommendation, scope or acceptance criterion. Do not ask the user to identify a control or value that can be inspected directly.

Ground each question in a concrete finding. Explain the affected task, what is known, what remains uncertain and which decision the answer changes. Offer a small set of meaningful options, with a recommendation and its tradeoff where the evidence supports one. Explain whether the rationale is an applicable standard, platform practice, research or heuristic, product requirement, or taste. An established pattern can inform an option without becoming a universal mandate. Allow the user to combine options, qualify them or delegate the choice.

For example, after discovering an existing comparison chart, ask which business question its comparison should answer if that purpose remains unclear; do not ask whether the chart exists. Show how an equal-length prior-period comparison and a comparison against an approved target would answer different questions. Preserve the product's known units and definitions, label missing data or backend dependencies, and do not invent a target or alert threshold. For a visual choice, compare the same content and state rather than asking whether the user wants something “more modern.”

Keep a decision queue in the brief: affected entity/pass, evidence and unknown, question, options and rationale, answer or explicit delegation, status, source and dependent work. Reuse confirmed answers across pages within their scope. New evidence can justify revisiting a decision, but explain what changed and ask only about that change. Quantity of questions is not a completion metric; resolved material uncertainty and honest remaining gaps are what matter.

Make conflicting preferences concrete. If a newly supplied reference uses rounded silhouettes while an earlier instruction requires small technical radii, distinguish inheriting the material from inheriting the shape. Show those alternatives and their consequences. If the new instruction does not clearly resolve the conflict, ask which dimension should change; do not silently discard the earlier preference or restart the entire interview.

Continue independent, authorized read-only inspection while answers are pending. Mark dependent conclusions as open rather than passing them using an assumed domain meaning. Optional stylistic choices can remain clearly labeled, reversible recommendations after a reasonable opportunity to answer. Actual dependencies concerning scope, feature removal, access policy or consequential behavior remain unresolved until evidence or an authorized decision resolves them. Record the scope of explicit delegation; silence is not delegation. An audit discussion guides recommendations without independently authorizing implementation.

## Cover at least twenty tailored questions early

Before developing the substantial visual direction, create at least **twenty distinct, relevant preference questions** in the [design brief](../assets/design-brief.template.md). Ground each in the observed product and a decision it can change. Carry forward already confirmed answers as covered questions with their source; ask only the unanswered questions. Do not count twenty paraphrases of one decision, questions about discoverable facts, or a yes/no request to accept accessibility as meaningful coverage.

Make this discovery visible to the user early, before a polished concept creates commitment to an unexamined direction. Use short batches organized around a decision, within the question tool's actual limits. Prioritize the questions that affect structure and workflow; address visual details next. If a single document suits the user's request better, offer a clearly numbered brief that allows selective answers. Avoid twenty compulsory visual choices presented simultaneously.

Explicit user delegation can waive the remaining interview: for example, an instruction to choose the design direction independently. Record that instruction and the affected decisions. Do not infer delegation from silence, impatience, a missing tool response, or approval of an unrelated artifact. Do not repeatedly ask questions the user already answered or explicitly delegated.

The question floor governs discovery, not a requirement to obtain twenty approvals. Mark each answer as `confirmed`, `pending`, `delegated` or `hypothesis`. Distinguish a genuine dependency from an optional preference. Continue authorized inventory, research and independent concept preparation while replies are pending. After a reasonable opportunity to answer, optional choices may become clearly stated, reversible proposals. Missing decisions about feature removal, real access scope or consequential side effects remain unresolved dependencies; elapsed time does not resolve them. The separate production-implementation approval boundary still applies.

## Build the interview from the actual product

The prompts below are an original question bank, not a script to send unchanged. Replace bracketed terms with observed tasks, screens and alternatives. For a substantial concept, select and adapt at least twenty meaningful questions; substitute an irrelevant topic with another product-specific decision. For an audit or focused fix, use the relevant questions and add those revealed by the work without imposing that count. Existing answers count without re-asking them.

| ID | Tailored decision prompt | Design consequence |
| --- | --- | --- |
| Q01 | Of the observed tasks [A, B, C], which should the interface make fastest? | Dominant work region and action priority |
| Q02 | Which step in [named journey] currently costs you the most attention or effort? | Workflow redesign priority |
| Q03 | What would make you judge [task] as improved after using the new design? | An observable success criterion |
| Q04 | Which existing behaviors or arrangements in [current screen] should feel familiar after the change? | Continuity and migration constraints |
| Q05 | When opening [workspace], should users first see [task-specific option A] or [option B], and why? | Starting state and hierarchy |
| Q06 | Are the discovered destination names [examples] meaningful to your users, or should their wording change? | Navigation language, with old-to-new mapping |
| Q07 | When moving from [overview] into [detail], which context should remain visible and which should be restored on return? | Selection, filters, time range and back behavior |
| Q08 | Which secondary information in [screen] should stay alongside the work, and which can open on demand? | Supporting panes and progressive disclosure |
| Q09 | How should [expert role] and [occasional role] differ in guidance or density while retaining their actual capabilities? | Role-aware presentation, without changing permissions |
| Q10 | Which complete task should remain practical on the observed phone or tablet use case? | Deliberate responsive workflow priorities |
| Q11 | For [dense view], is scanning more items or reading each item more comfortably the better default? | Default density; preserve existing density choices |
| Q12 | Where do the observed personal settings and administrative settings feel difficult to distinguish? | Scope labeling and account/admin navigation |
| Q13 | For an unavailable action in [known role context], which explanation would help users understand their next step? | Denied, disabled or request-access presentation within the real policy |
| Q14 | In [time-sensitive workflow], which events deserve immediate attention and which should remain quietly reviewable? | Alert hierarchy and interruption policy |
| Q15 | Which of two task-matched compositions makes [relationship or comparison] easier for you to understand? | Structural alternative selection, supported by concrete examples |
| Q16 | Given the existing theme choices and actual working environment, which should be the default presentation? | Theme default without silently deleting supported modes |
| Q17 | Which qualities of the current brand should remain recognizable, and which feel dated to you? | Brand continuity and permissible visual change |
| Q18 | For [specific information level], does [typographic example A] or [example B] communicate the intended emphasis better? | Type hierarchy and information character |
| Q19 | Where should the existing accent color attract attention, and where should it recede? | Accent distribution while retaining status meanings |
| Q20 | How restrained or expressive should shape, surface treatment and motion feel in [actual task context]? | Visual character, within accessibility and performance constraints |
| Q21 | With the supported languages already identified, what tone and terminology should remain consistent across them? | Localization and content direction |
| Q22 | In the discovered [chart or graph], which comparison or threshold must be understandable at a glance? | Chart emphasis while preserving data meaning and controls |
| Q23 | Which existing view preferences should users be able to keep between visits, and at what already supported scope? | Persistence and customization expectations |
| Q24 | How much structural change are you comfortable testing in [journey], given the habits it currently supports? | Innovation range and rollout sensitivity |

Add mission-specific questions where they matter. For example: “How many of these selected objects must be recognizable at the same time?”, “Which stale or failed state must remain apparent in the focused view?”, or “What delay would make this response too late for the task?” Use the discovered product's actual vocabulary and explain the layout or workflow decision each answer changes. Do not repeat answered questions just to expand the count.

Translate the answers into task-based alternatives and observable criteria before polishing the visual direction. Compare the same content, role and device conditions. Record what the user should be able to recognize, compare, complete and restore; include failure cases. Performance-related proposals such as reduced preview media rate, virtualization or deferred rendering need real measurement and a check of their effects on awareness and interaction. A simulated preview can demonstrate a proposed composition but cannot establish real media latency or operational throughput.

A preference answer is not evidence that all users share it. If the owner's taste and observed task performance point in different directions, describe the conflict plainly and propose a concrete comparison or usability check. Do not claim that a fashionable treatment is more intuitive without evidence.

## Explain why a recommendation has authority

Use a short explanation with the class, relevant source or observation, and consequence. The labels below prevent “global best practice” from becoming an unexplained veto.

| Class | Meaning in a recommendation | Boundary |
| --- | --- | --- |
| Normative standard | An applicable technical requirement, with version, criterion and conditions | Explain applicability and exceptions; do not turn an unverified legal assumption into a requirement |
| Platform or implementation guidance | A vendor convention or an informative implementation pattern suited to the target environment | Explain why it fits this product; another platform may make different choices |
| Research or heuristic | Evidence from a stated study/context, or an expert rule that suggests a useful direction | Name transfer limits; do not call a heuristic a universal law |
| Product choice | A requirement, owner preference or deliberate tradeoff for this application | Record the owner and scope; compare reasonable alternatives |
| Hypothesis | A plausible explanation or improvement not yet validated | Define the evidence that would support or reject it |

Accessibility conformance concerns the applicable normative requirements and their exceptions. Supporting explanations and interaction examples do not independently add requirements or certify a design. Verify the project’s required level and current primary guidance before making a conformance claim.

For example: “The keyboard interaction needs correction to meet the agreed accessibility target. Moving the inspector to the right is our proposed product choice because the comparison stays visible. A compact default is your preference; comfortable spacing remains available.” Separate those claims rather than calling the entire composition a worldwide standard. A chosen reference can inform a decision without becoming a universal mandate for unrelated products.

## Complete discovery without inventing certainty

The brief should contain the mission/task/evidence summary, the applicable question and decision records, known preferences, product constraints, open dependencies, meaningful alternatives and evidence classes. A substantial concept includes the twenty-or-more question records or a documented explicit delegation; an audit instead continues its adaptive interview wherever material uncertainty appears. Link the feature map and the agreed work scope. Explain which optional decisions are proposals and which dependent conclusions remain open. When concept work is authorized, use [concept-to-code.md](concept-to-code.md) to render and refine the direction, and carry accepted decisions into the contract. A completed interview does not approve a design or authorize feature removal.

The question structures and decision procedures in this module are independently authored skill policy.
