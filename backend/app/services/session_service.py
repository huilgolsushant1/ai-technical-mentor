import uuid

from app.store.session_store import SessionStore
from app.models.domain_models import (
    AssessmentSession,
    AssessmentInteraction
)

class SessionService:

    def __init__(
            self,
            session_store: SessionStore
    ):
        self._session_store = session_store

    # Method for creating a new assessment session
    def create_session(
            self,
            target_role: str
    ):
        session = AssessmentSession(
            session_id=str(uuid.uuid4()),
            target_role=target_role
        )

        self._session_store.save_session(session)

        return session

    # Method for adding a question to an existing assessment session
    def add_question(
            self,
            session: AssessmentSession,
            question: str
    ) -> None:

        interaction = AssessmentInteraction(
            question=question
        )

        session.interactions.append(
            interaction
        )

    # Method for retrieving the current interaction (question) in an assessment session
    def get_current_interaction(
            self,
            session: AssessmentSession
    ) -> AssessmentInteraction:

        return session.interactions[-1]

    # Method for submitting an answer to the current interaction (question) in an assessment session
    def submit_answer(
            self,
            session: AssessmentSession,
            answer: str
    ) -> None:

        interaction = self.get_current_interaction(
            session
        )

        interaction.answer = answer

    def get_session(self, session_id: str):
        return self._session_store.get_session(session_id)