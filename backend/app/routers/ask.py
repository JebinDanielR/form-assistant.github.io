from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class AskRequest(BaseModel):
    question: str
    session_id: Optional[str] = None
    language: str = "english"

class AskResponse(BaseModel):
    answer: str
    sources: list[str] = []

@router.post("/", response_model=AskResponse)
async def ask_question(request: AskRequest):
    """
    RAG-based Q&A. Searches Qdrant for relevant scheme
    chunks, passes them to LLM, returns plain-language answer.
    """
    # Logic added in Step 6
    return {
        "answer": "RAG logic coming in Step 6.",
        "sources": []
    }