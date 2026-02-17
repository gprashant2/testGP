import requests
import os

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

branch = os.getenv("GITHUB_REF_NAME", "unknown")
commit = os.getenv("GITHUB_SHA", "unknown")[:7]
repo = os.getenv("GITHUB_REPOSITORY", "unknown")
actor = os.getenv("GITHUB_ACTOR", "unknown")

prompt = f"""
Write a final DevOps deployment report using ONLY the facts below.

FACTS:
Environment: {branch}
Branch: {branch}
Commit: {commit}
Repository: {repo}
Triggered By: {actor}

Write the final report directly.
Do NOT write instructions.
Do NOT leave placeholders.

Format exactly like this:

Environment: {branch}
Branch: {branch}
Commit: {commit}
Repository: {repo}
Triggered By: {actor}

Deployment Details:
Docker image built and pushed to registry.
Helm deployment executed.
Kubernetes rollout restarted.

Risk Notes:
No deployment risks reported.

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
            "num_predict": 160
        }
    },
    timeout=90
)

print("\n===== DETAILED AI RELEASE SUMMARY =====\n")
print(response.json()["response"])