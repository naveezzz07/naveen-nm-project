LegalEase: AI-Powered Legal Document Generator
LegalEase bridges the gap between accessibility and legal professionalism by allowing users to draft, preview, edit, and export customized legal documents without requiring formal legal training.   
PDF

Features
AI-Powered Legal Drafting: Dynamically generates contracts, NDAs, and agreements using Google Gemini models.   
PDF

Modular Full-Stack Architecture: Features an asynchronous FastAPI REST API backend and a lightweight Streamlit interface.   
PDF

Interactive Document Preview: Displays drafted contracts inside an HTML preview container.   
PDF

Inline Modification: Allows direct editing of the AI-generated text prior to exporting.   
PDF

Multi-Format Exporting: Converts text into .txt, styled .docx files, and .pdf documents with automated branding.   
PDF

System Architecture & Tech Stack
Frontend: Streamlit   
PDF

Backend: FastAPI, Uvicorn   
PDF

AI Engine: Google Generative AI (Gemini)   
PDF

Document Formatting: python-docx, fpdf, Pillow

   
PDF

Configuration: python-dotenv, pydantic

   
PDF

Project Structure
Plaintext
LEGALEASE/
├── ai_core/
│   ├── gemini_generator.py    # Gemini API prompt handling and generation logic
│   └── generator.py           # DOCX, PDF, and HTML formatting utilities
├── frontend/
│   └── app.py                 # Streamlit UI, form controls, and download handlers
├── Image/
│   ├── Logo.png               # Document and header branding logo
│   └── inverseLogo.png        # Inverted logo asset
├── legalEaseAPI/
│   ├── main.py                # FastAPI app initialization and root endpoints
│   └── routes.py              # API route definitions and request validation
├── .env                       # Environment variables (API keys)
├── requirements.txt           # Project dependencies
├── run.bat                    # Windows startup script
└── run.sh                     # Unix/macOS startup script
   
PDF

Installation & Setup
Clone or Extract the Project:

Bash
cd LegalEase
Create and Activate a Virtual Environment:

Windows:

PowerShell
python -m venv venv
.\venv\Scripts\Activate
macOS / Linux:

Bash
python3 -m venv venv
source venv/bin/activate
Install Dependencies:

Bash
pip install -r requirements.txt
   
PDF

Configure the Environment:
Create a .env file in the root directory and add your API key:   
PDF

Code snippet
GEMINI_API_KEY=your_google_gemini_api_key_here
Running the Application
Option 1: Automated Script

Windows: Double-click run.bat

macOS / Linux: Run bash run.sh

Option 2: Manual Startup

Start the FastAPI backend:   
PDF

Bash
uvicorn legalEaseAPI.main:app --reload
In a separate terminal, launch the Streamlit frontend:   
PDF

Bash
streamlit run frontend/app.py
Access the web interface at http://localhost:8501.   
PDF

Made by Naveen