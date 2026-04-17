import json
from pathlib import Path

EMOJI_RAG_PATH = Path("data/emoji_rag.json")

with open(EMOJI_RAG_PATH, "r", encoding="utf-8") as file:
    EMOJI_RAG = json.load(file)


def extract_emoji_candidates(original_text: str, simplified_text: str) -> list[str]:
    text_to_check = f"{original_text} {simplified_text}"
    found = []

    for term, data in EMOJI_RAG.items():
        text_hint = data.get("text_hint", "")
        matched = term in text_to_check or (text_hint and text_hint in text_to_check)

        if matched:
            for emoji in data.get("emoji_candidates", []):
                if emoji not in found:
                    found.append(emoji)

    return found[:10]