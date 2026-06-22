from app.models.domain_models import AssessmentSession


class SessionStore:

    def __init__(self):
        self.sessions: dict[str, AssessmentSession] = {}

    def save_session(
            self,
            session: AssessmentSession
    ) -> None:

        self.sessions[session.session_id] = session

    def get_session(
            self,
            session_id: str
    ) -> AssessmentSession | None:

        return self.sessions.get(session_id)