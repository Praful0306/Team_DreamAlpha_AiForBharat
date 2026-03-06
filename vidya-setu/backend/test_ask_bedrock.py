from app.bedrock_client import call_bedrock
import json

print("Testing call_bedrock (Mock Mode should be default true)...")
result = call_bedrock(
    language="en",
    topic="Physics",
    question="what is gravity",
    student_name="Rahul",
    student_age=12,
    student_grade="7"
)

print("\nRESULT:")
print(json.dumps(result, indent=2))
