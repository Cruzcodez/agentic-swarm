# 1. Intake

**Date:**
**Who asked:**
**Who's building it:**

Fill this out before you do anything else. Before research, before design, definitely before code.

The job of this file is to freeze the original ask in writing, while it's still fresh and before you've started reinterpreting it. Six weeks from now somebody will say "I thought this was also going to do X." This file is how you find out whether they said that, whether it changed along the way, or whether it never came up. Without it you're arguing from memory.

If this is your own idea, put your own name in "who asked." Write it down anyway. The version of you that's three weekends deep and chasing a tangent needs something to argue with.

---

## What they asked for

Write it the way they said it. Don't tidy it up and don't translate it into architecture yet.

If they said "we need a chatbot that reads our S3 bucket," write exactly that. The messy original wording is the useful part. Later you'll want to know what was actually said, as opposed to what you decided they must have meant.

> 

## Why they want it

What's the problem underneath the request?

People ask for solutions, not problems. Somebody asking for a chatbot usually has a problem more like "our team burns an hour a day hunting for documents." That problem is the thing you're actually solving. The chatbot is one possible answer to it, and it might not be the best one.

This matters because if you only build what was asked for, you can ship exactly what they requested and still not help them.

If you can't answer this yet, good. That's your first discovery question.

> 

## What does success look like

How will they know it worked? Push for something you could actually go check.

"It's faster" isn't checkable. "Someone can find a policy document in under 30 seconds without messaging the ops team" is. If you can't measure it, you can't tell whether you're done, and neither can they.

> 

## Constraints already on the table

Anything that limits your options, as far as you know right now:

- Budget:
- Deadline:
- Tools or platforms they have to use:
- Tools or platforms they can't use:
- Security or compliance requirements:
- Who has to approve things:

You'll find more of these in discovery. This is just what's been said so far.

## What you don't know yet

List the questions you can't answer. These become your discovery checklist.

Be honest here, it costs you nothing. "I don't know what format their data is in" is a real gap, and writing it down is how it gets closed. Pretending you know is how you find out the expensive way.

- [ ] 
- [ ] 

---

## Prompt for your AI assistant

Paste this into Claude, Kiro, or whatever you use. It interviews you and writes the file from your answers.

Here's what it deliberately will not do: make things up. If it starts inventing constraints or guessing what the customer wants, stop it. The point of this document is that you thought about it. An assistant that fills it in for you hands back a page of reasonable sounding text you never actually considered, and you won't spot the wrong parts until they cost you something.

```
I'm starting intake for a new proof of concept. Interview me one question at a
time and then write an intake document from my answers.

Cover these sections:
- What was asked for, in the asker's own words
- The underlying problem behind the request
- What success looks like, in terms someone could actually verify
- Constraints already known (budget, deadline, required tools, banned tools,
  security requirements, approvers)
- What I don't know yet

Rules:
- Ask one question at a time. Wait for my answer before moving on.
- If my answer is vague, push back and ask for something specific. "It should
  be faster" is not an acceptable success criterion.
- Never invent, assume, or fill in anything I haven't told you. If I don't
  know something, write "unknown" and add it to the open questions list.
- Don't suggest solutions. This document is about the problem.
- When we're finished, output the completed markdown and nothing else.
```
