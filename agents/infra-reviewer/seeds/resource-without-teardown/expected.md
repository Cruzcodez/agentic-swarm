verdict: BLOCK
must_mention:
  - dashboard
  - SNS
  - teardown
notes: |
  The Terraform resources have a destroy path. But the deploy script says two
  resources (a dashboard and an SNS topic) are created by hand in the console.
  Nothing destroys those. Also the bucket will refuse to destroy if it has
  objects. Correct behavior: BLOCK on the two manual resources with no
  removal path, WARN or note the non-empty bucket problem.
