# Installation

As of September 17, 2026. Install either the individual skill or the plugin in your client. Installing the same skill twice is unnecessary.

## Codex: individual skill

Codex loads project skills from `.agents/skills/` and personal skills from `~/.agents/skills/`. Keep the entire skill directory so that references, templates and scripts remain available.

Download the repository, for example in a terminal:

```sh
git clone https://github.com/sthiermann/stn-ultradesign.git
cd stn-ultradesign
```

For a personal installation on macOS or Linux, run these commands from the downloaded repository:

```sh
mkdir -p "$HOME/.agents/skills"
ln -s "$PWD/skills/stn-ultradesign" "$HOME/.agents/skills/stn-ultradesign"
```

The link assumes that no entry with the same name exists at the destination and that the repository stays in this location. Alternatively, copy the complete `skills/stn-ultradesign` directory to `~/.agents/skills/stn-ultradesign`. For a project installation, copy it to `<project>/.agents/skills/stn-ultradesign`. On Windows, use the corresponding directories in your user profile; copying does not require symbolic links.

Reopen Codex if the skill does not appear. In Codex CLI or the IDE, select it through `/skills` or mention `$stn-ultradesign` in your request. Interfaces that offer a skill selector through `@` may also list it there.

> $stn-ultradesign Review the settings area for clarity, consistency, error recovery and keyboard operation.

## Codex: plugin package

The repository includes the supported compatibility manifest `.codex-plugin/plugin.json`. For a local marketplace workflow, use `$plugin-creator` to register the existing repository directory in a local marketplace, refresh the client, then install the plugin from that source. The creator should register this existing package without regenerating its skill contents.

Publishing on GitHub does not add the package to the official plugin directory. This repository does not configure a personal Codex marketplace itself. The individual installation above is sufficient for immediate use.

## Claude Code: plugin from GitHub

Enter these commands inside a Claude Code terminal session:

```text
/plugin marketplace add sthiermann/stn-ultradesign
/plugin install stn-ultradesign@stn-ultradesign
```

Choose the intended installation scope when prompted. If Claude Code requests it, run `/reload-plugins` afterward. Invoke the skill with:

> /stn-ultradesign:stn-ultradesign First develop a reviewable design concept for this workflow. Implement it after my approval.

The marketplace points to the plugin at the repository root. Use the GitHub repository name as the source, rather than a direct URL to its `marketplace.json`.

For a local trial without marketplace installation:

```sh
claude --plugin-dir /absolute/path/stn-ultradesign
```

Replace `/absolute/path/stn-ultradesign` with the actual repository path. This runs the local plugin for that session.

## Claude Code: individual skill alternative

Copy the complete `skills/stn-ultradesign` directory to `~/.claude/skills/stn-ultradesign` or `<project>/.claude/skills/stn-ultradesign`. Then use `/stn-ultradesign`. Personal installation applies to local Claude Code sessions; other Claude products have their own loading mechanisms.

## Verify and update the installation

Open a new task and explicitly invoke the skill. Start with a bounded audit. Check that the agent reads the skill and relevant references, respects the requested scope, and separates observed results from assumptions.

With a linked installation, skill files follow the checked-out repository revision. With a copied installation, copy the skill directory again after updating. Review changes before adopting them. Update Claude plugins through the client's plugin manager.

Manifest validation checks the package format. It establishes neither successful installation in every client version nor the quality of a particular audit. When reporting problems, include the client version, installation method and checks actually performed.

## Start a new design review

Open the application project in a new task and use the [README example for an audit and redesign](../README.md#put-it-to-work). Supply access to the original running application and the relevant source code. An earlier concept preview is not the original application.

For a fresh review, start a separate task without copying or forking the previous design conversation. Previous concepts and preference notes can remain in their existing location; do not attach them as the desired result. Project instructions and design documents remain available, so clarify which earlier design decisions still apply while preserving current technical and product requirements. The skill should discover the product and ask about your current preferences through its normal workflow.

Deleting old concepts or reverting working product changes is not a prerequisite. Preserve ongoing changes and identify the source revision and running build actually inspected. A separate working copy can isolate new artifacts when useful; it does not automatically remove historical guidance or make its runtime match the source. Audit and concept work can use the existing project with production changes held until approval.

For a repeatable evaluation, record the skill revision, application baseline and available tools, and keep the skill version fixed during the run. Record findings for a later skill update. No additional test-specific launch prompt is required.
