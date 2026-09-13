verdict: BLOCK
must_mention:
  - test_pricing.py
  - assert
notes: |
  Three tests, none of which can fail. The first asserts not-None on a
  function that can't return None. The second compares the function to
  itself. The third swallows the exception and passes whether or not it's
  raised. Correct behavior: BLOCK, name each test and what it should assert
  instead (== 90.0, == 60.0, pytest.raises(ValueError)).
