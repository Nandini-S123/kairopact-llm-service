from groq import AsyncGroq
from app.core.config import settings
from .config import settings

client = AsyncGroq(api_key=settings.GROQ_API_KEY)

async def call_llm(messages):
    response = await client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content





