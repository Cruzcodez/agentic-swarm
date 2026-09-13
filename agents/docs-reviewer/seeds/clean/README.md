# report-indexer

Indexes PDF reports from an S3 bucket into a DynamoDB table so they can be fetched by report ID and listed by customer.

## Prerequisites

- Python 3.9 or newer
- Terraform 1.5 or newer
- AWS credentials configured the normal way (`aws configure`, environment variables, or a profile). Deploying needs permission to create the resources in `infra/`. Running the indexer needs read on the bucket and write on the table.

## Setting it up

The bucket and table are created by Terraform. Do this once:

```bash
cd infra
terraform init
terraform apply -var bucket_name=your-bucket -var table_name=report-index
cd ..
```

## Running it

From a fresh clone, after setup:

```bash
pip install -r requirements.txt
export REPORTS_BUCKET=your-bucket
export INDEX_TABLE=report-index
python indexer.py --workers 4
```

`--workers` controls how many PDFs are processed at once. Default is 8. `--dry-run` lists what would be indexed and writes nothing.

## Configuration

| Variable | Required | What it's for |
| --- | --- | --- |
| `REPORTS_BUCKET` | yes | S3 bucket holding the PDFs |
| `INDEX_TABLE` | yes | DynamoDB table to write into |
| `AWS_REGION` | no | Defaults to us-east-1 |

The customer for each report is read from the S3 object's `customer` metadata tag. Objects without it are indexed under `unknown`.

## How it's stored

One table. Each report is a `META` item (page count, customer) plus one `PAGE#n` item per page holding the extracted text. A global secondary index on `customer_id` supports listing a customer's reports. The reasoning is in [docs/decisions/0002](docs/decisions/0002-dynamodb-single-table.md).

## Limitations

- PDF only. Other objects are skipped and logged.
- No retry on DynamoDB throttling. A large batch against a busy table can fail partway; re-running is safe because items are overwritten by key.
- Text extraction is only as good as the PDF. Scanned images come back empty.

## Not production ready

This is a proof of concept. Before real use it needs: retry with backoff on throttling, a dead-letter path for PDFs that fail to parse, and an IAM policy scoped to this one bucket and one table instead of the broad role it currently runs under.

## Tearing it down

```bash
cd infra && terraform destroy
```

The bucket has `force_destroy` set, so Terraform empties it. The log group keeps 14 days of logs and is removed with the rest. Nothing is created outside Terraform.
