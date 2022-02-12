#Lambda Function to Get all the Applications that are being submitted by students

import json
import boto3
from datetime import datetime,date

def lambda_handler(event,context):
    #Connect to the dynamodb table
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    table = dynamodb.Table('Submitted_Applications')
    
    # The IF block gets you the details of a single student.
    # Check if the query string has Application ID and the ID of the student that submitted the application
    if 'id' in event['params']['querystring'] and '_' in event['params']['querystring']['id']:
        # Extract the student ID
        id = event['params']['querystring']['id']
        # Construct the response by getting the single Item from the table
        response = table.get_item(
            Key={
                "applicationid_email" :event['params']['querystring']['id']
                
            }
            )
        
        return {
            "status":200,
            "body":response
        }
        # The ELIF block gets you the details of all the students who submitted that Applicaiton with that particular ID.
    elif 'id' in event['params']['querystring'] and '_' not in event['params']['querystring']['id']:
        
        submittedapplications = table.scan()
        response = {"Items":[]}
        id = event['params']['querystring']['id']
        x = {"ID":[]}
        for i in submittedapplications['Items']:
            if id in i['applicationid_email']:
                x['ID'].append(i['applicationid_email'])
                response['Items'].append(i)
        
        # for key in submittedapplications['Items']:
        #     for internalkey in key['submission']:
        #         if id in internalkey['submissiondata']['ApplicationID']:
        #             x['ID'].append(key['applicationid_email'])
        #             response['Items'].append(key)
                
        return{
            "status":200,
            "body": response
            # "body":submittedapplications['Items'],
        }
         
    else:
        return {
            'status' : 400,
            'body':'Forbidden'
        }
