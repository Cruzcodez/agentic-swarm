# 4. No general-purpose code reviewer

**Status:** Accepted
**Date:** 2026-09-13

## Context

Every collection of review agents has a generic "code-reviewer." It was the obvious first agent to write.

## Decision

There isn't one, and there won't be.

## Why

A general code reviewer has no lane. It comments on everything, which means it overlaps every specialized agent and adds style opinions on top. In a merged report, its findings duplicate the security reviewer's, the docs reviewer's, and the test reviewer's, and bury the one thing only it noticed under twenty things everyone noticed.

It's also the agent most likely to say "looks good" without having checked anything specific, because nothing specific is its job.

Five agents with sharp edges are more useful than six where one is blurry.

## Consequences

- If a real gap shows up that none of the specialized agents cover, that's the signal to write a new specialized agent for that gap. Not a general one.
- Style, naming, and formatting are nobody's job here. A linter does that, deterministically, for free.
