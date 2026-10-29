# Banner and social preview

The header follows the shared repository format: **diagonal-drift (1a)**, seed `7`, with the title `GitHub Projects` and handle `@aaitor`. The README points at a commit-pinned banner in [aaitor/assets](https://github.com/aaitor/assets); a local copy is kept in `assets/hero.svg`.

`shared-assets.json` records the shared source revision and template revision. Banner generation is separate from the skill’s GitHub workflow. Regenerate shared artwork in the assets repository with Node.js 18+.

## Generate the banner

From a clone of `aaitor/assets` with Node.js 18+ installed:

```bash
node banner-kit/make-banner.mjs --style diagonal-drift \
  --repo "GitHub Projects" \
  --tagline "Turn your backlog into coordinated agent work." \
  --handle "@aaitor" --seed 7 --out banners/skill-github-projects.svg
```

See the [shared generation guide](https://github.com/aaitor/assets/blob/ffdc5e1302cf6276c5e765cec19cc3204903c766/docs/banner-generation.md) for all styles, fixed seeds, static output, and the JavaScript API. The kit requires no npm packages or network access. Preserve the bundled font notices.

## Regenerate the social card

From that same assets checkout, center the generated banner on a matching 1280 × 640 canvas:

```bash
python3 - <<'PYTHON'
from pathlib import Path
banner = Path('banners/skill-github-projects.svg').read_text()
inner = banner.replace('<svg ', '<svg x="0" y="160" ', 1)
Path('social/skill-github-projects.svg').write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="640" '
    'viewBox="0 0 1280 640" role="img" aria-label="GitHub Projects">'
    '<rect width="1280" height="640" fill="#0e0f11"/>' + inner + '</svg>\n')
PYTHON
```

Open the SVG in a modern browser to check fonts and clipping. Export to PNG with a browser or vector editor that supports embedded webfonts. If using Chromium, run from the assets checkout:

```bash
chromium --headless --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=1 --window-size=1280,640 \
  --virtual-time-budget=1500 \
  --screenshot="$PWD/social/skill-github-projects.png" \
  "file://$PWD/social/skill-github-projects.svg"
```

Copy the reviewed banner and social SVG/PNG into this skill's `assets/`, update the source revision and pinned README URL after publishing upstream, and keep the font notices. The ready-to-upload `assets/social-preview.png` is included, but must be uploaded through **GitHub Settings → General → Social preview** to activate it. Merely committing it does not set the repository preview.

## Terminal demo

The [recording guide](../examples/README.md) documents real skill installation and Claude Code review of a fictional backlog. Use the black terminal preset in `examples/demo-spec.json`. Stop at the proposed action; do not change live boards to produce a demo.
