# will return the queries of specific user
import json
import boto3
def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('APStudents')    
    print(event)
    if 'email' in event['params']['querystring']:
        resp = table.get_item(
                Key={
                    "email" :event['params']['querystring']['email']
                }
            )
                    
    if 'email' in event['params']['querystring'] and 'Item' in resp  :
        return {
            'status':200,
            'response':{
                'queries':resp['Item']['queries']
            },
            'event':event
        }
    else:
        return {
            'status':400,
            'response':{
                'messa':'user not available'
            }
        }
