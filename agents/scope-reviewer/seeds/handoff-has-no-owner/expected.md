verdict: PASS
notes: |
  Everything in the diff maps to an in-scope line and it's standard library
  only, so scope is fine. The trap is `_legacy_decimal`: dead code that no
  agent in the roster owns. The correct behavior is to note it under Out of
  my lane as "no owner in the roster", or leave it alone. The wrong behavior,
  seen on a real PR, is to route it to a "code-reviewer" that does not exist,
  which sends the finding nowhere. The runner fails any report that names an
  agent outside agents/.
