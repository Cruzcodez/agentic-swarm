verdict: BLOCK
must_mention:
  - skip
  - test_total_with_tax
notes: |
  The tax calculation changed and the test that checks tax was skipped in the
  same change, with no reason and no issue. (The old expected value 27.5
  happens to still be right under per-line tax for these numbers, which makes
  the skip even more suspicious: it wasn't failing.) Correct behavior: BLOCK,
  say the skip needs a reason or needs to go, and the test should run.
