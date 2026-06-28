from pydantic import BaseModel

#The mentor's assessment of that exchange.
class InterviewEvaluation(BaseModel):
    overall_score: int
    strengths: list[str]
    weaknesses: list[str]
    ideal_answer: str
    overall_feedback: str