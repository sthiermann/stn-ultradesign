# Anthropic frontend design and STN Ultradesign: capability and gap review

**Access date: September 16, 2026.** This is an independent examination of public instructions and our local implementation. It is not a comparison of model output quality. No external skill, example, template, code or asset was installed, executed or incorporated into this repository.

## Identify the actual reference

The informal name `/design-skill` does not uniquely identify a public Anthropic package. The directly verified frontend package is **`frontend-design`**. Its official Claude Code manifest reports version **1.1.0**; its README describes automatic use for frontend work. That does not establish which package or revision a particular user's client has installed. [Plugin manifest](https://github.com/anthropics/claude-code/blob/df52d04a4e65195c1621fe6222e0564bcccb1804/plugins/frontend-design/.claude-plugin/plugin.json), [plugin README](https://github.com/anthropics/claude-code/blob/df52d04a4e65195c1621fe6222e0564bcccb1804/plugins/frontend-design/README.md)

A separate official **Design Plugin** covers critique, design systems, handoff, writing, accessibility and research. Its README lists several commands; it should not be silently treated as the same single frontend skill. This review does not claim to exhaust Anthropic's design tooling. [Design Plugin overview](https://github.com/anthropics/knowledge-work-plugins/blob/main/design/README.md)

Reproducible public snapshots read:

| Repository | Resolved snapshot | Relevant evidence |
| --- | --- | --- |
| `anthropics/skills` | `34040c9c568585f6929bedeaad110ad08f079624` | [Pinned frontend instruction file](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/frontend-design/SKILL.md) |
| `anthropics/claude-code` | `b782847db9a18667f00918ea341197f201b22bb4` | [Pinned corresponding plugin instruction file](https://github.com/anthropics/claude-code/blob/b782847db9a18667f00918ea341197f201b22bb4/plugins/frontend-design/skills/frontend-design/SKILL.md); identical instruction blob to the fully read earlier snapshot |

The skill repository records a September 3, 2026 revision at [`41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`](https://github.com/anthropics/skills/commit/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f). A fresh GitHub API lookup confirmed the skills snapshot as its current main revision. Claude Code main had advanced to `b782847db9a18667f00918ea341197f201b22bb4`. A fresh GitHub contents-API lookup verified that its frontend instruction file and the fully read earlier snapshot `df52d04a4e65195c1621fe6222e0564bcccb1804` both resolve to Git blob `a5333457c414d20d625f307df945842c0952ecc3` (9,390 bytes). This establishes equality of that instruction file only; the manifest and README evidence above remain pinned to their inspected earlier revision. The skill's [license file](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/frontend-design/LICENSE.txt) identifies Apache 2.0; reporting that metadata is not a decision to reuse its contents.

Anthropic itself notes that these public examples can differ from behavior in Claude products. Source inspection therefore cannot establish what every Claude installation does. [Official repository README](https://github.com/anthropics/skills/blob/main/README.md)

## What the current frontend instructions actually emphasize

The examined instruction file grounds appearance in the subject, audience and real content. It requests deliberate typography, meaningful structural devices, restrained motion, a brief-specific plan, review before implementation, and visual self-critique during building. It treats interface wording as design work and explicitly prioritizes the client's chosen direction over generic stylistic avoidance. Its focus is visual authorship and implementation discipline; the file does not specify a complete application-coverage ledger or a controlled comparative benchmark. Those absences describe this file, not all Anthropic products. [Pinned instructions](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/frontend-design/SKILL.md)

That is a stronger reference than describing the package merely as a collection of attractive colors or font bans. Conversely, an instruction to make distinctive work is not evidence that a particular generated interface achieved it.

## What Ultradesign already covers

The inspected local baseline was the September 16 working tree on commit `adb70623c077219ff91fe38517d1e829d14ae512`, including the pending task-flow, propagation and information-economy changes. Line numbers below identify that review snapshot; section names remain the more stable lookup.

| Capability examined | Actual Ultradesign evidence | Assessment |
| --- | --- | --- |
| Product-specific art direction | [Concept method](../../skills/stn-ultradesign/references/concept-to-code.md), lines 7–11; [visual systems](../../skills/stn-ultradesign/references/visual-systems.md), authored-direction section | Already requires a domain-based thesis and meaningful structural alternatives. Do not add another vague distinctiveness slogan. |
| Typography as composition | [Visual systems](../../skills/stn-ultradesign/references/visual-systems.md), typography section, lines 109–129 | Already covers rendered glyphs, roles, proportions, numerals, fallback, licensing and hierarchy. Its absence would be a false finding. |
| Purposeful structure and visual emphasis | [Visual systems](../../skills/stn-ultradesign/references/visual-systems.md), composition section, lines 50–70 | Already questions repeated wrappers and aligns emphasis with work. A universal one-button or one-panel rule would weaken complex workspaces. |
| Copy and information economy | [Workflow method](../../skills/stn-ultradesign/references/workflows.md), opening section | Already examines repeated facts, labels, helpers, accessible descriptions and recovery value. |
| Rendering and correction | [Concept method](../../skills/stn-ultradesign/references/concept-to-code.md), lines 35–59; [verification](../../skills/stn-ultradesign/references/verification.md), visual-regression section | Already requires actual target-size renders, concrete criticism, correction and fresh evidence. |
| CSS implementation discipline | [Web engineering](../../skills/stn-ultradesign/references/web-engineering.md), resilient-layout section | Already addresses cascade ordering, specificity escalation and real rendering. This is not a missing principle. |
| Approval, preservation and complete audits | [Skill entrypoint](../../skills/stn-ultradesign/SKILL.md), work modes and product contract; [design contract](../../skills/stn-ultradesign/assets/design-contract.template.md) | Explicit requirements for this package. Broader scope is useful for its intended tasks; breadth alone does not imply better visual results. |

The central problem is therefore **reliable execution of the rules**, with a few opportunities to make the visual decision process more concrete. Adding many more paragraphs would not, by itself, address the observed weakness.

## Three improvements worth implementing and testing

These proposals are independently formulated from the local files, recorded evaluation limitations and product requirements. They are development candidates, not assertions that Anthropic already implements the same procedure or that our skill has passed it.

### 1. Produce a compact, rendered direction proof before expanding a visual system

**Current weakness:** The concept method and contract name a thesis, structural alternatives and rendered artifacts, but permit those decisions to remain spread across separate prose records and screen samples. They do not define a compact artifact that demonstrates whether the proposed hierarchy survives ordinary product content before extensive implementation.

**Concrete change:** For an unsettled substantial direction, create a small proof containing the main working surface, its linked detail and one consequential control state. Use the same domain content and capability map for each structural candidate. Mark the current scope, work object, next action and return path directly in review notes. Keep the chosen direction and the strongest rejected alternative together, with the reason for selection. A narrow fix can use its affected component; an established approved composition need not be reopened.

**Independent acceptance:** A reviewer who has not read the designer's explanation can identify the main task, selected object, actionable state and route back from the artifact. They can point to visible differences between the candidates that affect work. Renaming the product must not be the only evidence of domain fit. Uncertain findings remain hypotheses until user testing. This proof helps choose a direction; it does not replace review of every affected usage or the full-audit obligation.

**Why this is more than wording:** The deliverable is a comparable rendered artifact and an explicit decision, not an additional description of how the final interface should feel.

### 2. Add a same-content typography and proportion trial when those choices are open

**Current weakness:** The typography section provides strong inspection criteria, but no repeatable selection exercise connects those criteria to a new typographic direction. A designer can list valid tokens while retaining a weak relationship among heading, data, label and action.

**Concrete change:** Where typography or density is genuinely being redesigned, render the same realistic title, paragraph, numerical comparison, field/error and action using the proposed treatment and a plausible alternative. Preserve the authorized brand boundaries. The alternative may change hierarchy, weight, measure or spacing within one approved family; it need not introduce a new font. Include the smallest relevant layout and a supported difficult locale or content case. Record the actual loaded font and fallback.

**Independent acceptance:** Compare reading order, label/value distinction, numerical discrimination, wrapping, visible workload and retained action access. Select a treatment with explicit advantages and costs. Check enlarged text and the chosen compact/comfortable state where relevant. Do not reward novelty, use an arbitrary “premium” score, or require a new typeface when the existing one works. The selected treatment must then survive the surrounding composition, not only a specimen sheet.

**Why this is more than wording:** It creates evidence that can falsify a font/scale choice before it propagates. The resulting specimens belong to the project, not to a universal aesthetic catalogue.

### 3. Complete a fresh craft evaluation and carry failures through implementation

**Current weakness:** The published evaluation records an owner-rejected synthetic concept. It also explicitly states that a full accepted concept-to-code cycle and a controlled comparison remain outstanding. Later source-only flow reviews help establish useful reasoning, but do not resolve the visual result. [Evaluation status](../quality/evaluation.md), synthetic-concept and not-yet-demonstrated sections

**Concrete change:** Execute the existing [evaluation procedure](../../skills/stn-ultradesign/references/skill-evaluation.md) with an independently authored dense working application and a different, form-oriented task. Keep content, constraints, tools, model and budget recorded. Obtain real renders, a critical-task walkthrough, an external craft critique and a revision of the identified weaknesses. Then implement only the approved direction and compare the final result with it. Keep rejected iterations visible in the record rather than publishing only the best screenshot.

**Independent acceptance:** Each consequential critique identifies a visible symptom, affected decision, concrete correction and fresh verification. Record owner acceptance separately from task success, input access and visual fidelity. Include actual target-size evidence and meaningful error/dense states. A technical pass cannot close a visual rejection, and a flattering review cannot close lost functionality. For a competitive claim, repeat matched runs under the same protocol; one accepted output is still not a superiority benchmark.

**Why this is more than wording:** The next progress measure is a completed, inspectable outcome. An extra module, citation count or package-validation pass is not a substitute.

## Integration status

The project-specific research procedure and [reference translation template](../../skills/stn-ultradesign/assets/reference-translation.template.md) now specify the direction proof and conditional typography trial from proposals 1 and 2. This is an instruction change, not evidence that every future concept will satisfy it. The complete accepted concept-to-code evaluation in proposal 3 remains outstanding.

## What should not be imported

Do not copy a competitor's instruction structure, wording, examples, templates, palette lists or assets. Do not convert its aesthetic preferences into universal bans. Keep the user's approved brand, required platform behavior, legitimate domain terminology and accessibility constraints. A useful lesson can be restated as an original decision procedure with observable evidence, without reproducing the source material.

Do not interpret broader coverage as aesthetic superiority or a short skill as inherently incomplete. Different packages target different work. This review verifies public instructions and identifies testable improvements; it does not establish which system makes better interfaces for a given user. That requires the matched evaluation described above.
