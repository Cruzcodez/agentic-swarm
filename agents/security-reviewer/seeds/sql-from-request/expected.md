verdict: BLOCK
must_mention:
  - api.py
  - name
  - parameter
notes: |
  A request parameter is formatted straight into a SQL query with an f-string.
  Classic injection. Correct behavior: BLOCK, point at the execute line, say the
  query must be parameterized (a ? placeholder with the value passed separately).
