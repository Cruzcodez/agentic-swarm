# 2. One repository, each agent installable on its own

**Status:** Accepted
**Date:** 2026-09-13

## Context

The question was whether each review agent should get its own repository, so someone who only wants the security reviewer can take just that, or whether they should all live together.

The concern behind it was real. A stranger on GitHub who wants one agent shouldn't have to take seven.

## Decision

One repository. Each agent is a separate plugin in `.claude-plugin/marketplace.json`, so it installs on its own:

```
/plugin install security-reviewer@agentic-swarm
```

The "I only want one" case is solved by packaging, not by repository boundaries.

## Why

Claude Code, Kiro, and GitHub Copilot all define an agent the same way: markdown, YAML frontmatter, prompt in the body. Claude Code's marketplace format lets one repository publish many independently installable plugins. That's the mechanism.

The largest public collection of Claude Code agents (154 of them, around 23k stars) is one repository with category plugins. Every other sizeable collection is built the same way. Nobody runs a repository per agent, because then:

- the shared output format has nowhere to live
- the shared review rules have nowhere to live
- the seeded-defect test runner has nowhere to live
- the swarm orchestrator would have to reach across repositories
- a change to any convention is seven pull requests

## Consequences

- A stranger has to read the README to learn they can install one piece. That's a documentation job, and the README does it.
- If a single agent ever grows its own tooling (an MCP server, a CLI, a large test corpus), it can be split out then. Splitting is easy. Merging seven repositories back together is not.
- `dist/` is committed rather than gitignored, because the marketplace reads agent files straight from the repository and can't run a build step first. `scripts/check.sh` verifies the committed output matches what `scripts/build.sh` would produce, so it can't silently go stale.
