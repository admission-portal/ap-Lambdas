import json
import boto3
import pprint
from datetime import datetime, date

def lambda_handler(event,context):
    dynamodb = boto3.resource("dynamodb")
    client = boto3.client("dynamodb")
    table = dynamodb.Table("Submitted_Applications")
    id = event['applicationid']+"_"+event['email']
    
    singleapplicationdata = table.get_item(
        Key={
            'applicationid_email' : id}
            )
    if 'applicationid' in event and 'email' in event:
        response = table.update_item(
            Key={
                'applicationid_email' : id
                
            },
            UpdateExpression = "SET submission= :g",
            ExpressionAttributeValues = {':g' : [event['submission']]},
            ReturnValues = "UPDATED_NEW"
        )
        return {
            # this will also contain the XMLHTTPResponse status
            "status": "200",
            "body": response,
            }
    else:
        return{
            "status":"403",
            "body":"Forbidden"
        }