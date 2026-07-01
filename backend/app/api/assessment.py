from fastapi import APIRouter

from app.models.assessment_models import (
    StartAssessmentRequest,
    StartAssessmentResponse,
    SubmitAnswerRequest,
    SubmitAnswerResponse,
)

from app.services.assessment_service import AssessmentService
from app.services.evaluation_service import EvaluationService
from app.services.question_service import QuestionService
from app.services.session_service import SessionService
from app.store.session_store import SessionStore
from app.services.llm_service import LLMService

llm_service = LLMService()

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)

session_store = SessionStore()

session_service = SessionService(session_store)
question_service = QuestionService()
evaluation_service = EvaluationService()

assessment_service = AssessmentService(
    session_service=session_service,
    question_service=question_service,
    evaluation_service=evaluation_service,
)


@router.post(
    "/start",
    response_model=StartAssessmentResponse,
)
def start_assessment(request: StartAssessmentRequest):
    return assessment_service.start_assessment(request)


@router.post(
    "/answer",
    response_model=SubmitAnswerResponse,
)
def submit_answer(request: SubmitAnswerRequest):
    return assessment_service.submit_answer(request)

@router.get("/{session_id}")
def get_assessment_session(session_id: str):
    return assessment_service.get_assessment(session_id)


