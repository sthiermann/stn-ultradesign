# Contributing

Describe the user task, the observed problem and the intended outcome. Prefer changes that make a design decision clearer, a workflow more complete or verification more reliable.

## Package scope

Keep this repository focused on the usable skill: original instructions, reusable references and templates, validators, meaningful automated tests, installation guidance and distribution metadata. Keep development histories, research notes, source comparisons, evaluation reports and standalone test applications outside the package. Public content is English.

Write original material and retain any legally required notices. Contributions must be available under the project's [MIT License](LICENSE). Follow the [privacy and audit boundaries](PRIVACY.md); private product data and customer screenshots do not belong in public changes.

Keep `SKILL.md` concise. Put specialist guidance in the relevant reference, and inspect its callers before removing a resource. Guidance should describe a useful decision and observable outcome while respecting the user's requested scope.

## Check the change

Run the package checks from the repository root:

```sh
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

For operational changes, exercise a representative task and a meaningful counterexample. Keep detailed development evidence outside the public package and report only checks actually performed. For validator changes, cover valid and inconsistent ledgers. For visual changes, inspect the rendered result at normal and compact widths.

For behavior changes, compare frozen candidate and previous skill snapshots against fixed tasks in separate fresh contexts when the host supports them. Keep participant inputs separate from reviewer rubrics and prior results, pin the task and skill fingerprints before execution, and retain failing or unavailable runs. Review observable outcomes and false-positive controls, not exact wording. Disclose prompting, isolation, tool and environment limits; source reasoning is not runtime evidence. Keep this development suite and detailed results outside the public package. Full application trials and human visual/task assessment remain separate from bounded case results.

Package checks establish internal consistency. Application behavior, visual quality, successful client installation and human acceptance need their own evidence.

## Release metadata

Keep the version in both plugin manifests and the README current-release declaration synchronized. Use patch releases for compatible corrections and minor releases for new capabilities. Before 1.0, incompatible artifact or schema changes require a minor release and user-facing migration guidance; after 1.0, use a major release. Run the relevant checks before publishing.

Keep installation instructions aligned with supported client behavior. Adding hooks, external integrations or dependencies requires a justified change to the package's intended scope.
