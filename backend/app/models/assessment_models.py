from pydantic import BaseModel

from app.models.domain_models import AssessmentSession
from app.models.interview_evaluation import InterviewEvaluation


class StartAssessmentRequest(BaseModel):
    target_role: str


class StartAssessmentResponse(BaseModel):
    session_id: AssessmentSession
    question: str


class SubmitAnswerRequest(BaseModel):
    session_id: str
    answer: str


class SubmitAnswerResponse(BaseModel):
    interview_evaluation: InterviewEvaluation
    next_question: str