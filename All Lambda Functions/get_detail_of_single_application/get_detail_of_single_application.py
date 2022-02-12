# will return the a specific applications metadata
import json
import boto3
def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Applications')    

    print(event)
    if 'ApplicationID' in event:
        resp = table.get_item(
                Key={
                    "ApplicationID" :event['ApplicationID']
                }
            )
    
    # return resp      
    if 'ApplicationID' in event and 'Item' in resp:
        return {
            'status':200,
            'response':resp['Item']
        }
    else:
        return {
            'status':400,
            'response':{
                'message':'Appication not available!'
            }
        }
