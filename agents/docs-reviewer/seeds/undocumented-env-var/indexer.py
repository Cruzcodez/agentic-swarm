import os
import boto3

BUCKET = os.environ["REPORTS_BUCKET"]
TABLE = os.environ["INDEX_TABLE"]
BATCH = int(os.environ.get("INDEX_BATCH_SIZE", "25"))
REGION = os.environ.get("AWS_REGION", "us-east-1")


def run():
    s3 = boto3.client("s3", region_name=REGION)
    ddb = boto3.resource("dynamodb", region_name=REGION).Table(TABLE)
    # ... indexing logic ...
