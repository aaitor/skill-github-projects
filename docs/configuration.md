# Configuration and limitations

There is no server, package installation, `.env` file, or daemon. Supply the board **owner and project number** in the agent request. The agent uses your existing `gh` authentication.

## Board conventions

The default workflow uses Status, Priority, and Size single-select fields. See [board setup](board-setup.md) for the options. IDs are always discovered from the board, never copied from examples. The agent reads the board README for local conventions; document deliberate workflow variations there. Keep the skill's human-controlled In Definition/Done boundary.

For label-scoped work, supply the label explicitly. Labels belong to issues, not project items. They help divide work, but overlapping labels are not a lock: coordinate agents and re-read the current item before claiming it. Priority selects among eligible Todo items; size describes effort.

## Scale and access

Examples often use `--limit 100` or GraphQL `first: 100`. These are bounded examples, not complete pagination. Increase a supported CLI limit or paginate with cursors before claiming an exhaustive summary of a larger board. Queries may also need pagination for labels/comments. Draft items and pull requests differ from issue-backed cards; check the content type before issuing issue commands.

This skill supplies workflow instructions, not an autonomous scheduler, atomic claim service, or technical enforcement of human approval. Harness tool permissions and your GitHub account permissions still apply. A read-only request does not authorize updates or issue comments.
