# Launched inside an isolated project by: python3 examples/record_demo.py
# Real Claude Code + real project skill. Reviews fictional input; no GitHub Projects operations.
Source theme.tape
Output demo.gif
Set Width 1280
Set Height 640
Set FontSize 20
Set BorderRadius 0
Set TypingSpeed 25ms
Set Theme { "name": "Aitor Black", "background": "#000000", "foreground": "#F4F7FB", "black": "#000000", "red": "#F28B82", "green": "#89E5CC", "yellow": "#F6D78B", "blue": "#9CAEC4", "magenta": "#C2ACEE", "cyan": "#89E5CC", "white": "#F4F7FB", "brightBlack": "#6A7D94", "brightRed": "#F28B82", "brightGreen": "#89E5CC", "brightYellow": "#F6D78B", "brightBlue": "#9CAEC4", "brightMagenta": "#C2ACEE", "brightCyan": "#89E5CC", "brightWhite": "#FFFFFF", "cursor": "#89E5CC", "selection": "#37516A" }
Hide
Type "export PS1='$ '; set -o pipefail; source demo-shell.sh; clear"
Enter
Sleep 500ms
Show
Type "git clone https://github.com/aaitor/skill-github-projects .claude/skills/github-project-board"
Sleep 500ms
Hide
Enter
Wait+Screen@30s /done./
Show
Sleep 3s
Type "clear"
Enter
Type 'claude -p "/github-project-board Review sample backlog.json. Propose the next task only."'
Sleep 1s
Hide
Enter
Wait+Screen@180s /Proceed with live discovery/
Show
Sleep 8s
