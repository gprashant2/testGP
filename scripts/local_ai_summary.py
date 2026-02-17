import requests
import os

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

branch = os.getenv("GITHUB_REF_NAME", "unknown")
commit = os.getenv("GITHUB_SHA", "unknown")[:7]

prompt = f"""
You are a senior DevOps release engineer.

Generate a DETAILED deployment summary.

Environment: {branch}
Branch: {branch}
Commit: {commit}

Include sections:

Environment:
Branch:
Commit:

Release Changes:
Deployment Details:
Risk Notes:
Final Status:

Write detailed but concise professional release notes.
"""

response = requests.post(
    OLLAMA_URL,
    json={
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.4,
            "num_predict": 220
        }
    },
    timeout=90
)

print("\n===== DETAILED AI RELEASE SUMMARY =====\n")
print(response.json()["response"])

