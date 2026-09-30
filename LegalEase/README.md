# LegalEase - AI Legal Document Generator

LegalEase leverages state-of-the-art Generative AI (Google Gemini 1.5 Pro) to simplify the creation of legal documents.

## Pre-requisites
- Python 3.10+
- An API key for Google Gemini

## Setup Instructions

1. **Extract this zip file** to a folder of your choice.
2. **Install dependencies:**
   Open a terminal in the folder and run:
   `pip install -r requirements.txt`
3. **Configure your API Key:**
   Open the `.env` file and replace `YOUR_GEMINI_API_KEY_HERE` with your actual Google Gemini API key.
4. **Run the Application:**
   - **Windows:** Double-click `run.bat`.
   - **Mac/Linux:** Run `bash run.sh`.
   - **Manual Start (Any OS):**
     Open two terminal windows:
     *Terminal 1 (Backend):* `uvicorn legalEaseAPI.main:app --reload`
     *Terminal 2 (Frontend):* `streamlit run frontend/app.py`

5. **Usage:**
   Navigate to the Local URL provided by Streamlit (usually `http://localhost:8501`), fill in the legal document details, and hit Generate.
