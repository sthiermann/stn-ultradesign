# Privacy and audit scope

STN Ultradesign reviews **interfaces and user journeys**. Account and access workflows mean how people sign in, recover access, understand roles, manage their own settings and navigate API-access controls. They do not mean collecting credentials or investigating private identities.

## Work with safe evidence

- Let the user sign in, use an already authenticated session, or use explicitly authorized synthetic test accounts.
- Never request passwords, one-time codes, recovery codes, live API tokens, private keys or session cookies in the conversation.
- Do not search password managers, secret files, `.env` contents, browser cookies or session storage to obtain access. Missing access is an audit gap, not a reason to bypass protection.
- Use redacted fixtures and synthetic data for concepts, screenshots, examples and shared findings. Do not include real credentials, private messages or customer data in public artifacts.
- Inspect credential-management layouts and lifecycle states without revealing secret values. Secret collection is not needed to explain a label, permission choice or recovery flow.

## Keep consequential actions explicit

An audit does not implicitly authorize creating or revoking credentials, changing real permissions, sending webhooks or messages, ending other sessions or deleting data. Exercise these journeys with explicitly authorized actions and safe fixtures. An isolated prototype may simulate them and must say so.

Backend authorization and identity-provider behavior can constrain a design. Record those dependencies and unverified conditions; do not claim a security assessment from a UI review.

## Package behavior

This repository supplies instructions, references, templates and local validation scripts. Its manifests configure no hooks, MCP servers, telemetry or credential collection. The audit-ledger checker reads the local JSON file supplied to it; it does not connect to the application.

These are scope and conduct rules for the agent using the skill, not a technical sandbox or a guarantee about every host application. The host's tools and permissions remain under its own controls.

Project-specific audits and private application evidence belong in the user's project or private output directory. Publishing the reusable skill does not authorize publishing that evidence.
