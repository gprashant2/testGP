import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

def summarize(text):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": f"""
You are a senior DevSecOps security expert.

Analyze scan result and produce structured table.

Output STRICT:

| Risk Level | Component | Issue | Fix |
|------------|-----------|-------|-----|
| <value> | <value> | <value> | <value> |

Rules:
- Use only scan data
- No extra explanation

Scan Data:
{text}
""",
            "stream": False,
            "options": {
                "temperature": 0.1
            }
        },
        timeout=300
    )

    return response.json()["response"]


with open("trivy.txt") as f:
    scan_data = f.read()

print("\n===== LLAMA3 SECURITY SUMMARY =====\n")
print(summarize(scan_data))

