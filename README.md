<p align="center">
  <img src="https://raw.githubusercontent.com/aaitor/assets/ffdc5e1302cf6276c5e765cec19cc3204903c766/banners/skill-github-projects.svg" alt="GitHub Projects — turn your backlog into coordinated agent work" width="100%">
</p>

<h1 align="center">GitHub Projects Skill</h1>
<p align="center">Turn your backlog into coordinated agent work.</p>
<p align="center"><a href="https://github.com/aaitor/skill-github-projects/releases/tag/v1.0">v1.0 release</a></p>
<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="examples/walkthrough.md">Tutorial</a> ·
  <a href="#documentation">Documentation</a> ·
  <a href="#contributing-and-support">Contribute</a>
</p>
<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-89E5CC?style=flat-square&amp;labelColor=101827" alt="MIT license"></a>
  <a href="https://github.com/aaitor/skill-github-projects/actions/workflows/quality.yml"><img src="https://github.com/aaitor/skill-github-projects/actions/workflows/quality.yml/badge.svg" alt="Offline repository checks"></a>
</p>

Give Claude Code and other shell-capable agents a shared workflow for **GitHub Projects v2**. Read backlogs, select work by priority and label, claim issues, leave structured progress updates, and hand work back for human approval through the `gh` CLI.

## Demo

![Install the skill and review a sample backlog with real Claude Code](assets/terminal-demo.gif)

A real Claude Code session: install the skill, review a **fictional local backlog**, and propose the next task. The harness loads the actual skill; the sample is not live GitHub data. No issues, comments, or board fields are changed. See the [recording guide](examples/README.md) for the input and reproduction command.

## Quick start

Install into your project's Claude Code skills directory:

```bash
git clone https://github.com/aaitor/skill-github-projects .claude/skills/github-project-board
```

For live board access, install and authenticate [GitHub CLI](https://cli.github.com/), grant project access to the account/token you use, and supply your board owner and number. See [installation](docs/installation.md) for permissions and other harnesses.

Start `claude`, then ask:

```text
/github-project-board Read project #<NUMBER> for <OWNER>.
Show the highest-priority Todo item and your proposed next action.
Do not claim work or post comments.
```

Expected result: the agent discovers the board README and current fields, reads the backlog, and recommends a task without modifying it. To try the skill without GitHub credentials, use the [sample-backlog exercise](examples/README.md#try-the-sample).

## Features

- **Dynamic discovery:** resolve project, field, and option IDs at runtime.
- **Priority-based work:** select Todo items, optionally scoped by issue labels.
- **Shared progress format:** structured comments for updates, blockers, and handoffs.
- **Human approval:** agents submit completed work as Ready; humans control Done.
- **Portable instructions:** plain Markdown, with command references and GraphQL recipes.

The skill is instructions, not a background worker or locking service. Label scoping helps divide work; overlapping agents still need coordination. Large boards need pagination beyond the examples' first 100 items. See [configuration and limitations](docs/configuration.md).

## Board workflow

```text
In Definition → Todo → In progress → To Review → Todo (feedback)
                                  → Ready → Done (human approval)
```

| Field | Options |
| --- | --- |
| Status | In Definition, Todo, In progress, To Review, Ready, Done |
| Priority | Critical, Very High, High, Average, Low, Very Low, Zero |
| Size | XL, L, M, S, XS |

Agents read your board README for local conventions and discover the actual option IDs. `In Definition` and `Done` remain human-controlled. [Set up a compatible board](docs/board-setup.md), then follow the [practical walkthrough](examples/walkthrough.md) from discovery through review. That tutorial uses fictional data and marks commands that change the board.

## Usage

```text
/github-project-board Summarize Todo items on project #<NUMBER> for <OWNER>.
Only consider issues labeled docs. Propose a task; do not update anything.
```

Once you authorize work, the skill provides conventions for claiming an issue, reporting progress, and submitting it as Ready. See [usage scenarios](examples/usage-scenarios.md) for triage, decomposition, clarification, and handoffs.

## Documentation

- [Installation and permissions](docs/installation.md) · [Other installation recipes](examples/installation.md)
- [Board setup](docs/board-setup.md) · [Configuration and limitations](docs/configuration.md)
- [Practical walkthrough](examples/walkthrough.md) · [Usage scenarios](examples/usage-scenarios.md)
- [CLI reference](references/gh-cli-commands.md) · [GraphQL recipes](references/graphql-recipes.md) · [Agent workflows](references/agent-workflow-patterns.md)
- [Troubleshooting](docs/troubleshooting.md) · [Security and privacy](docs/security-and-privacy.md)
- [Banner generation](docs/branding.md) · [Demo recording](examples/README.md)

## Repository layout

```text
SKILL.md       Installed skill: github-project-board
references/    CLI commands, GraphQL queries, workflow patterns
docs/          Installation, board setup, configuration, troubleshooting
examples/      Tutorials, fictional backlog, real harness recording
assets/        Banner, social preview, terminal demo, font notices
scripts/       Offline repository checks
```

## Contributing and support

Questions, bugs, and ideas: [Issues](https://github.com/aaitor/skill-github-projects/issues). Read [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [CHANGELOG.md](CHANGELOG.md). Report vulnerabilities privately through [SECURITY.md](SECURITY.md).

Run `python3 scripts/check.py` after installing `requirements-dev.txt`. CI checks packaging, sources, and local documentation; live GitHub operations and model recordings are manual checks.

## License

[MIT](LICENSE). The existing license is preserved. Embedded banner fonts retain their [OFL notices](assets/font-notices/NOTICE.md).

---

Built by [Aitor Argomaniz](https://github.com/aaitor) · [LinkedIn](https://www.linkedin.com/in/aitorargomaniz) · [More open source](https://github.com/aaitor?tab=repositories)
