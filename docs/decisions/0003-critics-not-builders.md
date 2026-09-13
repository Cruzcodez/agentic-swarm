# 3. Agents review. They don't build.

**Status:** Accepted
**Date:** 2026-09-13

## Context

A swarm of specialized agents could be organized two ways.

**Builders:** each agent writes part of the change. An infrastructure agent writes the Terraform, a backend agent writes the handler, a frontend agent writes the UI. They coordinate.

**Critics:** every agent reads the same finished change and looks for different things. None of them write code.

## Decision

Every agent in this repository is a critic. It reads a change and reports. It never edits, fixes, or generates replacement code.

## Why

Builders have to coordinate. That means integration bugs at the seams, one agent making an assumption another agent broke, and a lot of machinery to keep them in step. It's a real approach and it works, but it's hard to get right, and getting it wrong produces confident nonsense.

Critics don't coordinate at all. They each read the same diff. There's nothing to integrate. The only shared surface is the output format, which is a document.

There's a second reason that matters more. A reviewer that also writes code stops being a reviewer. It starts judging "is this what I would have written" instead of "is this correct." Keeping the two jobs in different agents is what makes the review worth anything.

## Consequences

- No agent in this repository will fix what it finds. That's on purpose. If you want the fix, take the finding to whatever you write code with.
- Every agent needs a defined lane and a list of what it stays out of, or six critics all say the same thing. See `shared/review-contract.md`.
- Every agent needs a list of what it refuses to pass. An agent that can only approve is decoration.
- A swarm orchestrator, when one exists, merges reports. It doesn't add findings of its own.
- The existing Kiro dev swarm (parallel builders with file isolation) stays a separate thing. This repository doesn't replace it.
