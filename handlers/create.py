import json
import logging
import os
import time
import uuid
from datetime import datetime

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    
    timestamp = str(datetime.utcnow().isoformat())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        "recorded": timestamp,
        "ph": data['ph'],
        "water_temp": data['water_temp'],
        "air_temp": data['air_temp'],
        "humidity": data['humidity']
    }

    # write to db
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response