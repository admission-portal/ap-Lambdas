import json
import boto3
from datetime import datetime

statuscode = 200
body = ''
def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    table = dynamodb.Table('APStudents')
    try:
        response = table.scan(
            AttributesToGet=[
            'email',
            'queries'
        ],
            Select='SPECIFIC_ATTRIBUTES'    
            )
        timestamp = datetime.now().strftime("%Y-%m-%d GMT: %H:%M:%S")
        statuscode = 200
        body = response['Items']
            
    except:
        statuscode = 400
        body = "400 Bad Request"
    
    
    return {
        'statuscode' : statuscode,
        'timestamp' : timestamp,
        'body' : body
    }