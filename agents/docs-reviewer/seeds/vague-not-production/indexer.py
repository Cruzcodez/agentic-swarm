import os, boto3
TABLE = os.environ["INDEX_TABLE"]
ddb = boto3.resource("dynamodb").Table(TABLE)

def put(report_id, text):
    ddb.put_item(Item={"PK": report_id, "SK": "META", "text": text})
