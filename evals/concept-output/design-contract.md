# Design contract — museum-settings/v0.1

Status: **in-review; visual direction rejected by owner, revision required**. Approval message/date/scope: **none**. Production implementation: **none**. Source of requirements: this exercise's brief. Artifacts: `index.html`, `review.md`, and viewport evidence listed in `verification.md` when available. No superseded version.

## Users, constraints and exclusions

Desktop staff and tablet/phone field curators manage document-workflow settings. Preserve blue/white identity and system font. Exact current tokens and source are unavailable; samples do not establish existing behavior. Real integrations, invitations, removals, ownership transfers and server authorization are outside this prototype. Language is English, following the exercise brief. Example names and data are synthetic.

| ID | Proposed rule | Acceptance / permitted variation |
|---|---|---|
| IA-01 | Personal notifications separate from organization members and integrations | Scope heading visible on each screen; navigation preserves the distinction at every size |
| IA-02 | Current organization is named | Cross-organization switching requires a later real domain model |
| VIS-01 | System font, white surfaces, blue actions | Current exact blue maps before production; no font substitution |
| VIS-02 | Type roles 30px desktop page title, 26px phone, 16px body, 13–14px detail | Text wraps; no essential truncation; system font glyphs vary by OS |
| VIS-03 | Quiet 1px boundaries, 8px controls, 12px grouped surfaces | Optical corrections allowed within the same role system |
| LAY-01 | Desktop sidebar, narrower tablet shell, phone top section navigation | 700px prototype breakpoint; validate against real content before locking production values |
| FLOW-01 | Notification changes use explicit save/cancel | Save failure retains changes; navigation checks for unsaved changes |
| FLOW-02 | Member access is edited in a scoped dialog | Cancel has no effect; Escape dismisses; successful save returns focus |
| PERM-01 | Document role and organization management are distinct | Actual backend policy is a blocking dependency for production |
| PERM-02 | Curator preview cannot access organization configuration | UI simulation only, not evidence of server authorization |
| INT-01 | Integration overview links to configuration context | No functioning setup/disconnect promise without provider requirements |
| A11Y-01 | Native controls, labels, focus visibility, status/error text | Keyboard and device testing required; no compliance certification claimed |

## State sheet

| Component | States represented | Limit |
|---|---|---|
| Navigation | Selected, idle, focused | Browser history/deep links not implemented |
| Preference checkbox | Checked, unchecked, focus | Organization-lock policy not known |
| Save action | Disabled clean state, dirty, saving, failed/retry, success | Simulated 500ms request; no actual persistence |
| Draft protection | Keep editing, discard, Escape | Real browser unload handling not implemented |
| Member dialog | Current values, draft, cancel, save, error | Last-admin and concurrent edits await backend policy |
| Role boundary | Admin controls, curator explanation | No identity verification |
| Integration | Overview, configuration detail | Loading/failed-provider states await actual contract |

## Refinement and conformance

v0.1 was the first proposal; the owner subsequently rejected its visual direction. No approval has been received. Every change after approval must map to these IDs or an approved revision. Unseen workflows are excluded rather than silently approved. Prototype inspection validates reviewability only; production conformance requires real data, permissions, transitions, persistence and supported environments.
