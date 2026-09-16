# Verification of design and implementation

These are project procedures, not a certification scheme. Choose checks that can detect a plausible defect in the agreed change.

## Establish a reproducible baseline

Record app revision, test accounts/roles, data fixtures, fonts/assets, locale, theme, viewport in CSS pixels, browser/OS and zoom. Capture the approved concept version and before-state when relevant. Baselines containing real personal data must be sanitized before sharing.

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

[Playwright's accessibility testing guide](https://playwright.dev/docs/accessibility-testing) supports automated scans while explicitly warning that automated testing cannot detect all accessibility problems. [Testing Library's guiding principles](https://testing-library.com/docs/guiding-principles/) favor checks resembling how software is used. Apply those ideas by asserting outcomes rather than implementation trivia.

## Minimum useful interaction pass

- Reach the task through normal navigation and a deep link if supported.
- Complete it with the main input method and keyboard.
- Exercise validation and at least the meaningful error/retry transition.
- Check Back/cancel and persistence of entered work.
- Verify success reflects actual completed work.
- Verify permission and session changes where they affect the task, using safe test environments.

Test selectors should describe user-visible roles and names where reliable. Use stable test identifiers for ambiguous structures, not brittle coordinates or incidental CSS class names. A test asserting that a new class exists does not prove the requested user outcome.

## Visual craft review

Render and inspect the actual result. First assess information hierarchy and task clarity at screen scale. Then inspect alignment, spacing relationships, typography, icon weight, border/radius consistency, contrast, crop, truncation, focus, disabled states and overlay stacking.

Compare with the concept at the same viewport, fixture and theme. Side-by-side images support judgment; overlay/difference images help locate drift. Investigate mismatches before changing a baseline. Legitimate font rasterization variation is different from a changed typeface or line break caused by a wrong width.

For adaptive behavior, test compact, medium and expanded spaces appropriate to the app, intermediate widths around each content breakpoint, and short heights. Include text enlargement/reflow and a real on-screen keyboard check when possible. Typical fixture sizes can aid repeatability, but are not universal design breakpoints.

Check forced colors, light/dark theme where supported, reduced motion and long/RTL content where applicable. Preserve scroll and focus on transitions. Test touch access to functions that otherwise appear on hover.

## Inspect the delivery surface

For visual changes, inspect the affected artifacts where people will actually consume them, within the authorized delivery workflow. A standalone image render cannot establish its integration into a page. For a GitHub README, inspect GitHub's rendered README at the intended revision, including surrounding text; a local Markdown preview is only a fallback. Apply the same distinction to an app shell, embedded widget, exported document or other host surface.

- **Identity and freshness:** Record the inspected revision, delivery URL or file, viewport, usable content-column width, and selected responsive asset or variant. Confirm that the displayed asset is the expected version, using its resolved source and a hash or visible revision marker where available. After an asset change, refresh or reopen the consuming surface and verify its identity; an unverified cached preview is not evidence of the new result.
- **Cross-artifact consistency:** Reconcile product names and versions that are supposed to agree across visible artwork, headings, captions, release metadata and manifests. Read the rendered image text, including SVG text, rather than trusting filenames or source checks alone. Explain intentionally different version domains instead of forcing them to match.
- **Composition in context:** Inspect image edges, captions, badges and adjacent metadata together. Check whitespace, grouping, hierarchy, crop, legibility and wrapping at their displayed size. Correct cramped or misleading relationships; there is no universal pixel gap that proves quality.
- **Adaptive delivery:** Choose compact, medium and expanded checks according to the changed content, supported surfaces and actual content column. Desktop, tablet and phone labels or window width alone are insufficient. Verify which responsive asset is selected and how it scales inside the host; exercise relevant variant boundaries and every changed variant.

Keep source/CI results, rendered visual findings and user approval separate. A passing build, valid SVG, working link or screenshot's existence does not establish design acceptance. Report visual acceptance only for the surfaces and revisions actually inspected. If the delivery surface is inaccessible, inspect the strongest available preview and leave delivery rendering explicitly unverified. This is evidence discipline, not an additional approval gate.

## Concept conformance

Map each acceptance ID to evidence and `pass`, `fail`, `blocked` or `not-tested`. Keep unresolved failures visible. Compare fixed rules exactly and fluid behavior against its allowed range; do not demand identical pixels across different rendering environments.

A discrepancy can be a bug, an intentional approved deviation, a rendering difference, or a specification gap. Classify it before acting. Approval of a deviation records scope and replaces the specific affected decision; it does not invalidate unrelated requirements.

## Stop and report accurately

Run the repository's required checks and tests proportional to the change. Repeat checks when code or evidence changes, not just to inflate confidence. If a check is unavailable, explain the missing capability and perform the strongest available alternative without claiming equivalence.

Separate “all implemented acceptance checks passed,” “all requested surfaces were inspected,” and “users perform the task better.” Each needs its own evidence. For release readiness, name unresolved critical/high issues and incomplete required checks; avoid a single green score that hides them.
