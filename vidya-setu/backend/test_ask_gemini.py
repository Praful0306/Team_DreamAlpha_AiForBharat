from app.gemini_client import ask_gemini
import json

print("Testing ask_gemini with all keys...")
result = ask_gemini(
    language="en",
    topic="Physics",
    question="what is light",
    student_name="Rahul",
    student_age=12,
    student_grade="7"
)

print("\nRESULT:")
print(json.dumps(result, indent=2))

if "invalid" in result.get("answer", "").lower():
    print("\n❌ STILL RETURNING MOCK ERROR.")
else:
    print("\n✅ SUCCESS! AI IS RESPONDING.")
