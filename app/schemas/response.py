from pydantic import BaseModel
from typing import List

class QueryResponse(BaseModel):
    answer: str
    confidence: float
    sources: List[str]