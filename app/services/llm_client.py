import os
import httpx
from dotenv import load_dotenv

load_dotenv()

ELM_API_URL = os.getenv("ELM_API_URL")
ELM_API_KEY = os.getenv("ELM_API_KEY")
ELM_MODEL = os.getenv("ELM_MODEL")

print("URL:", ELM_API_URL)
print("MODEL:", ELM_MODEL)
print("KEY EXISTS:", ELM_API_KEY is not None)


async def call_elm_llm(prompt: str):
    headers = {
        "Authorization": f"Bearer {ELM_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": ELM_MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2
    }

    print("HEADERS:", headers)
    print("PAYLOAD:", payload)

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            ELM_API_URL,
            headers=headers,
            json=payload
        )

    print("STATUS CODE:", response.status_code)
    print("RAW RESPONSE:", response.text)

    response.raise_for_status()

    result = response.json()
    return result["choices"][0]["message"]["content"]