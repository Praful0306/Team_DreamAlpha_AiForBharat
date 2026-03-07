import boto3
import json
import os
from dotenv import load_dotenv

# Force override to use .env values
load_dotenv(override=True)

def test_bedrock_llama():
    print("--- Bedrock Llama 3.1 70B Diagnostic ---")
    region = os.getenv("AWS_REGION", "us-east-1")
    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    session_token = os.getenv("AWS_SESSION_TOKEN")
    model_id = "meta.llama3-1-70b-instruct-v1:0"

    print(f"Region: {region}")
    print(f"Model: {model_id}")
    print(f"Using Access Key: {access_key}")
    
    try:
        client = boto3.client(
            "bedrock-runtime",
            region_name=region,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=session_token
        )
        
        # Small test prompt
        prompt = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>Hello, are you ready to teach?<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
        
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
    test_bedrock_llama()
