import os
import json
from dotenv import load_dotenv
from app.groq_client import generate_course_outline

load_dotenv()

print("--- Testing Module Generation Keys ---")
print(f"MODULE_GROQ_API_KEY: {os.getenv('MODULE_GROQ_API_KEY')[:10]}...")
print(f"MODULE_FALLBACK_GROQ_KEYS count: {len(os.getenv('MODULE_FALLBACK_GROQ_KEYS', '').split(',')) if os.getenv('MODULE_FALLBACK_GROQ_KEYS') else 0}")

try:
    response = generate_course_outline(
        subject="Physics",
        reference_notes="Intro to Gravity",
        student_name="Demo",
        student_age=12,
        student_grade="7"
    )
    print("\nResponse received:")
    print(json.dumps(response, indent=2))
    
    if "modules" in response and len(response["modules"]) > 0:
        print("\n✅ SUCCESS: Received real AI response for module generation!")
    else:
        print("\n❌ FAILED: Response structure is unexpected.")

except Exception as e:
    print(f"\n❌ ERROR during test: {e}")
