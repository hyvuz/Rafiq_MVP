import json
import re
from fastapi import APIRouter
from app.schemas.simplify_schema import SimplifyRequest
from app.services.rag_matcher import extract_rag_matches
from app.services.prompt_builder import build_prompt
from app.services.llm_client import call_elm_llm
from app.services.emoji_matcher import extract_emoji_candidates
from app.services.emoji_prompt_builder import build_emoji_prompt
from app.services.emoji_validator import validate_emoji_support

router = APIRouter(prefix="/api", tags=["Simplify"])


def extract_json_block(text: str):
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON found in LLM response")

    return json.loads(match.group())


@router.post("/simplify")
async def simplify(request: SimplifyRequest):
    try:
        text = request.text.strip()

        if not text:
            return {
                "success": False,
                "error": "Empty text is not allowed."
            }

        rag_matches = extract_rag_matches(text)
        prompt = build_prompt(text, rag_matches)

        raw_response = await call_elm_llm(prompt)
        parsed_response = extract_json_block(raw_response)

        simplified_text = parsed_response.get("النص_المبسط", "")
        steps = parsed_response.get("خطوات_قصيرة", [])

        if not isinstance(steps, list):
            steps = []

        emoji_candidates = extract_emoji_candidates(text, simplified_text)
        validated_emoji_support = []

        if emoji_candidates:
            try:
                emoji_prompt = build_emoji_prompt(simplified_text, steps, emoji_candidates)
                raw_emoji_response = await call_elm_llm(emoji_prompt)
                parsed_emoji_response = extract_json_block(raw_emoji_response)
                emoji_support = parsed_emoji_response.get("emoji_support", [])
                validated_emoji_support = validate_emoji_support(emoji_support, emoji_candidates)
            except Exception:
                validated_emoji_support = []

        parsed_response["دعم_بصري"] = validated_emoji_support

        return {
            "success": True,
            "data": parsed_response
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }