import os
import json
from dotenv import load_dotenv
from app.gemini_client import ask_gemini

load_dotenv()

print("--- Testing Chat (Doubt Solver) Keys ---")
print(f"CHAT_GROQ_API_KEY: {os.getenv('CHAT_GROQ_API_KEY')[:10]}...")
print(f"CHAT_FALLBACK_GROQ_KEYS count: {len(os.getenv('CHAT_FALLBACK_GROQ_KEYS', '').split(','))}")

try:
    response = ask_gemini(
        language="en",
        topic="Gravity",
        question="Why do things fall down?",
        student_name="Demo",
        student_age=12,
        student_grade="7"
    )
    print("\nResponse received:")
    print(json.dumps(response, indent=2))
    
    if "answer" in response and "analogy" in response:
        if "invalid" in response["answer"].lower() or "broken key" in response["analogy"].lower():
            print("\n❌ FAILED: Received mock response. Keys are likely restricted or invalid.")
        else:
            print("\n✅ SUCCESS: Received real AI response!")
    else:
        print("\n❌ FAILED: Response structure is unexpected.")

except Exception as e:
    print(f"\n❌ ERROR during test: {e}")
