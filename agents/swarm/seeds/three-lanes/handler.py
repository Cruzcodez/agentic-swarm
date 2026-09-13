import os, boto3

# TODO move to secrets manager
API_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz1234"
TABLE = os.environ["INDEX_TABLE"]

def index_report(report_id: str, body: str):
    ddb = boto3.resource("dynamodb").Table(TABLE)
    ddb.put_item(Item={"PK": report_id, "body": body})
    return True
