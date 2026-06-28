from fastapi import HTTPException

from app.models.assessment_models import (
    StartAssessmentRequest,
    StartAssessmentResponse,
    SubmitAnswerRequest,
    SubmitAnswerResponse,
)

from app.services.evaluation_service import EvaluationService
from app.services.question_service import QuestionService
from app.services.session_service import SessionService


class AssessmentService:

    def __init__(
            self,
            session_service: SessionService,
            question_service: QuestionService,
            evaluation_service: EvaluationService,
    ):
        self._session_service = session_service
        self._question_service = question_service
        self._evaluation_service = evaluation_service

    def start_assessment(
            self,
            request: StartAssessmentRequest,
    ) -> StartAssessmentResponse:

        session = self._session_service.create_session(
            request.target_role
        )

        question = self._question_service.generate_first_question(
            request.target_role
        )

        self._session_service.add_question(
            session,
            question,
        )

        return StartAssessmentResponse(
            session_id=session,
            question=question,
        )

    def submit_answer(
            self,
            request: SubmitAnswerRequest,
    ) -> SubmitAnswerResponse:

        session = self._session_service.get_session(
            request.session_id
        )

        if not session:
            raise HTTPException(
                status_code=404,
                detail="Session not found",
            )

        self._session_service.submit_answer(
            session,
            request.answer,
        )

        # We'll replace this mock implementation with LLM evaluation later.
        evaluation = self._evaluation_service.evaluate_answer(
            session.interactions[-1].question,
            request.answer,
        )

        session.interactions[-1].interview_evaluation = evaluation

        next_question = (
            self._question_service.generate_next_question()
        )

        self._session_service.add_question(
            session,
            next_question,
        )

        return SubmitAnswerResponse(
            interview_evaluation=evaluation,
            next_question=next_question,
        )

    def get_assessment(
            self,
            session_id: str,
    ):
        session = self._session_service.get_session(
            session_id
        )

        if not session:
            raise HTTPException(
                status_code=404,
                detail="Session not found",
            )

        return session