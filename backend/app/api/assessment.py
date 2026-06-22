from fastapi import APIRouter

from app.models.assessment_models import (
    StartAssessmentRequest,
    StartAssessmentResponse
)

from app.services.question_service import QuestionService
from app.services.session_service import SessionService
from app.services.session_store import SessionStore

session_store = SessionStore()

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"]
)

question_service = QuestionService()
session_service = SessionService(
    session_store
)

@router.post(
    "/start",
    response_model=StartAssessmentResponse
)
def start_assessment(
        request: StartAssessmentRequest
):
    session = session_service.create_session(
        request.target_role)

    question = question_service.generate_first_question(
        request.target_role
    )

    return StartAssessmentResponse(
        session_id=session,
        question=question
    )

@router.get("/{session_id}")
def get_assessment_session(
        session_id: str
):
    session = session_store.get_session(
        session_id
    )

    return session