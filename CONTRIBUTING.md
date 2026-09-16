# Contributing

Help make a concrete design decision or verification step more reliable. An issue or pull request should describe the task, the observed problem, and the intended outcome. For an incorrect recommendation, a minimal example and a traceable counterexample are useful evidence.

## Contribution principles

- **Write original material.** Create your own instructions, code, templates, illustrations, and fixtures. Do not import another design skill, component library, screenshot, font file, or brand asset. Write actionable methods in original words. Keep research evidence project-local; do not add provider comparisons or source catalogues to this package.
- **Make guidance actionable.** Describe the trigger, decision, relevant exception, and observable outcome. Distinguish standards, vendor guidance, research, and project assumptions.
- **Respect the product.** Consider existing identity, user tasks, language, accessibility, and platform constraints. Personal aesthetic preferences are not universal rules.
- **Preserve full-audit coverage.** Every discovered page, component usage, widget, drilldown, and defined relevant workflow belongs in the requested scope. Record resumable batches and access gaps. Sampling requires an explicit scope change.
- **Evaluate craft as well as behavior.** Inspect rendered concepts at their target sizes, explain compositional decisions, and record criticism and revision. Passing an automated test does not establish aesthetic quality.
- **Report only performed checks.** Do not invent studies, screenshots, approval, scores, or performance gains. A mockup is not evidence of working production behavior.
- **Keep evidence private by scope.** Follow [PRIVACY.md](PRIVACY.md). Use synthetic fixtures for account and access workflows. Never publish customer data, credentials, session material, or private product screenshots.

Keep `SKILL.md` concise and place specialist detail in the relevant reference. Add dependencies only when a demonstrated need justifies them. Public instructions and examples should be in English.

## Version and release changes

Publish user-visible changes to skill behavior, templates or validators as a versioned release. Use a patch release for compatible corrections and a minor release for compatible new capabilities. Before 1.0, incompatible artifact or schema changes also require a minor release plus an explicit migration guide; after 1.0 they require a major release. Do not change versions for every work-in-progress edit or isolated typo.

Keep the current README release, both plugin manifests and the latest changelog entry consistent. Run package validation and relevant tests before creating the matching tag and release. Describe the observable change and its limits; preserve historical evaluation versions instead of implying they were rerun. Release metadata and successful checks do not establish universal design quality.

## Before opening a pull request

1. Check internal links, metadata, skill names, and the relevant primary sources. Keep version-sensitive research evidence in the project-local working record.
2. Run the repository checks from its root:

   ```sh
   python3 scripts/validate_repository.py
   python3 -m unittest discover -s tests -v
   ```

3. For changes to operational behavior, exercise a representative task and a meaningful counterexample. Record the client, model, tools, initial conditions, and result. A focused review is sufficient for simple text corrections.
4. For coverage-validator changes, test both valid and deliberately inconsistent ledgers. Declared coverage must never be presented as proof of actual interface quality.
5. For visual changes, inspect the rendered output, check readability at normal and compact widths, and provide a concise account of what was verified.

The [evaluation reference](skills/stn-ultradesign/references/skill-evaluation.md) describes repeatable evaluation across project revisions. Use the same tasks and conditions, expose variation, and separate visual preference from task success.

## Packaging and rights

Keep plugin versions synchronized. Check installation instructions against official documentation and available client help. Report manifest validation separately from an actual installation test. Hooks, network services, and integrations require a separate, justified scope decision.

By contributing, you confirm that you can provide your contribution under the project's [MIT License](LICENSE). Include any required attribution or rights information with the contribution and, where appropriate, in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Attribution alone does not grant permission to reuse third-party material.
