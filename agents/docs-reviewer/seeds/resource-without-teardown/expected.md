verdict: BLOCK
must_mention:
  - teardown
  - handoff
notes: |
  Four billable resources are created (bucket, table, log group with infinite
  retention, IAM role) and the handoff's teardown section says TBD. Correct
  behavior: BLOCK, say the teardown must cover terraform destroy AND the things
  destroy won't catch (a non-empty bucket, the log group's retained data).
