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

## Prepare questions with visible recommendations

Revisit material unknowns during semantic, visual and workflow passes and when comparing linked surfaces. Inspect available evidence and existing answers first. Ask only when the remaining uncertainty can change an interpretation, recommendation, scope or acceptance criterion; the initial interview does not finish discovery.

Every material decision question must visibly state the known situation, a preferred option or next step, why it fits, its main tradeoff and the basis for that advice. Put this guidance in the question or its displayed option descriptions, not only in private notes or a preceding message that may disappear. Distinguish an applicable normative requirement from established guidance or practice, product preference, and an untested hypothesis. Explain the relevant condition rather than treating a familiar pattern as a universal mandate. Offer meaningful alternatives and allow qualification, combinations or explicit delegation. When evidence cannot support a design preference, recommend a concrete comparison or evidence-gathering step instead of inventing certainty.

A factual question must not fabricate a recommended fact. Explain why the missing value matters, what should be measured and how the user can obtain it; accept an unknown value as unknown. Use a supported answer channel that captures the value itself, such as free text. Selecting a suggested measurement action is not the measurement; retain the same unresolved question until a value or an explicit unknown is supplied. Screen scaling and browser zoom, for instance, are separate inputs rather than interchangeable measurements. Retain known domain units and definitions; missing thresholds and backend dependencies remain unknown. Discoverable feature existence, implementation trivia and values already established by evidence do not belong in the preference interview.

A decision question could read: “The selected order must remain comparable with other rows. I recommend a details panel beside the table on wide screens because it preserves that comparison; it reduces the width available to columns. This is an established interaction pattern applied to your comparison task, not a mandatory standard. Prefer the side panel, a full-page detail with more reading space, or a comparison of both using the same order?” The answer determines this task's layout, not the placement of unrelated command menus.

## Keep one active question batch

Use the user's requested response channel. Prefer the available Q&A tool for an interactive interview; use a document as the user's response surface only when requested. If the requested channel is unavailable, explain the limitation and offer an in-conversation alternative without silently moving the interview into a file.

Default to one question at a time. A batch of up to three is appropriate only for closely related decisions when it suits the user and the tool supports it. Coordinate contributors through one active batch; do not issue a competing batch while its questions await reconciliation. Continue independent inspection instead. Before presenting another batch, match partial or delayed replies to stable question IDs and their actual presentation IDs, never to arrival order. Retain answered items and keep only unresolved items pending; a retry must not ask the user to answer completed questions again.

Use the existing brief's decision queue to track `queued`, `presented`, `answered`, `needs-clarification`, `deferred` or `delegated`, together with the source, dependent work and next action. These presentation states do not replace the authoritative requirement's decision or delivery status. Reconcile each active question as answered, delegated, or explicitly deferred before presenting the next batch. A disappeared card, empty tool return or expired wait is not an answer or delegation.

After a reasonable opportunity to answer an optional question, the interview lead may explicitly defer its presentation if the user permits moving on or the documented host behavior for an empty return permits continuing. Record that basis, the same question/presentation IDs, unanswered meaning and next action. End its active presentation through supported host behavior before opening another batch. Presentation deferral is neither an answer, approval nor delegation; preserve proposals, gaps and any true decision dependencies.

Read the actual host/tool behavior for presenting, awaiting and ending questions. If ending the response or replacing a request dismisses an unanswered card, keep the supported wait active while expecting the reply. If the card disappears or delivery is uncertain while a reply is still expected, retain the unresolved question and re-present only it through the agreed channel, correlating the new presentation with the same question ID. Describe what was observed without claiming an unverified host bug. A final message that says “I am waiting” does not preserve a request the host has already closed.

## Reconcile meaning before expanding the direction

Reuse confirmed answers within their scope. Unpack compound answers into independently changeable decisions: default versus available user choices, trigger location versus opening surface, overlay versus layout reflow, role visibility, responsive behavior and persistence. A chosen default does not authorize removing other supported choices. Keep the original wording beside the interpretation and link the resulting requirement IDs. Briefly state consequential interpretations; ask a narrow follow-up only when ambiguity changes the outcome.

Before propagating a critical workflow choice, describe its entry, selected object, opening surface, retained context and return using the observed baseline. Separate a preserved behavior from a proposed change. Terms such as “beside,” “detail” or “floating” need a concrete layout and behavior interpretation. Compare the same task, content, role and device conditions; carry unaffected decisions forward when a new answer changes one dimension.

Conflicting instructions need their exact dimensions and authority. A new reference's material treatment need not replace an earlier shape preference. Show the consequences, identify what changed and ask only about the unresolved conflict. Quantity of questions is not a completion metric; resolved material uncertainty and honest gaps are what matter.

Continue independent authorized work while answers are pending. Optional preferences may become clearly labeled, reversible proposals after a reasonable opportunity to answer, with their unanswered status retained. Reconcile any active presentation under the protocol above before presenting another batch. Required decisions about scope, feature removal, access policy or consequential behavior remain unresolved until evidence or an authorized decision settles them. Record explicit delegation and its limits. An audit answer alone does not authorize implementation.

## Cover at least twenty tailored questions early

Before developing a substantial visual direction, cover at least **twenty distinct, relevant preference questions** in the [design brief](../assets/design-brief.template.md). Ground each in the observed product and a decision it can change. Existing confirmed answers count with their sources; ask only what remains unknown. Avoid duplicate questions, discoverable facts and requests to accept accessibility as preference coverage.

Make discovery visible before a polished concept creates commitment to an unexamined direction. Prioritize structure and workflow, then visual details, using the one-active-batch protocol above. The floor is not twenty approval gates. Explicit delegation may waive remaining questions within its recorded scope; silence, impatience, missing replies and approval of another artifact do not. Keep independent preparation moving and retain the separate production-implementation approval boundary.

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
