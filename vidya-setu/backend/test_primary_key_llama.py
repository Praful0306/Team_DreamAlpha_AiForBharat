import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def test_primary_key_llama():
    print("--- Testing PRIMARY AWS Key with Llama 70B Profile ---")
    region = "us-east-1"
    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    
    # Isolation
    with open(".env", "r", encoding="utf-8") as f:
        env_content = f.read()
        if "AWS_SESSION_TOKEN" not in env_content:
            if "AWS_SESSION_TOKEN" in os.environ:
                del os.environ["AWS_SESSION_TOKEN"]

    try:
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        client = session.client("bedrock-runtime")
        
        # Use the specific profile ID that worked before
        model_id = "us.meta.llama3-1-70b-instruct-v1:0"
        prompt = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>Hi!<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
        
        request_body = {
            "prompt": prompt,
            "max_gen_len": 10,
        }

        print(f"Invoking {model_id}...")
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )
        print("✅ Success! Primary key is working in script.")
    except Exception as e:
        print(f"❌ Failed: {e}")

if __name__ == "__main__":
    test_primary_key_llama()
