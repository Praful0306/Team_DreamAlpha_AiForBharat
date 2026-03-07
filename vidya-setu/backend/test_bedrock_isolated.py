import boto3
import json
import os
from dotenv import load_dotenv

# Force override to use .env values
load_dotenv(override=True)

def test_bedrock_llama_isolated():
    print("--- Bedrock Llama 3.1 70B Isolated Diagnostic ---")
    
    # Explicitly clear the session token if it's not in .env
    # This prevents the system's expired token from leaking in
    if "AWS_SESSION_TOKEN" not in open(".env").read():
        if "AWS_SESSION_TOKEN" in os.environ:
            print("Clearing expired AWS_SESSION_TOKEN from environment...")
            del os.environ["AWS_SESSION_TOKEN"]

    region = os.getenv("AWS_REGION", "us-east-1")
    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    model_id = "meta.llama3-1-70b-instruct-v1:0"

    print(f"Region: {region}")
    print(f"Model: {model_id}")
    print(f"Using Access Key: {access_key}")
    
    try:
        # Use session to be extra sure about credential isolation
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        client = session.client("bedrock-runtime")
        
        # Small test prompt
        prompt = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>Hello, be brief.<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
        
        request_body = {
            "prompt": prompt,
            "max_gen_len": 50,
            "temperature": 0.5,
        }

        print("Sending request to Bedrock...")
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )
        
        response_body = json.loads(response.get("body").read())
        generation = response_body.get("generation", "")
        
        print("\n✅ Success! Bedrock Response:")
        print(f"'{generation}'")
        
    except Exception as e:
        print(f"\n❌ Bedrock API Error: {e}")

if __name__ == "__main__":
    test_bedrock_llama_isolated()
