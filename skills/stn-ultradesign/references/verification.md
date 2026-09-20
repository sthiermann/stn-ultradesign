# Verification of design and implementation

These are project procedures, not a certification scheme. Choose checks that can detect a plausible defect in the agreed change.

## Establish a reproducible baseline

Use the [reproducible reference recipe](concept-to-code.md#preserve-a-reproducible-reference) for concept comparison; bind the implementation revision separately. For a focused change, record only its affected before-state, restoration steps, fixture and relevant rendering/input conditions. Baselines containing personal data must be sanitized before sharing. Restore the state before comparing; a current URL does not establish which build or approved state is running.

For new UI, use representative content and at least one stressed example per significant component. For modifications, include the changed journey and shared usages likely to be affected. A whole-product audit additionally needs the inventory and coverage process in `audit-method.md`.

## Layers of evidence

| Layer | Good at detecting | Cannot establish alone |
| --- | --- | --- |
| Source review | Semantic errors, state contradictions, token drift, missing branches | Actual layout or user comprehension |
| Component interaction checks | State transitions, labels, keyboard contract in isolation | All real page integration behavior |
| End-to-end checks | Navigation, input, recovery, roles and task completion | Subjective visual quality or full accessibility |
| Automated accessibility checks | Machine-detectable rule violations | Full WCAG conformity or screen-reader usability |
| Screenshot comparison | Layout and visual changes in a fixed environment | Correct interaction, meaningful content or authority |
| Manual keyboard/AT checks | Focus order, semantics, announcements, modal behavior | Outcomes for every assistive technology |
| Usability sessions | Where representative people struggle and why | Population-level effect from a tiny sample |
| Field measurements | Real device/network performance and task signals | Causal attribution without suitable study design |

Assert observable outcomes rather than implementation trivia. Combine appropriate automation with manual interaction and rendered inspection; automated accessibility findings are only one layer of evidence.

## Verify the requirement and its interpretation

Use [requirements-conformance.md](requirements-conformance.md) to reconcile active requirements, acceptance obligations and evidence at the artifact revision being reviewed. Read the original request or answer as well as its interpreted rule. Review in both directions: find missing requirements and consequential additions without an authorized basis. Preserve the distinction between a mapped requirement, a depicted concept and verified behavior.

For a selected design language, inspect the private project profile produced by [project-research.md](project-research.md). Compare reference → interpreted project rule → rendered concept → integrated result. A consistent component family can still implement the wrong interpretation. Source reading, kit inspection, rendered specimens and observed native interactions support different claims; missing motion or target-platform evidence stays visible.

Compare equivalent tasks, content, states, dimensions and appearance settings. State when identical conditions are unavailable and which comparison remains meaningful. Check structural roles, typography, semantic color, geometry relationships, material behavior and transition/recovery sequences. Distinguish an intentional project departure, an implementation defect and an unverified approximation. A visually similar start frame does not establish identical interactions or native rendering.

The reviewer challenges the current evidence independently of the author's preferred verdict. Fixes to shared rules reopen their affected usages and applicable checks. Scope changes retain the original requirement and actual authorization; recording an exception or obtaining broad aesthetic approval cannot turn a missing obligation into a pass.

## Minimum useful interaction pass

Begin with the task and rendered interface, before reading handlers or receiving a route/control hint from the author. Apply [interaction-comprehension.md](interaction-comprehension.md): predict the target, scope and result from visible evidence, then find the entry, act, observe the outcome and return. Keep a missing entry, unclear domain meaning, unexpected behavior, visual defect and optional preference distinct. If implementation knowledge is already unavoidable, disclose that limit or use a fresh reviewer for this pass. Expert predictions are not observed user comprehension.

Apply only the steps the actual website or application supports; a content journey need not have a form or administrative action.

- Reach the task through normal navigation and a deep link if supported. Include reachable first-use, empty or unselected starts using [the critical-task walkthrough](task-flow-design.md#7-expose-missing-primary-workflows-before-presentation); record entry discoverability separately from handler correctness.
- Complete it with the main input method and keyboard.
- Exercise validation and meaningful error/retry transitions where the task supports them.
- Check Back/cancel and persistence of entered work.
- Verify success reflects actual completed work.
- Verify permission and session changes where they affect the task, using safe test environments.
- Execute the affected [state-semantics cases](feature-parity.md#preserve-state-semantics-before-replacing-the-ui), comparing expected and observed results, including state that must remain unchanged. Retain separate results for defaults, merge behavior and relevant role combinations; matching fields cannot close them.
- Reconcile baseline actions against proposed controls in both directions; identify additions separately and keep missing child actions unresolved.
- Check independent overlays, panels and preferences in the supported combinations that alter behavior, including closing, reopening, resize, return and reload persistence.
- Inspect a control from its resting state without a cue naming the target. For a surface presented as one action, activate its label, icon, internal padding and points just inside its visible edges independently, resetting the safe fixture between probes. Verify the intended outcome occurs once, secondary controls retain their own action and points outside the declared target do not activate it. Exercise the applicable pointer, touch and semantic keyboard behavior; record the actual input/device conditions and leave unavailable checks open.

Test selectors should describe user-visible roles and names where reliable. Use stable test identifiers for ambiguous structures, not brittle coordinates or incidental CSS class names. For geometry probes, derive positions from the currently rendered target, identify the hit receiver, then activate and verify the outcome. A named-control click or class assertion cannot establish the rest of the apparent surface.

For a defect crossing navigation, overlays or lifecycle, choose a focused integration check that retains the actual router, applicable guards, overlay implementation and mount/unmount behavior. Reproduce the relevant pointer-down, focus, pointer-up and click sequence, then check competing dismissal/navigation handlers, draft retention and focus return. Direct handler calls can miss this ordering. Declare replaced boundaries and mocks; a mocked guard or close callback does not prove the real boundary, even when the surrounding component passes.

## Layout and analytical integrity

Before closing affected visual obligations, execute [layout-integrity.md](layout-integrity.md) in the actual owning surfaces. Record normal and stressed content, boundary dimensions, open/transient states and intended overflow exceptions. A source declaration or clean screenshot at one width is not a responsive pass.

For widgets and data journeys, apply the [purpose and duplication review](data-visualization.md#review-purpose-and-duplication-separately) and [drilldown data chain](data-visualization.md#trace-selection-drill-and-return-as-separate-transitions). Verify visible scope and actual included/excluded records independently, with known fixture expectations. Keep usefulness, shared implementation, layout and data-outcome obligations separate so one successful check cannot hide another failure.

## Visual craft review

Render and inspect the actual result. First assess information hierarchy and task clarity at screen scale. Then inspect alignment, spacing relationships, typography, icon weight, border/radius consistency, contrast, crop, truncation, focus, disabled states and overlay stacking.

Compare with the concept at the same viewport, fixture and theme. Side-by-side images support judgment; overlay/difference images help locate drift. Investigate mismatches before changing a baseline. Legitimate font rasterization variation is different from a changed typeface or line break caused by a wrong width.

Convert known geometry failures and consequential visual feedback into targeted regression cases in the existing acceptance record. Name the exact relationship, affected usages and restored state: for example, the painted mark relative to its control, the image edge relative to the text column, or the crop relative to its container. Compare the current render at relevant widths and open states; use measurements or overlays where they can expose the discrepancy. CSS declarations and layout boxes alone may miss optical bounds, clipping or an intermediate animation pose.

Keep the agreed tolerance or allowed variation beside that case. Preserve intentional asymmetry, meaningful repetition, approved crops and useful local scrolling; similarity is not a reason to remove them. Use the planned layout-integrity contexts for adaptive review, including justified exceptions. Device presets alone do not establish boundary or content resilience.

Check forced colors, light/dark theme where supported, reduced motion and long/RTL content where applicable. Preserve scroll and focus on transitions. Test touch access to functions that otherwise appear on hover.

Inspect the painted extents of changing illustrations and controls at rest, expanded and during transitions, including any wider intermediate pose and focus rings. At affected container sizes, verify that labels, targets and focus remain clear of neighboring content and controls, and that visual layers do not intercept activation. Include reversal and reduced-motion behavior where supported. Layout-box measurements alone cannot establish visible clearance.

## Inspect the delivery surface

For visual changes, inspect the affected artifacts where people will actually consume them, within the authorized delivery workflow. A standalone image render cannot establish its integration into a page. For a GitHub README, inspect GitHub's rendered README at the intended revision, including surrounding text; a local Markdown preview is only a fallback. Apply the same distinction to an app shell, embedded widget, exported document or other host surface.

- **Identity and freshness:** Distinguish the source revision, delivered build and revision actually running in the inspected user tab. Record the delivery URL or file, viewport, usable content-column width, and selected responsive asset or variant. Confirm that the displayed asset is the expected version, using its resolved source and a hash or visible revision marker where available. After an asset change, refresh or reopen the consuming surface and verify its identity; an unverified cached preview is not evidence of the new result.
- **Cross-artifact consistency:** Reconcile product names and versions that are supposed to agree across visible artwork, headings, captions, release metadata and manifests. Read the rendered image text, including SVG text, rather than trusting filenames or source checks alone. Explain intentionally different version domains instead of forcing them to match.
- **Composition in context:** Inspect image edges, captions, badges and adjacent metadata together. Check whitespace, grouping, hierarchy, crop, legibility and wrapping at their displayed size. Correct cramped or misleading relationships; there is no universal pixel gap that proves quality.
- **Adaptive delivery:** Choose compact, medium and expanded checks according to the changed content, supported surfaces and actual content column. Desktop, tablet and phone labels or window width alone are insufficient. Verify which responsive asset is selected and how it scales inside the host; exercise relevant variant boundaries and every changed variant.

When release compatibility is in scope for an updateable website with lazy-loaded routes or assets, keep a tab on the previous build across a representative deployment, then open a previously unvisited route whose assets were not already loaded. Verify successful loading or the defined stale-asset recovery, retained recoverable work and the absence of reload loops; a fresh tab alone cannot establish this transition. Use an authorized release simulation when needed and label it. Record preview-host restrictions that prevent the check and leave the actual deployment transition unverified.

Keep source/CI results, rendered visual findings and user approval separate. A passing build, valid SVG, working link or screenshot's existence does not establish design acceptance. Report visual acceptance only for the surfaces and revisions actually inspected. If the delivery surface is inaccessible, inspect the strongest available preview and leave delivery rendering explicitly unverified. This is evidence discipline, not an additional approval gate.

## Concept conformance

Map each acceptance ID to evidence and `pass`, `fail`, `blocked` or `not-tested`. Keep unresolved failures visible. Compare fixed rules exactly and fluid behavior against its allowed range; do not demand identical pixels across different rendering environments.

A discrepancy can be a bug, an intentional approved deviation, a rendering difference, or a specification gap. Classify it before acting. Approval of a deviation records scope and replaces the specific affected decision; it does not invalidate unrelated requirements.

### Verify component families after integration

First verify semantic fit against the action-to-surface record: task, owning workspace, selected surface and steps to outcome. Then, after integration or a shared correction, reconcile the [consumer map](../assets/design-contract.template.md#shared-family-behavior) against actual imports, wrappers, local implementations and runtime entries. Add discovered consumers and their relevant contexts before closing the family. A specimen or one successful page cannot close the other usages.

Open each affected usage through its real entry at the integrated revision. Compare placement, geometry, header/actions, motion and relevant interaction states; for editors, exercise validation, save/cancel, dirty dismissal, focus entry and return using safe fixtures. For selectors, also check keyboard selection, popup placement, option details and retained draft values. Verify affected responsive transformations and reduced motion. Repeat the original failing path and the consuming usages; where a justified variant differs, check that its specialized behavior survived. Still images establish position, not transition or focus sequence.

Record family ID, usage IDs, integrated revision, context, evidence and exception status. Keep source inspection, rendered state and interaction results distinct. A usage remains unresolved when its code appears shared but its actual path has not been checked. These checks follow the requested change boundary and affected dependencies, not an unsolicited whole-product audit.

## Reconcile bindings and evidence files

When the delivery binding record is in use, run the [delivery checker](delivery-ledger.md) against the current decisions, artifacts and results with the available private evidence root. Inspect both declared readiness and integrity gaps. Keep the existing audit validator authoritative for full-audit coverage. Missing local captures, changed files or outdated execution bindings remain unresolved; updating a hash is not a recheck. The checker does not launch tests or establish authenticity.

## Stop and report accurately

Run the repository's required checks and tests proportional to the change. Repeat checks when code or evidence changes, not just to inflate confidence. If a check is unavailable, explain the missing capability and perform the strongest available alternative without claiming equivalence.

A concept with missing required pages, unresolved action mappings or lost widget/state semantics is not ready for approval of the full requested scope. A table listing the omissions makes the limit honest; it does not close it. If the owner rejects the current direction, preserve useful discovery and confirmed preferences, establish a corrected task-and-component slice, and verify it before expanding. Do not keep propagating the rejected architecture or silently restart the interview.

Separate “all implemented acceptance checks passed,” “all requested surfaces were inspected,” and “users perform the task better.” Each needs its own evidence. For release readiness, name unresolved critical/high issues and incomplete required checks; avoid a single green score that hides them.
