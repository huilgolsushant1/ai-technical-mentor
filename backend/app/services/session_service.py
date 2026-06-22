import uuid

from app.models.domain_models import AssessmentSession
from app.services.session_store import SessionStore


class SessionService:

    def __init__(
            self,
            session_store: SessionStore
    ):
        self.session_store = session_store

    def create_session(
            self,
            target_role: str
    ):
        session = AssessmentSession(
            session_id=str(uuid.uuid4()),
            target_role=target_role
        )

        self.session_store.save_session(session)

        return session