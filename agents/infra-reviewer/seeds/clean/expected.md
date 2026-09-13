verdict: PASS
notes: |
  OIDC credentials, account and region from variables, deploy actions pinned
  to SHAs with version comments, permissions block present, manual trigger
  with an environment gate, resources tagged, log retention set, bucket has
  force_destroy, README says teardown is complete and nothing is manual.
  Correct behavior: PASS.

  First run, the agent BLOCKED because there was no remote backend (state
  on an ephemeral runner means destroy removes nothing) and the workflow
  referenced a prod.tfvars that didn't exist. Both were right. Both fixed.
