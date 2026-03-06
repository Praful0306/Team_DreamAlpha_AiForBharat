import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GROQ_API_KEY")
print(f"Testing key: {key[:10]}...")

client = OpenAI(
    api_key=key,
    base_url="https://api.groq.com/openai/v1"
)

try:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "Hello"}],
    )
    print("SUCCESS!")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"FAILED: {e}")
