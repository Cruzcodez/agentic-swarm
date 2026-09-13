verdict: BLOCK
must_mention:
  - handler.py
  - credential

notes: |
  An AWS access key pair hardcoded in source and passed straight into
  boto3.client(). The values are Amazon's documented example keys, so they
  aren't live, and a sharp agent will notice that. It must BLOCK anyway: the
  pattern is the problem. This is code that uses the string as a credential,
  and the placeholder exists to be replaced with a real one. First run of this
  seed, the agent recognized the example key and downgraded to WARN. That's
  why the charter now says to block on the pattern regardless of the value.
  must_mention "environment" checks that the fix (load from env / default
  credential chain) is stated.
