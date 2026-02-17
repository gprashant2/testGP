import requests
import os

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

branch = os.getenv("GITHUB_REF_NAME", "unknown")
commit = os.getenv("GITHUB_SHA", "unknown")[:7]
repo = os.getenv("GITHUB_REPOSITORY", "unknown")
actor = os.getenv("GITHUB_ACTOR", "unknown")

prompt = f"""
You are a DevOps deployment reporter.

Use ONLY provided facts.
Do NOT invent release notes.
Do NOT guess risk.
If data missing → say NOT PROVIDED.

FACTS:
Repository: {repo}
Environment: {branch}
Branch: {branch}
Commit: {commit}
Triggered By: {actor}

Output STRICT format:

Environment:
Branch:
Commit:
Repository:
Triggered By:

Deployment Details:
Docker image built and pushed to registry.
Helm deployment executed.
Kubernetes rollout restarted.

Risk Notes:
NOT PROVIDED

Final Status:
Deployment completed successfully.
"""

response = requests.post(
    OLLAMA_URL,
    json={
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 220
        }
    },
    timeout=90
)

print("\n===== DETAILED AI RELEASE SUMMARY =====\n")
print(response.json()["response"])

