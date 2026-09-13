# report-indexer infra

State is remote (S3 + DynamoDB lock), configured at init time from repository
variables so nothing account-specific is committed. Copy `backend.hcl.example`
to `backend.hcl` for local runs.

Deploy: run the Deploy workflow (manual trigger, production environment gate).
Teardown: `cd infra && terraform init -backend-config=backend.hcl && terraform destroy -var-file=prod.tfvars`.
The bucket has force_destroy so it empties itself. Nothing is created outside Terraform.
