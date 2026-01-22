from fastapi import APIRouter
from pydantic import BaseModel

from app.core.nlp import compute_match

router = APIRouter(prefix="/match", tags=["matching"])


class MatchRequest(BaseModel):
    resume_text: str
    job_description: str


class MatchResponse(BaseModel):
    match_score: float
    missing_keywords: list[str]


@router.post("/", response_model=MatchResponse)
def match_resume(data: MatchRequest):
    score, missing = compute_match(
        data.resume_text,
        data.job_description
    )
    return {
        "match_score": score,
        "missing_keywords": missing
    }
