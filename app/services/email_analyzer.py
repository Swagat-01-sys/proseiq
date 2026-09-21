import os

from google import genai

from ..schemas import EmailAnalysisResponse
from ..prompts.email_prompt import SYSTEM_PROMPT


class EmailAnalyzer:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )

        self.client = genai.Client(api_key=api_key)

    def analyze(
        self,
        email_text: str
    ) -> EmailAnalysisResponse:

        prompt = f"""
        {SYSTEM_PROMPT}

        EMAIL TO ANALYZE:
        -------------------------
        {email_text}
        -------------------------
        """

        response = self.client.interactions.create(
            model="gemini-3.8-flash",
            input=prompt,
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": EmailAnalysisResponse.model_json_schema()
            }
        )

        return EmailAnalysisResponse.model_validate_json(
            response.output_text
        )