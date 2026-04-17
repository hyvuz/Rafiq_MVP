def validate_emoji_support(emoji_support: list[dict], allowed_emojis: list[str]) -> list[dict]:
    validated = []

    for item in emoji_support:
        if not isinstance(item, dict):
            continue

        step_text = str(item.get("step_text", "")).strip()
        emojis = item.get("emojis", [])

        if not isinstance(emojis, list):
            emojis = []

        clean_emojis = []
        for emoji in emojis:
            if emoji in allowed_emojis and emoji not in clean_emojis:
                clean_emojis.append(emoji)

        max_allowed = min(4, len(allowed_emojis))
        clean_emojis = clean_emojis[:max_allowed]

        # enforce at least 2 if possible from allowed_emojis
        if len(clean_emojis) < 2 and len(allowed_emojis) >= 2:
            for emoji in allowed_emojis:
                if emoji not in clean_emojis:
                    clean_emojis.append(emoji)
                if len(clean_emojis) >= 2:
                    break

        validated.append({
            "step_text": step_text,
            "emojis": clean_emojis
        })

    return validated