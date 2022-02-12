import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Notices")
    try:
        table.delete_item(Key={"NoticeID": event["id"]})
        response = table.scan()
    except Exception as e:
        print(e)
    else:
        return json.dumps(response) 
