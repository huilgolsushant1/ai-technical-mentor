from google import genai

from app.config import GEMINI_API_KEY


class LLMService:

    def __init__(self):
        self._client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate(self, prompt: str) -> str:

        response = self._client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text