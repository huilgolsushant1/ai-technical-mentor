from pydantic import BaseModel
from typing import List

class AssessmentInteraction(BaseModel):
    question: str
    answer: str | None = None
    score: float | None = None
    feedback: str | None = None

class AssessmentSession(BaseModel):
    session_id: str
    target_role: str
    interactions: list[AssessmentInteraction] = []