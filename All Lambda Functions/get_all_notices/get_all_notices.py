#Function to get all the notices created by the institute/admin
import json
import boto3

def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Notices')
    response=table.scan()
    return json.dumps(response)
