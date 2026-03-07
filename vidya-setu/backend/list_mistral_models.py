import boto3
import os
import json
from dotenv import load_dotenv

load_dotenv(override=True)

def list_mistral_models():
    region = os.getenv("AWS_REGION", "us-east-1")
    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    
    # Isolation
    session_token = None
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            if "CHAT_AWS_SESSION_TOKEN" in f.read():
                session_token = os.getenv("CHAT_AWS_SESSION_TOKEN")

    print(f"Listing models in {region}...")
    try:
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=session_token,
            region_name=region
        )
        client = session.client("bedrock")
        
        response = client.list_foundation_models(byOutputModality='TEXT')
        found = False
        for model in response.get('modelSummaries', []):
            if "mistral" in model['modelId'].lower():
                print(f"ID: {model['modelId']} | Name: {model['modelName']}")
                found = True
        
        if not found:
            print("No Mistral models found in this region/account.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_mistral_models()
