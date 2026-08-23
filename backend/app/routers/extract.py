from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class ExtractResponse(BaseModel):
    session_id: Optional[str] = None
    doc_type: str
    fields: dict
    confidence_flags: dict

@router.post("/", response_model=ExtractResponse)
async def extract_fields(
    file: UploadFile = File(...),
    doc_type: str = "aadhaar",
    session_id: Optional[str] = None
):
    """
    Upload a document image.
    Qwen3-VL reads it and returns extracted fields as JSON.
    doc_type: aadhaar | passbook | land_record
    """
    # Logic added in Step 5
    return {
        "session_id": session_id,
        "doc_type": doc_type,
        "fields": {},
        "confidence_flags": {}
    }