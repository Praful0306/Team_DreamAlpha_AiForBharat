import boto3
import os
from dotenv import load_dotenv

# Force override to use .env values even if system env vars exist
load_dotenv(override=True)

def test_bedrock():
    try:
        region = os.getenv("AWS_REGION", "us-east-1")
        access_key = os.getenv("AWS_ACCESS_KEY_ID")
        secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        session_token = os.getenv("AWS_SESSION_TOKEN") # Might be None for AKIA keys
        
        print(f"Region: {region}")
        print(f"Access Key: {access_key}")
        print(f"Has Session Token: {session_token is not None}")
        
        client = boto3.client(
            "bedrock-runtime",
            region_name=region,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=session_token
        )
        
        # Test a small invoke or list
        response = client.list_foundation_models()
        print("Success! Models found using .env credentials.")
        for model in response.get('modelSummaries', [])[:3]:
            print(f"- {model['modelId']}")
            
    except Exception as e:
        print(f"Error testing Bedrock with .env keys: {e}")

if __name__ == "__main__":
    test_bedrock()
