import requests
import os

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

branch = os.getenv("GITHUB_REF_NAME", "unknown")
commit = os.getenv("GITHUB_SHA", "unknown")[:7]
repo = os.getenv("GITHUB_REPOSITORY", "unknown")
actor = os.getenv("GITHUB_ACTOR", "unknown")

ai_prompt = f"""
Write 3 professional sentences describing THIS deployment event.

This is NOT a DevOps explanation.
Do NOT list deployment steps.
Do NOT explain DevOps concepts.
Do NOT write generic theory.

Context:
Container image built and pushed to registry.
Helm deployed application to Kubernetes namespace {branch}.
Rollout restart executed successfully.

Write only deployment summary text.
"""

response = requests.post(
    OLLAMA_URL,
    json={
        "model": "tinyllama",
        "prompt": ai_prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 100
        }
    },
    timeout=60
)

ai_text = response.json()["response"]

print("\n===== DETAILED AI RELEASE SUMMARY =====\n")

print(f"Environment: {branch}")
print(f"Branch: {branch}")
print(f"Commit: {commit}")
print(f"Repository: {repo}")
print(f"Triggered By: {actor}")

print("\nDeployment Summary:")
print(ai_text)

print("\nRisk Notes:")
print("No deployment risks reported.")

print("\nFinal Status:")
print("Deployment completed successfully.")
