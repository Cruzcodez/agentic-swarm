# Tech constraints

## Stack

- **Language:** Bash for scripts, Markdown for everything else. No application code.
- **Runtime / platform:** Claude Code CLI and Kiro CLI on a developer's machine.
- **IaC:** none
- **Test framework:** `scripts/run-seeds.sh`, which is the eval
- **Package manager:** none

## Allowed

Editing charters, adapters, seeds, shared contracts, scripts, and docs. Running `scripts/build.sh` and committing the result.

## Requires approval

- A new agent (needs a charter, two adapters, five seeds, and a marketplace entry, and it should be on the roadmap in `docs/design.md`)
- Any change to `shared/output-format.md`. Every agent and the future orchestrator depend on it.
- Adding a tool an agent is told to run. Say why it beats what's already there.

## Forbidden

- Editing anything under `dist/`. Edit the charter and rebuild.
- An agent that writes, edits, or fixes code. See `docs/decisions/0003`.
- A general-purpose code reviewer. See `docs/decisions/0004`.
- Removing a seed to make the eval pass.

## Cloud

None. Nothing here deploys anywhere.
