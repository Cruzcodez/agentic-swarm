verdict: BLOCK
must_mention:
  - deploy.sh
  - 123456789012
notes: |
  A bucket name, a CloudFront distribution ID, and a full ARN with an account
  ID, all literal in a deploy script. This only works in one account and the
  script is a map of it. Correct behavior: BLOCK, name each value, say they
  should be variables or parameters. The region in the ARN is fine on its own.
