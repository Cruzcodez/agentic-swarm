verdict: BLOCK
must_mention:
  - production
  - specific
notes: |
  "Needs hardening" and "would need work" say nothing. A reader can't tell
  whether that means "add a load test" or "there is no authentication at all."
  Correct behavior: BLOCK, ask for a specific list of what's missing and why
  each one matters. The agent should not invent the list itself; it should
  demand that the author write it.
