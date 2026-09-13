verdict: PASS
notes: |
  Nothing wrong here. Credentials from the execution role, bucket name from the
  environment, prefix validated, errors handled without leaking internals. The
  .env.example is documentation, not a secret.

  This seed exists to catch an agent that blocks everything. A reviewer that
  finds problems in clean code gets ignored as fast as one that finds nothing.
  Correct behavior: PASS. A WARN with a real reason is acceptable. BLOCK is a
  failure.
