# 2. Discovery

**Date:** 2026-09-13
**Decision:** build it

---

## What you looked at

- Claude Code's subagent documentation: file format, where files live, how plugins bundle them
- Claude Code's plugin marketplace documentation: how one repo can offer many separately installable plugins
- Kiro's custom agent configuration reference and its sub-agent invocation docs
- GitHub Copilot's custom agent configuration, to see if a third tool fit the same shape
- The largest public collection of Claude Code subagents (VoltAgent, about 23k stars, 154 agents) to see how a big collection is actually organized

## What you found

**All three tools define an agent the same way.** A markdown file. YAML frontmatter at the top holds the configuration. The body of the file is the system prompt. Field names differ a little between tools. The shape does not. Kiro can even point its prompt at an external file.

**Per-agent install already exists inside one repo.** Claude Code lets a repo act as a marketplace. A `marketplace.json` file lists each plugin, and people install them one at a time with `/plugin install <name>@<marketplace>`. That's the "I only want the security agent" case, solved without splitting anything up.

**Big collections are single repos.** The 154-agent collection is one repo with category folders, each exposed as a plugin. Every other collection I looked at is the same. Nobody with a real collection does one repo per agent.

**Both Claude Code and Kiro run sub-agents in parallel.** A primary agent can hand the same work to several specialized agents at once and wait for all of them. Kiro controls which agents can be spawned with an `availableAgents` list. Claude Code has the parent spawn them, and sub-agents can't spawn their own, so the structure stays flat.

## Assumptions

| What you're assuming | How you'd confirm it | What breaks if it's wrong |
| --- | --- | --- |
| The Claude Code CLI can run a named agent non-interactively, so a script can test it | Run `claude -p` against one seed and see if the agent is used | The eval has to run by hand, or only through Kiro's CLI |
| Kiro's `file://` prompt path resolves relative to the agent file | Install one agent into `.kiro/agents/` and switch to it | `build.sh` inlines the charter into the Kiro file instead of referencing it. Small change. |
| `marketplace.json` lets a plugin entry point at an agent file by path | Install one plugin from the repo | The folder layout has to follow the plugin standard exactly (`agents/` inside each plugin dir). Annoying, not fatal. |
| gitleaks and semgrep install cleanly on a Mac with Homebrew | `brew install gitleaks semgrep` | The security agent falls back to pattern matching in the prompt itself. Weaker, still works. |

## Constraints

- Technical: two target tools, Claude Code and Kiro. Anything written has to work in both or it isn't done.
- Access: the agents only run on my machine for now. The sandbox Claude works from can't reach GitHub or run the Claude Code CLI.
- Time: usable before November.
- Money: every review costs tokens. Seven agents on one diff is seven times the cost of one. That's an argument for starting small and for keeping agents narrow.
- Political: none. I'm the only person involved.

## Options you considered

**Option A: one repo per agent.**
- How it works: `cruzcodez/security-reviewer`, `cruzcodez/docs-reviewer`, and so on. Each fully independent.
- Good because: obvious to find one. Obvious to star one.
- Bad because: seven repos to keep in sync. A shared output format has nowhere to live. The orchestrator would have to reach across repos. Every convention change is seven pull requests.

**Option B: one repo, each agent installable on its own.**
- How it works: `cruzcodez/agentic-swarm`, with a `marketplace.json` listing each agent as a separate plugin.
- Good because: one place for shared rules, shared tests, and the orchestrator. Per-agent install is free. It's how every serious collection works.
- Bad because: slightly harder to explain in one sentence. Someone has to read the README to learn they can install just one piece.

**Option C: put the agents inside project-starter.**
- How it works: every project generated from the template ships with the agents.
- Good because: zero install step.
- Bad because: the agents would be copied into every project and drift immediately. Fixing one would mean fixing it everywhere. Also ties the agents to one template when they should work on any repo.

**Doing nothing.** Keep using generic assistants and explaining what I want each time. That's what I do now and it's the thing I'm tired of.

Chose B.

## What it would take

- Effort: the first two agents, their tests, and the scripts around them is a weekend. Each additional agent is an evening.
- What it costs to run: tokens per review. Unknown until it's used. Will measure.
- What you'd need access to: Claude Code CLI and Kiro CLI, both signed in, on my Mac. gitleaks and semgrep installed.
- Biggest thing that could go wrong: the agents sound confident and catch nothing. This is the whole risk, and it's why every agent gets seeded-defect tests before it gets used on anything real.

---

## Decision

> **Decision:** build it
>
> **Because:** the research settled every open question from intake. The structure is one repo with per-agent install, which is how the tools already work and how every big collection is built. The value is testable: plant a known defect, see if the agent catches it. And there's a real first use waiting for it. The easymoney repository has three committed env files, static AWS keys in its CI, and 180 dependency alerts. I know what's wrong with it. If the security agent finds those, it's real.

### If you're building: what would make you stop

> **Still worth it if:** the security reviewer, run against the easymoney repository, names all three of the known problems (committed `.env` files, static AWS keys in workflows, hardcoded resource identifiers) without being told where to look.
>
> **Check by:** 2026-09-27
>
> If it can't do that after the charter has been tuned twice, the approach is wrong and I stop adding agents until I understand why.
