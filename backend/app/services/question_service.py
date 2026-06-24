class QuestionService:

    def generate_first_question(
            self,
            target_role: str
    ) -> str:

        return (
            f"What are the responsibilities "
            f"of an {target_role}?"
        )

    def generate_next_question(self) -> str:

        return "What are embeddings?"