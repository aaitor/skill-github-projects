# Troubleshooting

| Symptom | Check |
| --- | --- |
| Skill not discovered | Clone into `.claude/skills/github-project-board`, keep `SKILL.md` at that directory's root, and restart the harness if needed. |
| Old repository URL | Update your Git remote as described in [installation](installation.md). The invocation name remains `/github-project-board`. |
| Project not found or forbidden | Check owner, project number, membership, organization policy, and project permissions. |
| Scope refresh did not help | An environment token may override stored gh authentication. Check which source is active without printing tokens. |
| Missing fields or status mismatch | Discover actual fields/options and compare with [board setup](board-setup.md); do not reuse tutorial IDs. |
| Incomplete backlog | Follow pagination; a first page of 100 items is not necessarily the whole board. |
| Agent claims instead of summarizing | Explicitly request read-only review; restrict harness tools to read operations for that session. |

For an offline installation check, use the [sample-backlog exercise](../examples/README.md). File sanitized reproducible problems in Issues; use [SECURITY.md](../SECURITY.md) for vulnerabilities.
