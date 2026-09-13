verdict: BLOCK
must_mention:
  - "[security-reviewer"
  - "[docs-reviewer"
  - handler.py
  - deploy.yml
  - INDEX_TABLE
notes: |
  Problems in at least four lanes: a GitHub token hardcoded (security), static
  AWS keys in CI (security AND infra, should merge to one finding tagged with
  both), no permissions block (infra), INDEX_TABLE undocumented (docs), a test
  that can't fail (test). The merged verdict must be BLOCK. The report must
  show attribution brackets for at least security and docs, must group by
  file, and the static-keys finding should appear once with two agents named,
  not twice. This seed tests the merge, not the individual agents.
