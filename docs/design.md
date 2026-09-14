# Design

How this repository is shaped and why. The ADRs in `decisions/` hold the individual choices. This is the picture they add up to.

## What it is

Agentic Swarm Development: many narrow AI reviewers examine the same change at once, each with a defined lane and a list of what it refuses to pass, and their findings merge into a single verdict. Agents criticize. People build.

## Three layers, kept apart

Most collections of agents are a folder of prompt files. This one separates three things that change for different reasons.

| Layer | What it is | Changes when |
| --- | --- | --- |
| Charter | What the agent is for, what it blocks on, what it stays out of. Plain markdown. No tool knows about it. | You learn something about reviewing |
| Adapter | A few lines of YAML frontmatter that make the charter a Claude Code agent or a Kiro agent. | A tool changes its format |
| Distribution | `marketplace.json`, the Kiro install script, the README index. | An agent is added or removed |

`scripts/build.sh` glues an adapter onto its charter, with the two shared contracts prepended, and writes the result to `dist/`. It's `cat` with a check mode. That's all it needs to be. The point is that the thinking lives in one file per agent and never gets edited in three places.

## Every agent has five parts

- **Mandate.** One sentence. What it's responsible for.
- **Blocks on.** Specific things that produce a BLOCK. Checkable. An agent that can only approve is decoration.
- **Tools.** Named, with flags. Where preferences get frozen instead of re-explained.
- **Out of lane.** What it must not comment on. Without this, every agent flags the same thing.
- **Output format.** Identical across agents, so reports can be merged instead of read one at a time.

The output format has a section called "Out of my lane." When an agent notices something that isn't its job, it goes there with a note about whose job it is. Findings don't get lost and agents don't step on each other. That one section is what makes a swarm work instead of a pile of agents talking over each other.

## Proving they work

Each agent has a `seeds/` folder. Each seed is a small folder with one planted defect and an `expected.md` saying what the correct verdict is and what the report must mention. Plus a clean seed with nothing wrong, because an agent that blocks everything is as useless as one that passes everything.

`scripts/run-seeds.sh` runs each agent against each of its seeds through the Claude Code CLI and checks the answer. That's an eval. It answers the question that otherwise never gets asked: is this agent real, or does it just sound sure of itself.

When an agent misses something on a real repository, that becomes a new seed. The corpus grows from real failures.

## The roster and the order

| Agent | Job | Wave |
| --- | --- | --- |
| security-reviewer | Ways the change can be attacked or leak | 1 |
| docs-reviewer | Whether someone inheriting this could run, change, and remove it | 1 |
| infra-reviewer | Will it run, what does it cost, can it be torn down | 2 |
| swarm | Runs every installed critic at once, merges the reports | 2 |
| test-reviewer | Is new behavior covered, would the tests fail if it broke | 3 |
| scope-reviewer | Does the change match what was agreed, was the reasoning recorded | 3 |
| engagement-guide | Interviews you to fill out intake, discovery, scope, handoff | 3 |

Wave 1 had a gate: install both agents into a real project and run them on a real change. If two agents can't produce a useful review, adding five more doesn't help. All three waves are built as of 2026-09-14; the gate was passed on this repository's own engagement documents, and the full swarm has since reviewed real pull requests on shelflife.

The swarm orchestrator is wave 2 on purpose. There's nothing to orchestrate until at least two critics exist and have caught something.

## What's deliberately missing

A general code reviewer. See `decisions/0004`.

A Copilot adapter. The format is nearly identical and adding one is cheap. But it would be untested, and an untested adapter is worse than none.

Automatic runs in CI. First the agents run by hand, on demand, so their output gets read by a person while it's still being tuned.
