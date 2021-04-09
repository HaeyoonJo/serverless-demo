import json
import logging
import boto3
from boto3.dynamodb.conditions import Key

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ListOfName')
    createdAt = ''
    name = event['Name']
    age = event['Age']
    try:
        response = table.get_item(Key={'name': name, 'age': age})
    except Exception as e:
        logger.error('ERROR couldn\'t get response: %s', str(e))
    else:
        logger.info('response get_item data:%s', response['Item'])
        createdAt = response['Item']['createdAt']
    response = {
        'createdAt': createdAt,
        'userName': name
    }
    return response