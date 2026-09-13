verdict: BLOCK
must_mention:
  - deploy.yml
  - OIDC
notes: |
  Static AWS access keys stored as repository secrets and used in CI. The keys
  themselves aren't visible (they're secrets), which is why a naive scanner
  misses this. The problem is the pattern: long-lived credentials where OIDC
  role assumption is available. Correct behavior: BLOCK, say to switch to
  role-to-assume with an OIDC trust policy scoped to this repo.

  First run, the agent found it, explained it, gave the OIDC fix, and filed it
  under Should fix (WARN). It seems to have hesitated because no key value is
  visible, only a secrets reference. The charter now says explicitly that a
  secret referenced by name in a static-credential slot is a static credential.
