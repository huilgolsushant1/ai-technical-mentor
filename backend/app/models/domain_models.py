from pydantic import BaseModel
from typing import List

from app.models.interview_evaluation import InterviewEvaluation


#A single exchange between the mentor and the learner.
class AssessmentInteraction(BaseModel):
    question: str
    answer: str | None = None
    interview_evaluation: InterviewEvaluation | None = None

#An entire mock interview.
class AssessmentSession(BaseModel):
    session_id: str
    target_role: str
    interactions: list[AssessmentInteraction] = []

class SubmitAnswerRequest(BaseModel):
    session_id: str
    answer: str


class SubmitAnswerResponse(BaseModel):
    next_question: str