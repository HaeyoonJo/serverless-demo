import json
import logging
import boto3
from datetime import date, datetime
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    process = None
    status_code = 0
    today = date.today()
    d_time = datetime.datetime.now().replace(microsecond=0).isoformat()
    name = event['Name']
    age = event['Age']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ListOfName')
    try:
        response = table.update_item(
            Key = {'name': name, 'age': age},
            UpdateExpression="set createdAt = :p",
            ExpressionAttributeValues={':p': d_time},
            ReturnValues = 'UPDATED_NEW'
        )
    except Exception as e:
        logger.error("ERROR!!: %s", str(e))
    else:
        logger.info("response: %s", response['ResponseMetadata']['HTTPStatusCode'])
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        process = True
    response = {
        'process': process,
        'Status_code': status_code,
        'Name': name,
        'Age': age
    }
    return response