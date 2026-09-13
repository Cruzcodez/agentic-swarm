import os
import boto3
from botocore.exceptions import ClientError

BUCKET = os.environ["REPORTS_BUCKET"]


def get_client():
    # Credentials come from the execution role. Nothing is passed here.
    return boto3.client("s3")


def list_reports(prefix: str = "reports/") -> list[str]:
    if not prefix.startswith("reports/"):
        raise ValueError("prefix must stay under reports/")
    client = get_client()
    try:
        resp = client.list_objects_v2(Bucket=BUCKET, Prefix=prefix)
    except ClientError as e:
        raise RuntimeError("could not list reports") from e
    return [o["Key"] for o in resp.get("Contents", [])]
