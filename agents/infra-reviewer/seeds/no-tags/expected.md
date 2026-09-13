verdict: BLOCK
must_mention:
  - main.tf
  - tag
notes: |
  A Lambda named fn-<random> with no tags, no description, and a log group
  that keeps logs forever. Someone looking at the bill can't tell what this is.
  Correct behavior: BLOCK on the missing identification (a tag or a meaningful
  name), WARN on retention_in_days = 0.
