"""Check documentation, assets, and Markdown skill packaging offline."""

import ast
import json
import yaml
import html
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {".git", ".venv", "__pycache__", "node_modules"}


def main():
    errors = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in EXCLUDED for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix == ".svg":
            try:
                ET.parse(path)
            except ET.ParseError as exc:
                errors.append(f"{path.relative_to(ROOT)}: invalid SVG: {exc}")
        if path.suffix == ".json":
            json.loads(path.read_text())
        elif path.suffix in (".yml", ".yaml"):
            yaml.safe_load(path.read_text())
        elif path.suffix == ".py":
            ast.parse(path.read_text(), filename=str(path))
        if path.suffix != ".md":
            continue
        text = re.sub(r"^(`{3,}|~{3,}).*?^\1[^\n]*$", "", path.read_text(), flags=re.M | re.S)
        links = re.findall(r'!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text)
        links += re.findall(r'(?:href|src)=["\x27]([^"\x27]+)', text)
        for link in links:
            parsed = urlsplit(html.unescape(link))
            if parsed.scheme or parsed.netloc:
                continue
            target = (
                (ROOT if parsed.path.startswith("/") else path.parent) / unquote(parsed.path).lstrip("/")
                if parsed.path
                else path
            )
            if not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing target {link}")
                continue
            if parsed.fragment and target.suffix == ".md":
                headings = re.findall(r"^#{1,6}\s+(.+)$", target.read_text(), flags=re.M)
                anchors = {re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-") for heading in headings}
                if parsed.fragment not in anchors:
                    errors.append(f"{path.relative_to(ROOT)}: missing heading {link}")
    skill = (ROOT / "SKILL.md").read_text()
    metadata = yaml.safe_load(skill.split("---", 2)[1])
    if metadata.get("name") != "github-project-board" or not metadata.get("description"):
        errors.append("Skill entrypoint must keep its existing name and a description.")
    sample = json.loads((ROOT / "examples/backlog.json").read_text())
    if not sample.get("source") or not sample.get("items"):
        errors.append("Sample backlog needs explicit provenance and items.")
    required = ("number", "title", "status", "priority", "size", "labels")
    for item in sample.get("items", []):
        if any(key not in item for key in required):
            errors.append("Sample backlog item is incomplete.")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    print("OK: documentation links/headings, SVG/JSON/YAML, Python syntax, and skill packaging.")


if __name__ == "__main__":
    main()
