# Platform and visual design-system research

Research and access date: **September 16, 2026**. Primary sources; no ranking of the “best” companies. The selection covers native platforms, collaborative software, creative tools, enterprise applications and a Chinese enterprise-design context. It does not represent every country, culture or use context.

## Method and limits

`D` means the page was opened directly and relevant text read. `I` means the official page returned a JavaScript shell, while relevant official content was accessible through its search index. `R` identifies vendor research with limited generalizability. The access date is not a publication date. Search-engine crawl dates are not reliable version evidence.

The sources below contain **vendor guidance**, not globally binding standards. A separate module covers accessibility, semantics and security boundaries. The delivered reference rules are an independently authored, testable synthesis. Improvement requires evidence from actual tasks; “5,000% better” or “100 times better” cannot be established without defined comparisons and measures.

## Source register and findings

| ID | Primary source | Status | Observation and application |
|---|---|---|---|
| P01 | [Apple HIG: Materials](https://developer.apple.com/design/human-interface-guidelines/materials) | I; indexed change log through 2025-09-09 | Liquid Glass distinguishes functional controls/navigation from content. Use it selectively; conventional materials structure content. This does not justify glass surfaces on every card. |
| P02 | [Apple WWDC25: Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/) | D; official transcript | Transparency, contrast and motion form a coordinated system. System components respond to accessibility settings. CSS blur alone does not reproduce this behavior. |
| P03 | [Apple HIG: Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | I; HIG | Layout considers safe areas, window size, orientation, text enlargement and localization. Desktop windows and split-screen iPads expose the limits of fixed device categories. |
| P04 | [Apple HIG: Typography](https://developer.apple.com/design/human-interface-guidelines/typography) | I; official index via change parameter; log through 2025-12-16 | Text must remain readable when enlarged; native text styles support Dynamic Type on supported platforms. This page states that macOS does not support Dynamic Type. Do not transfer native guarantees to React web applications. |
| P05 | [Apple HIG: Color](https://developer.apple.com/design/human-interface-guidelines/color) | I; official index via change parameter | Use semantic colors, accommodate appearance modes and communicate meaning beyond color. Cultural color meanings vary, including financial price movements. |
| P06 | [Apple: Reduced Motion evaluation criteria](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria) | D; App Store declaration guidance | Reduced motion requires checking actual triggers. Simulated depth, parallax and animated blur are relevant cases. This guidance is not a web conformance standard. |
| P07 | [Material Design 3](https://m3.material.io/) | I; official homepage; index includes I/O 2026 | The current presentation connects M3 Expressive with color, shape, typography, motion and adaptive components. Announcements and implementation availability require separate verification. |
| P08 | [Google Design: Expressive research](https://design.google/library/expressive-material-design-google-research) | D, R | Google reports 46 studies and more than 18,000 participants. Individual attention results are not universal success rates. Counterexamples include unfamiliar playlist structure and removed labels reducing usability. |
| P09 | [Android: Support different display sizes](https://developer.android.com/develop/adaptive-apps/guides/support-different-display-sizes) | D; document date 2026-09-02 | Relevant space is the application window or component container. State should survive layout changes. This source is Android-specific; applying its reasoning to React is an architectural decision. |
| P10 | [Android: Canonical layouts](https://developer.android.com/develop/ui/views/layout/canonical-layouts?hl=en) | D; Views documentation | List-detail, feed and supporting-pane patterns provide useful structures. Additional space can show simultaneous context; smaller windows need clear transitions and return navigation. |
| P11 | [Compose Material 3 release notes](https://developer.android.com/jetpack/androidx/releases/compose-material3) | D; release overview through 2026-09-09 | The page separates stable and experimental releases. An announced component is not automatically a stable feature of every library. Recheck versions during implementation. |
| P12 | [Fluent 2: Design principles](https://fluent2.microsoft.design/design-principles) | D | Platform familiarity, focused task completion, inclusion and recognizable brand moments. Microsoft's identity is not a neutral design goal for unrelated products. |
| P13 | [Fluent 2: Layout](https://fluent2.microsoft.design/layout) | D | Fluent uses a four-unit basis with optical exceptions and different grid behaviors. There is no universal requirement for twelve columns or an eight-pixel grid. |
| P14 | [Fluent 2: Material](https://fluent2.microsoft.design/material) | D | Solid, Acrylic, Mica and Smoke serve different purposes. Technical availability matters; Mica is not a transparent glass pane in this system. |
| P15 | [Carbon: 2x Grid](https://carbondesignsystem.com/elements/2x-grid/overview/) | D; current domain, not the v10 archive | IBM explains geometry and rhythm through its 2x grid. Fixed, fluid and hybrid structures support different tasks. IBM-specific spacing is not a global standard. |
| P16 | [Carbon: Typography](https://carbondesignsystem.com/elements/typography/overview/) | D | Productive and expressive typography differ by content and use. Marketing titles do not establish default sizing for operational tables, editors or settings. |
| P17 | [Spectrum: Platform scale](https://spectrum.adobe.com/page/platform-scale/) | I; relatively old index; check version context | Spectrum distinguishes placement space from input targets. This informs density decisions; do not copy older device- or width-based scaling rules without review. |
| P18 | [React Spectrum V3: Theming](https://react-spectrum.adobe.com/v3/theming.html) | D; explicitly V3 | This implementation distinguishes fine and coarse input for scaling. Physical device names alone are insufficient. Claims apply to this library generation. |
| P19 | [Atlassian: Spacing](https://atlassian.design/foundations/spacing) | D | A limited token set supports rhythm, grouping and optical corrections. Tokens do not replace inspection of visible alignment. |
| P20 | [Atlassian: Typography](https://atlassian.design/foundations/typography) | D | Current product and marketing fonts differ; typography tokens combine several properties. Semantic heading structure and visual size need deliberate coordination. Do not reuse fonts without appropriate licensing. |
| P21 | [Salesforce: Compare SLDS versions](https://developer.salesforce.com/docs/platform/lwc/guide/create-components-css-slds1-slds2.html) | D | SLDS 2 separates structure and styling through styling hooks; Cosmos is a specific platform context. Migration must consider themes, components and actual runtime together. |
| P22 | [Shopify: Polaris unified for the web](https://www.shopify.com/partners/blog/polaris-unified-and-for-the-web) | D; vendor announcement | Polaris is being unified through web components. Using React does not establish that an older React-specific Polaris example is still the correct integration. |
| P23 | [Shopify: Using Polaris web components](https://shopify.dev/docs/api/polaris/using-polaris-web-components) | D; UI-extension context | Components provide support, but authors must check labels, headings and complete interactions. Remote-DOM extensions, App Home and ordinary web DOM are not equivalent. |
| P24 | [Cloudscape: Content density](https://cloudscape.design/foundation/visual-foundation/content-density/) | D | Comfortable is Cloudscape's default; Compact targets data-rich tasks. Density concerns information organization and input targets, not merely reduced padding. |
| P25 | [Cloudscape: Layout](https://cloudscape.design/foundation/visual-foundation/layout/) | D | Application, page and section structures solve different problems. An information-rich workspace needs different constraints from a reading page. |
| P26 | [Cloudscape: Configurable dashboard](https://cloudscape.design/patterns/general/service-dashboard/configurable-dashboard/) | D | Configurable dashboards give control over content, size and arrangement. Benefits must match tasks, and configuration itself requires understandable interactions. |
| P27 | [Ant Design: Design values](https://ant.design/docs/spec/values/) | D; current domain | Ant emphasizes predictable, work-oriented interaction and reusable rules. Do not generalize unsupported cognitive percentages on the page. |

## Principal synthesis

1. **Modernity includes behavior.** Window resizing, input changes, enlarged text, dark appearance, reduced motion and real failures belong to design. A modern screenshot demonstrates little of this.
2. **Choose a coherent foundation.** First inspect an existing product's language. Combining Apple, Google, Microsoft and IBM details does not produce consistency by itself. Reasoning can transfer; appearance requires a brand decision.
3. **Separate standards, platform guidance and hypotheses.** An error indicated only in red differs fundamentally from a preference for softer corners. Label findings, vendor recommendations and design hypotheses appropriately.
4. **Density follows tasks.** Analytical comparisons, creative tools and occasional consumer tasks need different space allocation. Useful measures include completion, errors, search effort and context switching.
5. **Use expression deliberately.** Attention can become clearer without inventing navigation anew. Vendor research supports experiments, not universal improvement multipliers.
6. **Check implementation currency.** Versioned components, themes and input systems need verification. A design system may announce a direction before every runtime provides stable APIs.
7. **Test global use concretely.** Translation, writing direction, scripts, formats and cultural meaning need real fixtures. A library's origin does not replace local research.

## Application in the skill

- `references/visual-systems.md`: hierarchy, composition, tokens, typography, color, shape, surfaces, components, widgets and motion, with decision and acceptance tables.
- `references/platform-adaptation.md`: adaptation to space, input and tasks; native/web boundaries and transition checks.

These modules contain original review procedures, not reproductions of vendor manuals. They guarantee neither expert enthusiasm nor legal compliance. Design review alone does not demonstrate improvement before representative people attempt the relevant tasks.
