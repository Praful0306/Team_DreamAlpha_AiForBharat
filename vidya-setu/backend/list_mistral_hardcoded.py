import boto3

CHAT_ACCESS_KEY = "AKIAZPSKJRD3JWWDN7SH"
CHAT_SECRET_KEY = "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"
REGION = "us-east-1"

def list_mistral_hardcoded():
    print(f"Listing models with key: {CHAT_ACCESS_KEY}")
    try:
        client = boto3.client(
            "bedrock",
            region_name=REGION,
            aws_access_key_id=CHAT_ACCESS_KEY,
            aws_secret_access_key=CHAT_SECRET_KEY
        )
        
        response = client.list_foundation_models(byOutputModality='TEXT')
        found = False
        for model in response.get('modelSummaries', []):
            if "mistral" in model['modelId'].lower():
                print(f"ID: {model['modelId']} | Name: {model['modelName']}")
                found = True
        
        if not found:
            print("No Mistral models found.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_mistral_hardcoded()
