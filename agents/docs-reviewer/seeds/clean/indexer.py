"""Index PDF reports from an S3 bucket into a DynamoDB table.

Each PDF becomes one META item plus one PAGE item per page, keyed so a report
can be fetched by ID and listed by customer (via the GSI on customer_id).
Customer ID comes from the object's `customer` metadata tag.
"""
import argparse
import logging
import os
from concurrent.futures import ThreadPoolExecutor

import boto3
from pypdf import PdfReader
from io import BytesIO

BUCKET = os.environ["REPORTS_BUCKET"]
TABLE = os.environ["INDEX_TABLE"]
REGION = os.environ.get("AWS_REGION", "us-east-1")

log = logging.getLogger("indexer")


def list_pdfs(s3):
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=BUCKET):
        for obj in page.get("Contents", []):
            if obj["Key"].lower().endswith(".pdf"):
                yield obj["Key"]
            else:
                log.info("skipping non-PDF %s", obj["Key"])


def index_one(s3, table, key, dry_run):
    head = s3.head_object(Bucket=BUCKET, Key=key)
    customer = head.get("Metadata", {}).get("customer", "unknown")
    report_id = key.rsplit("/", 1)[-1].removesuffix(".pdf")
    if dry_run:
        log.info("would index %s (customer=%s)", report_id, customer)
        return
    body = s3.get_object(Bucket=BUCKET, Key=key)["Body"].read()
    reader = PdfReader(BytesIO(body))
    with table.batch_writer() as batch:
        batch.put_item(Item={"PK": report_id, "SK": "META", "customer_id": customer, "pages": len(reader.pages)})
        for i, page in enumerate(reader.pages):
            batch.put_item(Item={"PK": report_id, "SK": f"PAGE#{i}", "text": page.extract_text() or ""})
    log.info("indexed %s (%d pages)", report_id, len(reader.pages))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--workers", type=int, default=8, help="parallel workers (default 8)")
    ap.add_argument("--dry-run", action="store_true", help="list what would be indexed, write nothing")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    s3 = boto3.client("s3", region_name=REGION)
    table = boto3.resource("dynamodb", region_name=REGION).Table(TABLE)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for key in list_pdfs(s3):
            ex.submit(index_one, s3, table, key, args.dry_run)


if __name__ == "__main__":
    main()
