import json
from src.rag import lambda_handler

event = {
    "body": json.dumps({
        "question": "What is AWS Bedrock?"
    })
}

response = lambda_handler(event, None)

print("Status Code:", response["statusCode"])
print("Response:", json.loads(response["body"]))