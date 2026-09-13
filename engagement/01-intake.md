# 1. Intake

**Date:** 2026-09-13
**Who asked:** Chris Cruz (my own idea)
**Who's building it:** Chris Cruz, with Claude doing the heavy lifting while I watch and learn

---

## What they asked for

Written the way I said it, out loud, before any of it was designed:

> Beef up my agentic swarm idea by creating individual agent ideologies for each agent. For example, having an infrastructure agent, having a security agent. So that way when the swarm takes off, they can each do their own thing. And then testing that.

And a follow-up, which turned out to be the important part:

> What if someone only wants the security agent that does x, y, and z? Or what if someone only wants an intake agent?

## Why they want it

Two reasons, and they're different.

**For me:** right now if I tell an assistant "run a security scan," it runs one. Maybe not with the tool I'd pick. Maybe not checking the things I care about. Then I explain what I actually meant, and next time I explain it again. I want agents that already know how I want things done, so I stop re-explaining and they just go.

**For anyone else:** this goes on my GitHub. If an employer or a stranger finds it, it needs to make sense on its own and be usable without talking to me. A folder of prompts nobody can install isn't that.

## What does success look like

- Somebody can install just the security agent, without taking the rest.
- An agent catches a real problem on a real repository. Not a made-up example. A real one.
- A person who has never talked to me can read the README, understand what this is, and get one agent running.
- The agents can be proven to work, not just sound confident.

## Constraints already on the table

- Budget: my own time and API tokens. No outside money.
- Deadline: none hard. The Virginia Tech program starts in November and I want this usable before then.
- Tools or platforms they have to use: Kiro and Claude Code. Those are what I actually use day to day.
- Tools or platforms they can't use: nothing banned.
- Security or compliance requirements: nothing goes public until I say so. No customer material of any kind.
- Who has to approve things: me.

Also: everything written in plain language. Don't assume the reader knows anything. That's a constraint, not a preference.

## What you don't know yet

Questions I couldn't answer when I asked for this:

- [ ] Should each agent be its own repo so people can grab one, or should they all live together?
- [ ] Do Claude Code and Kiro define agents the same way, or do I have to write everything twice?
- [ ] How do I test an agent? How do I know the security agent is actually good and not just sure of itself?
- [ ] What does "run them all at once" actually look like in practice?
