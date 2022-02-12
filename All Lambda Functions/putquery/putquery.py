import json
import boto3
from datetime import datetime,date

def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    table = dynamodb.Table('APStudents')
    requestJSON = event
    today = date.today()
    timestamp = datetime.now().strftime("%Y-%m-%d GMT: %H:%M:%S")
    
    if 'qObj' in event:
        try:
            response=table.update_item(
           Key={
                    'email':event['email'] ,
               
           },
           UpdateExpression="set queries =list_append(queries, :g)",
           ExpressionAttributeValues={':g': [event['qObj']]},
    
           ReturnValues="UPDATED_NEW"   
        )
            return {
                # this will also contain the XMLHTTPResponse status
                'status':'200',
                'body':response
            }    
        except :
            return{
            'status':'400',
            'body':{
                'message':'user  email does not exit !'
            }
        }
        
    else :
        return{
            'status':'400',
            'body':{
                'message':'something went wrong !'
            }
        }
