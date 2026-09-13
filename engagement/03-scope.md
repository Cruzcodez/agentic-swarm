# 3. Scope

**Date:** 2026-09-13
**Confirmed with:** _Chris Cruz, ____ (sign it when you've read it)_

---

## What we're building

A repository of specialized AI review agents that each look at a code change from one angle, refuse to pass specific problems, and report in a shared format. Each agent installs on its own into Claude Code or Kiro. Each one ships with tests that prove it catches what it says it catches.

## In scope

- [ ] Two shared documents every agent follows: the output format, and the rules of review
- [ ] `security-reviewer`: charter, adapters for Claude Code and Kiro, at least five seeded tests including a clean one
- [ ] `docs-reviewer`: same shape
- [ ] `scripts/build.sh` to generate tool-specific agent files from each charter
- [ ] `scripts/run-seeds.sh` to test every agent against its seeds
- [ ] `scripts/install-kiro.sh` to install agents into Kiro
- [ ] `marketplace.json` so each agent installs separately into Claude Code
- [ ] `docs/design.md` and ADRs recording why the repo is shaped this way
- [ ] A README a stranger can use

## Out of scope

Parked, not refused. These are next, once the first two agents have proven themselves.

- `infra-reviewer`, `test-reviewer`, `scope-reviewer`, and `engagement-guide`. Second and third wave.
- The `swarm` orchestrator that runs every agent at once. There's nothing to orchestrate until at least two agents exist and work.
- A GitHub Copilot adapter. Cheap to add, but I don't use Copilot and won't be able to test it.
- Running the agents automatically in CI. First they run by hand on demand.
- Agents that fix things. Every agent in this repo reports. None of them edit code.
- A general-purpose code reviewer. Deliberately never. Explained in `docs/design.md`.
- A write-up or paper about this. After it has results, not before.

## Acceptance criteria

- [ ] Someone can install `security-reviewer` alone into a different repository using one command, and it runs
- [ ] Every seed for both agents produces the expected verdict, including the clean seed producing PASS
- [ ] `security-reviewer` run against `easymoney-enivro` names the committed env files, the static AWS keys in the workflows, and the hardcoded resource identifiers, without being pointed at them
- [ ] A person who has never talked to me reads `README.md` and can say what this is, what each agent blocks on, and how to install one

## Not production ready

This is a proof of concept. Before anyone relies on it:

- The agents have only been tested on seeds and on one real repository. They will have blind spots that haven't been found yet.
- There's no CI integration. Reviews happen when a person runs them.
- The eval is a script that checks verdicts. It doesn't check that the agent's reasoning is sound, only that it reached the right answer.
- Token cost per review hasn't been measured.

## What happens when scope changes

1. Write it down under Out of scope
2. Decide whether it replaces something in scope or extends the timeline
3. Update the date and the confirmed-with line
