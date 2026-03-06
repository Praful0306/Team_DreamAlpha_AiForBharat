import os
import json
from dotenv import load_dotenv
from app.groq_client import generate_quiz

load_dotenv()

def test_module_difficulty(mod_id):
    print(f"\n--- Testing Difficulty for Module {mod_id} ---")
    try:
        response = generate_quiz(
            module_id=mod_id,
            module_title="Photosynthesis",
            subject="Biology",
            student_name="Tester",
            student_age=13,
            student_grade="8"
        )
        print(f"Sample Question 1 (Module {mod_id}):")
        print(f"[{response['questions'][0]['difficulty']}] {response['questions'][0]['question']}")
    except Exception as e:
        print(f"Error: {e}")

# Test Module 1 (should be very basic)
test_module_difficulty(1)

# Test Module 3 (should be advanced focus)
test_module_difficulty(3)
