verdict: BLOCK
must_mention:
  - test_notify.py
  - mock
notes: |
  The test patches alert_if_over and then calls alert_if_over. It's testing
  the mock. The real function's logic (the comparison, the message format)
  is never executed. Correct behavior: BLOCK, say to mock send_alert instead
  and assert alert_if_over calls it with the right message when over the
  limit and doesn't when under.
