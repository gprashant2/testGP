import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

def summarize(text):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "tinyllama",
            "prompt": f"""
You are a DevSecOps engineer.

Summarize this security scan result in 3 bullet points:
- Risk Level
- Main Issue
- Suggested Fix

Scan Result:
{text}
""",
            "stream": False
        },
        timeout=120
    )

    return response.json()["response"]


def main():
    try:
        with open("trivy.txt") as f:
            scan_data = f.read()

        summary = summarize(scan_data)

        print("\n===== LOCAL AI SECURITY SUMMARY =====\n")
        print(summary)

    except Exception as e:
        print("AI summary failed:", e)


if __name__ == "__main__":
    main()
