import os, boto3

# TODO move to secrets manager
API_TOKEN = "ghp_EXAMPLE_NOT_A_REAL_TOKEN_0000000000"
TABLE = os.environ["INDEX_TABLE"]

def index_report(report_id: str, body: str):
    ddb = boto3.resource("dynamodb").Table(TABLE)
    ddb.put_item(Item={"PK": report_id, "body": body})
    return True
