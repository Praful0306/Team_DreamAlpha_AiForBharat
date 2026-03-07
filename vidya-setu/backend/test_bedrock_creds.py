import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def test_bedrock():
    try:
        print(f"Region: {os.getenv('AWS_REGION')}")
        print(f"Access Key: {os.getenv('AWS_ACCESS_KEY_ID')}")
        
        client = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION", "us-east-1"))
        
        # Simple list models or small invoke to test
        response = client.list_foundation_models()
        print("Success! Models found.")
        # Print first few models
        for model in response.get('modelSummaries', [])[:3]:
            print(f"- {model['modelId']}")
            
    except Exception as e:
        print(f"Error testing Bedrock: {e}")

if __name__ == "__main__":
    test_bedrock()
