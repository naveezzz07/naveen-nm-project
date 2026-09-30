import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiDocumentGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set in environment variables.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def generate_document(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        prompt = (
            f"Generate a comprehensive legal document titled '{document_type}'\n\n"
            f"Involved parties: {parties}\n"
            f"Effective Date: {dates}\n\n"
            f"Terms and conditions: {terms}\n\n"
            "Ensure formal legal structure with multiple sections and legal clauses. "
            "Return ONLY the document text. Provide clearly separated bullet points and markdown headings where appropriate."
        )
        response = self.model.generate_content(prompt)
        return response.text
