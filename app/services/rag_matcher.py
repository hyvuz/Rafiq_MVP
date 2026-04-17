import json
from pathlib import Path

RAG_PATH = Path("data/Hackathon_RAG.json")

with open(RAG_PATH, "r", encoding="utf-8") as file:
    RAG_DATA = json.load(file)


def extract_rag_matches(text: str):
    matches = []

    for word, values in RAG_DATA.items():
        if word in text:
            replacement = values.get("مستوى 2") or values.get("مستوى 1")

            if replacement:
                matches.append({
                    "الكلمة": word,
                    "البديل": replacement
                })

    return matches