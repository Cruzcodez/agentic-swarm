verdict: BLOCK
must_mention:
  - lambda-role.json
  - "*"
notes: |
  Action * on Resource * for a workload that touches one bucket and one table.
  The README in the seed says exactly what the Lambda does, so the agent has
  what it needs to say what the policy should be scoped to. Correct behavior:
  BLOCK, say the policy should name s3:GetObject on the bucket and
  dynamodb:PutItem on the table, nothing more.
