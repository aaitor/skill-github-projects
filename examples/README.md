# Install the skill and review a sample backlog

The GIF is a **real Claude Code recording**: Git clones the actual skill, Claude loads `/github-project-board`, reads [backlog.json](backlog.json), and recommends the highest-priority Todo task. The backlog is clearly labeled fictional input, not a captured board or mocked gh response. Nothing calls GitHub Projects or changes issues, status, or comments.

## Try the sample

From your project directory, with Git and authenticated Claude Code installed:

```bash
git clone https://github.com/aaitor/skill-github-projects .claude/skills/github-project-board
cp .claude/skills/github-project-board/examples/backlog.json backlog.json
claude -p "/github-project-board Review sample backlog.json. Propose the next task only."
```

Expected result: recommend sample issue #42 (Critical, Todo), describe a proposed claim/update, and leave the board unchanged. No GitHub credential is needed. For live access use [installation](../docs/installation.md), then the [full tutorial](walkthrough.md). That tutorial is also fictional and shows commands for an authorized real board separately.

## Reproduce the recording

Requires Python 3.10+, Git, authenticated Claude Code, [VHS, ttyd, and FFmpeg](https://github.com/charmbracelet/vhs#installation), and DejaVu Sans Mono. Model execution uses your Claude account and may consume model usage.

```bash
python3 examples/record_demo.py
```

The helper creates an isolated temporary project, performs the visible install, and saves `assets/terminal-demo.gif` only after recording completes. Use `--out /tmp/demo.gif` for another destination. [demo.tape](demo.tape) uses the shared black 1280 × 640 preset, omits clone/model waiting time, and holds the actual result. [claude-demo.md](claude-demo.md) controls output brevity; it does not provide a fabricated answer.

The session uses file/skill tools only, disables optional hooks/plugins, excludes configured MCP servers, and does not change global harness settings or bypass tool permissions. A shell function applies that session configuration to the visible `claude` invocation. Review the generated GIF for accuracy and private information before publishing. Live model recording is manual, never a CI step.
