import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

primary_key = os.getenv("GROQ_API_KEY")
fallback_keys_str = os.getenv("FALLBACK_GROQ_KEYS", "")
fallback_keys = [k.strip() for k in fallback_keys_str.split(",") if k.strip()]

all_keys = [primary_key] + fallback_keys
results = []

for i, key in enumerate(all_keys):
    if not key or key == "your_groq_key_here":
        continue
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
        results.append(f"Key {i} ({key[:10]}...): SUCCESS")
    except Exception as e:
        results.append(f"Key {i} ({key[:10]}...): FAILED - {str(e)[:50]}")

with open("key_test_results.txt", "w") as f:
    f.write("\n".join(results))
print("Results written to key_test_results.txt")
