import json
import boto3
from datetime import datetime,date

def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    table = dynamodb.Table('Notices')
    response=table.put_item(
           Item=event
             
    )
    return response["ResponseMetadata"]["HTTPStatusCode"]