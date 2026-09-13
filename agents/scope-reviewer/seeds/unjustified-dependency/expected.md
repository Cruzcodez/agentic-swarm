verdict: BLOCK
must_mention:
  - pandas
  - why
notes: |
  Three heavyweight dependencies (pandas pulls in numpy and pyarrow) added to
  a tool that reads a few CSVs, with a PR description that says "cleaner now"
  and nothing about why the standard library csv module wasn't enough.
  Correct behavior: BLOCK, ask for the justification. The agent should not
  argue pandas is wrong; it should ask for the reason to be written down.
