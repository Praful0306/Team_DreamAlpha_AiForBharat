import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def test_inference_profile():
    print("--- Bedrock Llama 3.1 70B Inference Profile Test ---")
    
    # Isolation
    with open(".env", "r", encoding="utf-8") as f:
        env_content = f.read()
        if "AWS_SESSION_TOKEN" not in env_content:
            if "AWS_SESSION_TOKEN" in os.environ:
                del os.environ["AWS_SESSION_TOKEN"]

    region = os.getenv("AWS_REGION", "us-east-1")
    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    
    # The Inference Profile ID
    model_id = "us.meta.llama3-1-70b-instruct-v1:0"

    print(f"Region: {region}")
    print(f"Targeting: {model_id}")
    
    try:
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        client = session.client("bedrock-runtime")
        
        prompt = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>Hi.<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
        request_body = {
            "prompt": prompt,
            "max_gen_len": 10,
            "temperature": 0.5,
        }

        print(f"Invoking {model_id}...")
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )
        
        print("✅ SUCCESS! Inference Profile ID worked.")
        
    except Exception as e:
        print(f"❌ Failed with {model_id}: {e}")

if __name__ == "__main__":
    test_inference_profile()
