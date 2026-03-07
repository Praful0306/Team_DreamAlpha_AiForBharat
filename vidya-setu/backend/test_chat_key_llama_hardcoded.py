import boto3
import json

# HARDCODED CHAT KEYS
CHAT_ACCESS_KEY = "AKIAZPSKJRD3JWWDN7SH"
CHAT_SECRET_KEY = "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"
REGION = "us-east-1"

def test_chat_llama_hardcoded():
    print(f"Testing Chat Key: {CHAT_ACCESS_KEY}")
    try:
        client = boto3.client(
            "bedrock-runtime",
            region_name=REGION,
            aws_access_key_id=CHAT_ACCESS_KEY,
            aws_secret_access_key=CHAT_SECRET_KEY
        )
        
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
        print("✅ Success! Chat key is authorized.")
    except Exception as e:
        print(f"❌ Failed: {e}")

if __name__ == "__main__":
    test_chat_llama_hardcoded()
