# Installation

The repository is now `aaitor/skill-github-projects`. The installed skill name remains **github-project-board**, so invoke `/github-project-board` in Claude Code. Existing clones can update their remote:

```bash
git remote set-url origin https://github.com/aaitor/skill-github-projects.git
```

## Claude Code

From your project directory:

```bash
git clone https://github.com/aaitor/skill-github-projects .claude/skills/github-project-board
claude
```

The complete skill includes `SKILL.md`, `references/`, and its linked guides. Keep the clone together. Global symlinks, copy installs, generic agents, remote hosts, and automation are covered in [installation recipes](../examples/installation.md).

## GitHub access

For live operations, install GitHub CLI and `jq`, authenticate, and check access to the intended owner/project. The existing setup recipes request the `project` OAuth scope for read/write workflows:

```bash
gh auth login
gh auth refresh -s project
gh project view <NUMBER> --owner <OWNER> --format json
```

Read-only access can use `read:project` where supported. Your account/token must also be allowed to access the project and its underlying repositories; changing scopes alone cannot grant membership. An environment-provided `GH_TOKEN` or `GITHUB_TOKEN` can override stored gh authentication. Use the appropriate permissions for your workflow and organization policy. Do not print or commit token values.

Create a compatible board only if needed using [board setup](board-setup.md). It contains commands that create projects, fields, and issues. For a credential-free planning exercise, follow [the sample demo](../examples/README.md#try-the-sample).
