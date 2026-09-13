verdict: BLOCK
must_mention:
  - INDEX_TABLE
  - README
notes: |
  The code requires INDEX_TABLE (no default, will crash without it) and the
  README only documents REPORTS_BUCKET. INDEX_BATCH_SIZE and AWS_REGION have
  defaults so they're WARN-level at most. Correct behavior: BLOCK on the
  missing INDEX_TABLE, name the README section that needs it.
