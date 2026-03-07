import boto3
import os
from dotenv import load_dotenv

# Force override to use .env values
load_dotenv(override=True)

def diag_bedrock_ids():
    print("--- Bedrock Inference Profile Diagnostic ---")
    
    # Isolation as before
    if "AWS_SESSION_TOKEN" not in open(".env").read():
        if "AWS_SESSION_TOKEN" in os.environ:
            del os.environ["AWS_SESSION_TOKEN"]

    region = os.getenv("AWS_REGION", "us-east-1")
    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    try:
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        client = session.client("bedrock")
        
        print("Listing Foundation Models...")
        response = client.list_foundation_models(byOutputModality='TEXT')
        for model in response.get('modelSummaries', []):
            if "llama3-1-70b" in model['modelId']:
                print(f"Model ID: {model['modelId']}")
        
        print("\nListing Inference Profiles (if available)...")
        try:
            # Note: list_inference_profiles might require specific permissions
            # but is the correct way to find us.meta... style IDs
            profiles = client.list_inference_profiles()
            for profile in profiles.get('inferenceProfileSummaries', []):
                if "llama3-1-70b" in profile['inferenceProfileId']:
                    print(f"Inference Profile ID: {profile['inferenceProfileId']}")
        except Exception as e:
            print(f"Could not list inference profiles: {e}")
            print("Trying common cross-region ID: us.meta.llama3-1-70b-instruct-v1:0")

    except Exception as e:
        print(f"Error during diagnostic: {e}")

if __name__ == "__main__":
    diag_bedrock_ids()
