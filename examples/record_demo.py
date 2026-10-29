"""Record real project-skill installation and a Claude Code sample-backlog review. Never changes boards."""

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def prepare(workspace):
    """Build an isolated Claude project; leave real skill installation to the tape."""
    subprocess.run(["git", "init", "-q", str(workspace)], check=True)
    (workspace / ".claude").mkdir()
    (workspace / ".claude/settings.json").write_text(
        json.dumps(
            {
                "disableAllHooks": True,
                "enabledPlugins": {},
            }
        )
        + "\n"
    )
    (workspace / "empty-mcp.json").write_text('{"mcpServers":{}}\n')
    (workspace / "CLAUDE.md").write_text((ROOT / "examples/claude-demo.md").read_text())
    (workspace / "backlog.json").write_text((ROOT / "examples/backlog.json").read_text())
    # Explicit tool permissions apply to this recording command only. No global
    # permissions are changed and no permission-bypass mode is enabled.
    (workspace / "demo-shell.sh").write_text(
        "claude() { command claude --setting-sources project --strict-mcp-config "
        "--mcp-config empty-mcp.json --tools Read,Skill "
        "--allowedTools Read Skill "
        '"$@" 2>claude-demo.log; }\n'
    )
    shutil.copy2(ROOT / "examples/theme.tape", workspace / "theme.tape")
    shutil.copy2(ROOT / "examples/demo.tape", workspace / "demo.tape")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "assets/terminal-demo.gif")
    args = parser.parse_args()
    for command in ["git", "claude", "vhs", "ttyd", "ffmpeg"]:
        if not shutil.which(command):
            parser.error(f"{command} must be installed and available on PATH.")
    output = args.out.resolve()
    with tempfile.TemporaryDirectory(prefix="github-projects-claude-recording-") as temporary:
        workspace = Path(temporary)
        prepare(workspace)
        print("Recording real installation and Claude Code sample review; no board changes.", flush=True)
        subprocess.run(["vhs", "demo.tape"], cwd=workspace, check=True)
        generated = workspace / "demo.gif"
        if not generated.is_file():
            raise RuntimeError("VHS did not create the recording.")
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(generated, output)
    print(f"Saved {output}")


if __name__ == "__main__":
    main()
