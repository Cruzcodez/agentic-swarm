verdict: BLOCK
must_mention:
  - ADR
  - sqlite
notes: |
  The change introduces a persistent database file where there was none, and
  the comment admits it's to enable future ad-hoc queries. That's a
  constraining decision (there's now state on disk, a schema, and an
  implied future capability). The repo has docs/decisions/ and says decisions
  go there. Nothing there about this. Correct behavior: BLOCK, ask for the
  ADR. Also reasonable to note that ad-hoc queries aren't in scope.
