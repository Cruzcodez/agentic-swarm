import boto3

# Quick fix for the demo, TODO move to env
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def get_client():
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name="us-east-1",
    )


def list_reports(bucket: str):
    client = get_client()
    resp = client.list_objects_v2(Bucket=bucket, Prefix="reports/")
    return [o["Key"] for o in resp.get("Contents", [])]
