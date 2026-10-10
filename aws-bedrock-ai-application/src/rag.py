import boto3
import json

AWS_REGION_BEDROCK = "ap-south-1"

client = boto3.client(
    service_name="bedrock-agent-runtime",
    region_name=AWS_REGION_BEDROCK
)

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        question = body.get("question")

        if not question:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "question needed"})
            }

        response = client.retrieve_and_generate(
            input={"text": question},
            retrieveAndGenerateConfiguration={
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": "YOUR_KB_ID",
                    "modelArn": "arn:aws:bedrock:ap-south-1::foundation-model/anthropic.claude-v2",
                },
            },
        )

        answer = response.get("output", {}).get("text", "No response generated")

        return {
            "statusCode": 200,
            "body": json.dumps({"answer": answer}),
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
        }
