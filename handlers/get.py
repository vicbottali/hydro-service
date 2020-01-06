import json
import os
import decimal
import boto3

dynamodb = boto3.resource('dynamodb')


def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    #Get all records
    result = table.scan()

    # create a response
    response = {
        "headers" : {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
