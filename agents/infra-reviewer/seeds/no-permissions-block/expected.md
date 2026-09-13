verdict: WARN
must_mention:
  - ci.yml
  - permissions
must_not_mention:
  - SHA
notes: |
  No permissions: key anywhere, on a job that only runs tests. The token gets
  the repo default, which is broader than it needs. Correct behavior: WARN,
  say to add permissions: contents: read. Not BLOCK, because the job has no
  credentials and can't deploy; the charter reserves BLOCK for jobs that can
  reach something.

  must_not_mention SHA is scoped to Blocking and Should fix. The agent may
  (and should) note under Noted that SHA pinning doesn't apply here. Reporting
  the @v4 pins as a finding on a test-only job would be a false positive.
