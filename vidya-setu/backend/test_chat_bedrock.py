import boto3
import json
import os
from dotenv import load_dotenv

# Use override=True to ensure .env values take precedence
load_dotenv(override=True)

def test_bedrock_chat_creds():
    print("--- Verifying Chat Bedrock Credentials ---")
    
    region = os.getenv("AWS_REGION", "us-east-1")
    access_key = os.getenv("CHAT_AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("CHAT_AWS_SECRET_ACCESS_KEY")
    # Check for session token (isolating from system env)
    session_token = None
    with open(".env", "r", encoding="utf-8") as f:
        env_content = f.read()
        if "CHAT_AWS_SESSION_TOKEN" in env_content and "your_chat_session_token_optional" not in env_content:
            session_token = os.getenv("CHAT_AWS_SESSION_TOKEN")

    print(f"Region: {region}")
    print(f"Access Key ID: {access_key[:10]}...")
    
    if not access_key or "your_" in access_key:
        print("❌ ERROR: CHAT_AWS_ACCESS_KEY_ID is missing or still a placeholder.")
        return

    try:
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=session_token,
            region_name=region
        )
        client = session.client("bedrock-runtime")
        
        # Mistral 7B Test
        model_id = "mistral.mistral-7b-instruct-v0:2"
        prompt = "<s>[INST] Hello! Just say 'Yes, Vidya-Setu is online with Mistral 7B.' [/INST]"
        
        request_body = {
            "prompt": prompt,
            "max_tokens": 64,
            "temperature": 0.5,
        }

        print(f"Invoking {model_id} for chat verification...")
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )
        
        response_body = json.loads(response.get("body").read())
        generation = ""
        if "outputs" in response_body:
            generation = response_body["outputs"][0]["text"].strip()
        else:
            generation = response_body.get("generation", "").strip()
            
        print(f"✅ SUCCESS! Response: {generation}")

    except Exception as e:
        print(f"❌ FAILED: {e}")

if __name__ == "__main__":
    test_bedrock_chat_creds()
