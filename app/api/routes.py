from fastapi import APIRouter, HTTPException
from app.schemas.request import QueryRequest
from app.schemas.response import QueryResponse
from app.core.llm import call_llm
import json
import traceback
router = APIRouter()

SYSTEM_PROMPT = """
You are an AI assistant for machine learning and LLM systems.


Always return valid JSON with:
- answer
- confidence (0-1)
- sources
"""

@router.post("/ask", response_model=QueryResponse)
async def ask_llm(query: QueryRequest):

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": query.question},
    ]

    try:
        raw = await call_llm(messages)
        data = json.loads(raw)
        return QueryResponse(**data)

    except Exception as e:
        print(f"LLM call failed: {e}")

        return QueryResponse(
            answer="Mock response: LLM quota exceeded but service is functional.",
            confidence=0.0,
            sources=["mock"]
        )