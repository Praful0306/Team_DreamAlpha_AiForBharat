import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

primary_key = os.getenv("GROQ_API_KEY")
fallback_keys_str = os.getenv("FALLBACK_GROQ_KEYS", "")
fallback_keys = [k.strip() for k in fallback_keys_str.split(",") if k.strip()]

all_keys = [primary_key] + fallback_keys

for i, key in enumerate(all_keys):
    if not key or key == "your_groq_key_here":
        continue
    print(f"Testing key {i} ({key[:10]}...): ", end="", flush=True)
    client = OpenAI(
        api_key=key,
        base_url="https://api.groq.com/openai/v1"
    )
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )
        print("SUCCESS!")
    except Exception as e:
        print(f"FAILED: {e}")
