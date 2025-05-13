import boto3
import json

# AWS Bedrock client (connecting to AWS Bedrock)
bedrock_client = boto3.client('bedrock-runtime', region_name='eu-west-1')

def get_titan_embedding(text: str) :
    response = bedrock_client.invoke_model( # Call the Titan embedding model
        modelId = "amazon.titan-embed-text-v2:0",
        body = json.dumps({"inputText": text}), # Send the text to embed
        contentType = "application/json",
        accept = "application/json"
    )
    result = json.loads(response['body'].read())
    return result['embedding'] # The embedded result