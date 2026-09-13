verdict: BLOCK
must_mention:
  - two-digit
  - test
notes: |
  A whole new input format was added (MM/DD/YY) and the only test covers the
  old one. Correct behavior: BLOCK, name the untested branch, say what the
  test should assert (e.g. "09/13/26" -> 2026-09-13, and ideally what happens
  with "99" since the century assumption is a real decision).
