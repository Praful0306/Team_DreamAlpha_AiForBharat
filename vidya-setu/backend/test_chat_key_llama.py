import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def test_chat_key_llama():
    print("--- Testing CHAT_AWS Key with Llama 70B ---")
    region = os.getenv("AWS_REGION", "us-east-1")
    access_key = os.getenv("CHAT_AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("CHAT_AWS_SECRET_ACCESS_KEY")
    
    session_token = None
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            if "CHAT_AWS_SESSION_TOKEN" in f.read():
                session_token = os.getenv("CHAT_AWS_SESSION_TOKEN")

    try:
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=session_token,
            region_name=region
        )
        client = session.client("bedrock-runtime")
        
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
        print("✅ Success! Key is authorized.")
    except Exception as e:
        print(f"❌ Failed: {e}")

if __name__ == "__main__":
    test_chat_key_llama()
