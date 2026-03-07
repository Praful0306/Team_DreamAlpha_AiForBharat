import boto3
import json

# HARDCODED TEST - NO DOTENV
# Using keys directly from the file to avoid any environment issues
ACCESS_KEY = "AKIAZPSKJRD3HL2IPMFR"
SECRET_KEY = "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"
REGION = "us-east-1"

def test_hardcoded():
    print(f"Testing with Access Key: {ACCESS_KEY}")
    try:
        client = boto3.client(
            "bedrock", # Using 'bedrock' to list models
            region_name=REGION,
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
        )
        
        response = client.list_foundation_models()
        print("✅ Success! list_foundation_models worked.")
        # Check if Llama 3.1 70B is in the list
        llama_found = False
        for model in response.get('modelSummaries', []):
            if "llama3-1-70b" in model['modelId']:
                print(f"  - Found: {model['modelId']}")
                llama_found = True
        
        if not llama_found:
            print("  - ⚠️ Llama 3.1 70B NOT FOUND in this region/account.")

    except Exception as e:
        print(f"❌ Hardcoded Test Failed: {e}")

if __name__ == "__main__":
    test_hardcoded()
