import os
import boto3

# Switched from the Postgres table to DynamoDB single-table design.
# PK = report_id, SK = "META" | "PAGE#<n>". GSI1 on customer_id for lookups.
TABLE = os.environ["INDEX_TABLE"]
ddb = boto3.resource("dynamodb").Table(TABLE)


def put_report(report_id: str, customer_id: str, pages: list[str]):
    with ddb.batch_writer() as batch:
        batch.put_item(Item={"PK": report_id, "SK": "META", "GSI1PK": customer_id})
        for i, text in enumerate(pages):
            batch.put_item(Item={"PK": report_id, "SK": f"PAGE#{i}", "text": text})
