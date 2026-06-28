from app.models.interview_evaluation import InterviewEvaluation


class EvaluationService:

    def evaluate_answer(self, question: str, answer: str) -> InterviewEvaluation:
        """
        Mock implementation.
        Later this will call an LLM to evaluate the user's answer.
        """

        return InterviewEvaluation(
            overall_score=7,
            strengths=[
                "Good understanding of the core concept."
            ],
            weaknesses=[
                "Could include more implementation details."
            ],
            ideal_answer=(
                "A complete answer would explain the concept in detail "
                "with practical examples and implementation considerations."
            ),
            overall_feedback=(
                "You have a solid foundation but your explanation lacks depth. "
                "Try to explain not only what the concept is, but also how it works "
                "and why it is used in real-world applications."
            )
        )