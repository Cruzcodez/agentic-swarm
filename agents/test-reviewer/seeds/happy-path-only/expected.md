verdict: BLOCK
must_mention:
  - KeyError
notes: |
  The happy path is covered and the test can fail. But load_user has an
  explicit `raise KeyError` for the not-found case, and nothing tests it. That
  raise is deliberately coded behavior: if someone changed it to return None,
  no test would notice. Correct behavior: BLOCK on the untested KeyError
  branch. File-missing and malformed-JSON are implicit (the code doesn't
  handle them, they'd just propagate) and belong under Should fix.

  First run, the seed expected WARN and the agent said BLOCK. The agent was
  right and the charter was ambiguous. Now the charter draws the line at
  whether the error path was written on purpose.
