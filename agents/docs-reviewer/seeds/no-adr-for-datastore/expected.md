verdict: BLOCK
must_mention:
  - ADR
  - DynamoDB
notes: |
  The code comment admits a datastore switch from Postgres to DynamoDB with a
  specific single-table key design. That's exactly the kind of decision that's
  expensive to reverse and shapes every query written after it. docs/decisions/
  exists and says decisions go there. There's only the seed ADR. Correct
  behavior: BLOCK, ask for an ADR covering why DynamoDB, why this key design,
  and what it costs to change later.
