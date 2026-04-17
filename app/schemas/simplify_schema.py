from pydantic import BaseModel, Field
from typing import List


class SimplifyRequest(BaseModel):
    text: str = Field(..., min_length=1)


class SimplifiedWord(BaseModel):
    الكلمة: str
    البديل: str


class SimplifyData(BaseModel):
    نوع_النص: str
    الفعل_المطلوب: str
    الكلمات_التي_تم_تبسيطها: List[SimplifiedWord]
    النص_المبسط: str
    خطوات_قصيرة: List[str]
    درجة_الدقة: int
    سبب_الدرجة: str