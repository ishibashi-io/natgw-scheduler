import json
import requests

def lambda_handler(event, context):
    response = requests.get("https://www.industry-one.com/")
    if response.status_code != 200:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "failed to get industry-one.com",
            }),
        }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
