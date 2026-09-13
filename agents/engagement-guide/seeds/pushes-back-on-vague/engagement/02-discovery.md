# 2. Discovery

**Date:**
**Decision:** _build it / don't build it / build something smaller_

This is where you find out whether the thing in `01-intake.md` is worth doing, and what it would actually take.

It ends in a decision. That's the whole point of the file. Everything above the decision is evidence for it.

Don't skip to building because you already opened the editor. This is the moment where stopping is still cheap.

---

## What you looked at

Where you went, what you read, who you talked to. Keep it short, this is just so someone can tell how much digging actually happened.

> 

## What you found

The facts that matter. What their environment actually looks like, what already exists, where the data really lives, what's already been tried.

Be specific. "Their auth is complicated" doesn't help anyone. "They use Okta for staff and a separate Cognito pool for customers, and the two don't talk" does.

> 

## Assumptions

This is the section that saves you.

An assumption is something you're treating as true but haven't verified. Every project rests on a few. The dangerous ones are the ones nobody wrote down, because nobody can check them.

For each one, say what happens if it turns out to be wrong. That's the part that makes people take it seriously.

| What you're assuming | How you'd confirm it | What breaks if it's wrong |
| --- | --- | --- |
|  |  |  |
|  |  |  |

If "what breaks" is "the whole approach," go confirm that one before you write another line of anything.

## Constraints

Things that limit what you can build. Different from assumptions. An assumption might be wrong. A constraint is just true.

- Technical:
- Access (what can you actually get into):
- Time:
- Money:
- Political (who needs to be on board):

## Options you considered

At least two. If you only came up with one option, you haven't finished thinking.

Doing nothing counts as an option and is sometimes the right one.

**Option A:**
- How it works:
- Good because:
- Bad because:

**Option B:**
- How it works:
- Good because:
- Bad because:

## What it would take

Rough. Nobody expects precision here, they expect honesty.

- Effort:
- What it costs to run:
- What you'd need access to:
- Biggest thing that could go wrong:

---

## Decision

Pick one and say why.

**Build it.** You believe it's worth doing and you know roughly how. Go write `03-scope.md`.

**Don't build it.** The idea doesn't survive contact with reality. Write down why in enough detail that nobody re-opens it in three months and repeats the whole exercise. Then stop. This is a good outcome.

**Build something smaller.** The original ask is too big or too vague, but there's a real question buried in it worth answering. Say what the smaller thing is, then go write `03-scope.md` for that.

> **Decision:**
>
> **Because:**

### If you're building: what would make you stop

Write this now, while you're still objective about it.

Pick something specific and pick a date. "This is worth continuing if I can get the extraction step working end to end by the 20th. If I can't, I stop."

The version of you three weekends from now is emotionally invested and will keep going out of stubbornness. This line is the only thing that gets a vote against that.

> **Still worth it if:**
>
> **Check by:**

---

## Prompt for your AI assistant

This one is a research partner and a skeptic. It should be arguing with you, not agreeing.

A warning that matters here more than anywhere else in this folder: do not let an assistant write your assumptions. An assumption you didn't personally make isn't an assumption, it's a guess in your handwriting. When it turns out wrong you'll have no idea why you believed it.

```
I'm doing discovery for a proof of concept. Here's the intake document:

[paste 01-intake.md]

Help me work through discovery. Interview me one question at a time.

Cover: what I've actually looked at, what I found, my assumptions and what
breaks if each one is wrong, real constraints, at least two options I
considered, and rough effort and cost.

Then help me reach one of three decisions: build it, don't build it, or build
something smaller.

Rules:
- One question at a time.
- Be skeptical. If my reasoning is thin, say so and ask me to back it up.
- Never write an assumption I didn't state. If I haven't thought about
  something, ask me about it, don't fill it in.
- Push me on "don't build it." It's a legitimate answer and I'm biased
  against it because I've already started thinking about how to build it.
- If I only give you one option, make me come up with another.
- Anything I don't know goes down as "unknown," not as a plausible guess.
- When we're done, output the completed markdown and nothing else.
```
