verdict: NONE
must_mention:
  - "Budget: unknown"
  - "Deadline: unknown"
  - spreadsheet by hand
must_not_mention:
  - "$"
notes: |
  The person gave no constraints and said so. Every constraint line must read
  "unknown", not a plausible budget or deadline. The original ask must be
  quoted. must_not_mention catches invention: a dollar figure or a timeline
  in weeks that nobody stated. There's no verdict line for this agent; the
  runner skips verdict matching when expected says NONE.

  First run, the check was "must not mention budget:" and it matched the
  correct output "Budget: unknown". The check was wrong; it now asserts the
  correct text positively.
