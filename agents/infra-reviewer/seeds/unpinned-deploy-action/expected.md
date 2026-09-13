verdict: BLOCK
must_mention:
  - release.yml
  - deploy-to-lambda
  - "@main"
notes: |
  Credentials are done right (OIDC, account ID from a variable). But a
  third-party action pinned to @main is executed with those credentials. If
  that repo is compromised, so is this deploy. Correct behavior: BLOCK on
  deploy-to-lambda@main specifically, say to pin to a commit SHA. The
  configure-aws-credentials@v4 pin is also worth a mention but it's a
  first-party action; a WARN there is fine.
