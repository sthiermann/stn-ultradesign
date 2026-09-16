# Brand discovery and selective inheritance

Use this module when proposing a substantial visual concept, redesign, new product surface or relationship between products. Discover the company's identity and the product's existing visual language before choosing a direction. A brand may be established, intentionally changing, incomplete or absent. Record which situation the evidence supports. Do not invent a corporate identity from a company name or treat the current website as a binding design manual.

These are independently authored working rules for this skill. They are not an international branding standard. Use [product-thinking.md](product-thinking.md) to establish the mission and tasks first, and [discovery-and-preferences.md](discovery-and-preferences.md) to distinguish standards, guidance, evidence and preferences. Brand expression must support the work the product exists to do.

## 1. Establish identity, sources and authority

Identify the company, product, audience and relevant brand owner from the project and the user's instructions. Read provided brand guidelines, approved design files, asset libraries, existing tokens and components, and relevant project documentation. Examine the actual product and its supported themes and languages. If public company materials are relevant, confirm the correct organization before researching them. Separate corporate identity from a product identity, a campaign and an outdated implementation.

Record each useful source with its location, version or observation date, applicable product/channel, and authority:

| Source class | How to use it |
| --- | --- |
| Binding guideline | Apply the stated rule within its documented scope; record any conflict with the task or technical constraints |
| Previously approved decision | Carry forward the exact decision and scope; do not request the same approval again |
| Existing product implementation | Discover continuity, conventions and reusable assets; do not assume every legacy choice is mandatory |
| Supplied reference or mood material | Extract the qualities the user values; do not treat it as authorization to reproduce the design or assets |
| Proposed direction | Label it as a proposal, with the reason and the decision still needed |

Find the rules for logos and naming, typography, colors, shapes, icons, illustration and photography, tone, layout grids, motion and surface materials. Note missing coverage instead of filling it with invented brand rules. Conflicting sources need an explicit interpretation: for example, a newer product guideline may cover application controls while a corporate manual covers the logo. Do not silently choose a document merely because it looks newer or more polished.

Discover assets only within the authorized project and supplied materials. Brand discovery does not require passwords, private keys, session credentials or unrelated account access. Continue useful analysis when a missing guideline affects only one part of the design.

## 2. Ask about meaningful unknowns

Reuse confirmed answers from the existing brief. These prompts belong in the overall tailored discovery interview; they are not twenty additional mandatory questions. The twenty-question floor for substantial concepts remains a skill-specific working method, not a fixed questionnaire. Ask additional questions when material brand decisions remain unresolved, and skip questions whose answers are already discoverable.

Adapt the following to the product:

1. Which company and product identity should this interface represent, and is their relationship already defined?
2. Which supplied guidelines, logos, font files or design libraries are current and applicable to this product?
3. Which materials are binding, and which are examples of a feeling or direction you like?
4. Which existing qualities must remain immediately recognizable to customers or staff?
5. For the observed colors, typography, shapes, icons and imagery, what should stay exact, evolve within limits, or become open to exploration?
6. How much of the current layout and navigation should remain familiar, separately from how much of the visual styling should change?
7. Which brand qualities should support the main task, and which currently compete with it?
8. How should the identity behave across the existing light, dark and system modes, languages and density preferences?
9. Who can decide changes within this project's actual approval process, and which decisions are already delegated or approved?
10. If this is part of a product family, which elements need continuity across products and which may express a distinct product identity?
11. If customer branding, partner branding or multiple brands actually exist, which identity has precedence in each relevant scope?
12. If an asset's intended use is undocumented, where is its license or permission record, or which authorized alternative should the concept use?

Questions about product families, co-branding or customer themes apply only when relevant. Do not invent enterprise complexity. Ask for the location or interpretation of ordinary brand materials, not confidential account information. Explain what each unanswered question changes in the concept. Optional stylistic unknowns can remain reversible proposals; do not turn them into hidden approval gates.

## 3. Choose inheritance separately for each dimension

Create a selective inheritance matrix. Avoid a single instruction to “keep the brand” or “make everything new”: a product can preserve its logo, evolve its color roles, reinterpret its typography and explore a new layout at the same time.

Use these dispositions with a written degree of change:

- **Preserve:** retain the established asset, rule or behavior within its known allowed variants. Responsive adaptation still needs to respect the applicable rule.
- **Evolve:** retain recognizable characteristics while making bounded changes; name the characteristics and the permitted changes.
- **Reinterpret:** retain an identified principle or quality while proposing a substantially different execution; show the relationship explicitly.
- **Explore:** compare original alternatives without implying an approved new identity. Record what, if anything, remains constrained.

“Slightly” or “80% retained” is insufficient by itself. Use observable boundaries such as “keep the approved wordmark unchanged; adjust the surrounding spacing,” or “retain the accent hue family, but compare theme-specific tones for controls.” The examples describe possible decisions, not defaults.

| Dimension | Inspect and record | Decision to make explicit |
| --- | --- | --- |
| Name and logo | Approved variants, clear space, minimum use conditions, product naming | Exact assets and allowed placement or responsive variants |
| Typography | Approved families, weights, language coverage, existing fallback behavior | Family continuity, hierarchy, reading density and fallback treatment |
| Color | Brand palette and current semantic uses | Which hues are identity anchors; which tones and roles may change |
| Shape | Corners, outlines, silhouettes and recurring geometry | Which shapes remain recognizable and where controls need different treatment |
| Iconography | Existing set, stroke/fill style, labels and meaning | Reuse, adaptation or original replacement; preserve semantic recognition |
| Imagery | Photography, illustrations, crops, subjects and asset provenance | Appropriate subjects and degree of visual continuity |
| Voice | Names, labels, instructions, errors and terminology across languages | Tone, clarity and terms that must remain stable |
| Layout | Grid, alignment, spacing, navigation, hierarchy and content rhythm | Structural inheritance separately from visual styling |
| Motion | Existing transitions, feedback and task timing | Character, purpose, reduction and performance boundaries |
| Materials | Flat or elevated surfaces, transparency, blur, textures and depth | Where treatment helps hierarchy and which conditions need a simpler fallback |

For every applicable row, include the source, authority, current expression, disposition, degree of change, affected screens/components, role/theme/locale/density conditions, proposed expression, acceptance criteria and decision status. A component may need a specific exception; record it instead of silently overriding the matrix. Distinguish product-wide rules from a single surface or campaign.

Brand changes cannot silently retire features, move controls outside a role's reach, alter authorization or change chart and threshold meaning. Maintain the [feature map](feature-parity.md). A request to preserve brand styling does not automatically require preserving a confusing workflow; propose and explain the workflow change separately.

## 4. Translate identity into usable design rules

Translate the accepted direction into the visual contract and implementation tokens described in [visual-systems.md](visual-systems.md). Keep identity primitives separate from functional roles. A palette hue is not automatically the correct foreground, action, selection, warning or focus color. Define those roles and their states, then verify the combinations in the real composition.

Provide appropriate light, dark and system-mode mappings where supported. Preserve the intended identity while checking actual foreground/background combinations, focus, boundaries and charts under the agreed [accessibility target](accessibility.md). Identical raw color values across themes are not a required outcome. If a binding palette cannot serve a functional role accessibly, show a concrete tonal variant, neutral treatment or other authorized option and explain the conflict. Do not silently recolor protected logo artwork or claim that an entire interface is exempt because its colors are branded.

Specify typography with real content: long labels, localized strings, numbers, tables, dense views and supported scripts. Inspect fallback behavior and layout stability. Do not choose a font only from a large display specimen and assume it works for operational text. Record proposed fallback families and any unverified language or weight coverage.

Use shape, spacing and material treatments consistently while preserving usable controls and content area. A rounded logo does not require every table, panel and button to become a rounded card. A brand's expressive marketing style may need a more restrained expression during sustained monitoring or editing; explain the product-specific choice. Use [navigation-and-materials.md](navigation-and-materials.md) for task-fit navigation and surface decisions.

Specify motion by trigger, purpose, state transition and reduced-motion behavior. Test translucent or textured surfaces over representative content, not only an ideal background. Preserve critical status, legibility and a usable fallback. Treat any unverified rendering cost as a hypothesis to measure, not evidence that a visual treatment is performant.

## 5. Keep asset provenance separate from visual inspiration

Maintain an asset register for reused logos, fonts, icons, photos and illustrations. Record the exact asset, its source, version, intended use, available license or permission evidence, and any known restrictions. Distinguish supplied assets, existing authorized project assets, original work and external references.

Do not claim rights clearance because an asset is publicly visible, already appears on a website or was found through image search. A reference can inform discussion of color, composition or tone without authorizing reuse of its artwork, code or distinctive composition. Do not copy another person's skill, template or implementation to reproduce the reference.

For fonts, record whether the intended delivery—such as web embedding or distribution with the application—is documented by the available license. Do not infer coverage from the presence of a font file. For unverified assets, label the dependency and use an original or otherwise authorized alternative for independent concept work. Do not fabricate a license conclusion or describe an assumption as legal clearance.

Reuse user-provided or existing project materials within the established authorization and applicable documented conditions. Avoid an unnecessary new permission request when the user has already authorized that use. If a concrete restriction prevents the intended action, explain the exact asset, proposed use and missing decision; continue work that does not depend on it.

## 6. Make the direction reviewable and traceable

Add a concise brand section to the project's [design brief](../assets/design-brief.template.md): identity, evidence and authority, confirmed preferences, inheritance matrix, asset register, conflicts and open decisions. Link it from the feature map when a visual change affects a familiar location or interaction.

Show alternatives with the same task, content, role and device conditions. Explain what each inherits, what it changes, and why that helps the work. A mood board alone does not demonstrate the resulting interface. Include representative ordinary and difficult states, theme variants, long localized content and the relevant density choices before calling the direction verified.

Carry accepted decisions into the [design contract](../assets/design-contract.template.md): token roles, assets, typography, layout boundaries, component exceptions, states and device/theme/locale/density coverage. Distinguish an approved brand direction from an approved complete concept and from authorization to implement it. Follow [concept-to-code.md](concept-to-code.md) for the existing approval and fidelity process.

Honor the actual approval scope. Do not invent a brand-owner sign-off step if none is required by the user or applicable project instructions. Do not re-ask an approved decision, and do not contact another person without authorization. When a later conflict requires changing an accepted rule, present the concrete affected change and its consequences; avoid reopening unrelated decisions.

Before handing off, check that every applicable brand dimension has evidence or an explicit unknown, every proposed departure is visible, asset assumptions are accurately labeled, and the rendered concept follows the recorded matrix. Report untested combinations and unresolved decisions honestly. Brand continuity is demonstrated through these concrete relationships, not through an unsupported claim that the interface “matches the brand.”
