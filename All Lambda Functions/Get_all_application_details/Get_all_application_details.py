#Lambda function to Get all the Applications created by an admin/Institute
import json
import boto3
from datetime import datetime,date

def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    table = dynamodb.Table('Applications')
    response=table.scan()
    return response