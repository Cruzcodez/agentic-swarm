verdict: BLOCK
must_mention:
  - README
  - "--workers"
notes: |
  Three things drifted. The README says PDF only; code handles docx and txt.
  README says single-threaded; code has a thread pool. Two new flags
  (--workers, --dry-run) aren't documented. The Limitations section is now
  actively wrong, which is worse than missing. Correct behavior: BLOCK, name
  each stale statement and each missing flag.
