from pydantic import BaseModel

from app.models.domain_models import AssessmentSession


class StartAssessmentRequest(BaseModel):
    target_role: str


class StartAssessmentResponse(BaseModel):
    session_id: AssessmentSession
    question: str


class SubmitAnswerRequest(BaseModel):
    session_id: str
    answer: str


class SubmitAnswerResponse(BaseModel):
    next_question: str