========================================================================
LegalEase: AI-Powered Legal Document Generator

PROJECT OVERVIEW

LegalEase leverages state-of-the-art Generative AI to simplify the creation
of legal documents by providing customizable, accurate, and editable
templates for a wide range of use cases. Users can generate employment
contracts, lease agreements, NDAs, and more—all tailored to their specific
inputs like involved parties, effective dates, and key terms.

Built with FastAPI and integrated with a powerful AI core, LegalEase ensures
users receive professional-grade legal documents that maintain formatting
standards, include custom branding (such as logos and footers), and support
features like editable previews and automatic term formatting. With secure
handling of sensitive user data and seamless document export options
(.PDF, .DOCX, .TXT), the platform bridges the gap between accessibility
and legal professionalism.

LegalEase empowers entrepreneurs, professionals, and individuals to generate
reliable legal content confidently—without needing a legal background.

KEY FEATURES

AI-Driven Generation: Powered by Google's Gemini 1.5 Pro model for
accurate legal structure and terms.

Interactive Frontend: User-friendly interface built with Streamlit.

Fast API Backend: High-performance RESTful API powering document logic.

Dynamic Preview & Editing: Live HTML text preview with inline editing
capabilities before finalized export.

Multi-Format Export: Seamlessly download generated documents in
.TXT, .DOCX, or .PDF formats.

Custom Branding: Integrates corporate logos and custom footers into
formatted documents (.DOCX and .PDF).

PROJECT ARCHITECTURE

+------------------------+
|   User Interface       |  (Streamlit / app.py)
|   - Inputs & Editing   |
|   - Multi-format Export|
+-----------+------------+
|
v
+------------------------+
|   FastAPI Backend      |  (main.py / routes.py)
|   - Request Handling   |
|   - Schema Validation  |
+-----------+------------+
|
v
+------------------------+
|   AI Document Core     |  (ai_core/gemini_generator.py)
|   - Google Gemini API  |
+-----------+------------+
|
v
+------------------------+
| Formatted Downloads    |  (.TXT, .DOCX, .PDF)
+------------------------+

PROJECT STRUCTURE

LEGALEASE/
│
├── ai_core/
│   ├── init.py
│   ├── generator.py
│   └── gemini_generator.py     # Gemini 1.5 Pro API integration logic
│
├── docs/                       # Project documentation
│
├── frontend/
│   ├── init.py
│   └── app.py                  # Streamlit UI interface
│
├── Image/
│   ├── Logo.png                # Main logo
│   └── inverseLogo.png         # Dark-themed logo
│
├── legalEaseAPI/
│   ├── init.py
│   ├── main.py                 # FastAPI application initialization
│   └── routes.py               # API route definitions
│
├── .env                        # Environment variables (API Keys)
├── config.py                   # Configuration settings
├── requirements.txt            # Project dependencies
├── run.bat                     # Windows startup script
└── run.sh                      # Shell startup script

PREREQUISITES & INSTALLATION

Python 3.10+ installed on your system.

Obtain a Google Gemini API Key from Google AI Studio.

Setup Steps:

Clone or extract the repository and navigate to the project root:
cd LegalEase

Create and activate a virtual environment:
python -m venv venv

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install required dependencies:
pip install -r requirements.txt

Configure environment variables:
Create a .env file in the root directory and add your API Key:
GEMINI_API_KEY=your_google_gemini_api_key_here

HOW TO RUN THE APPLICATION

Step 1: Start the FastAPI Backend
uvicorn legalEaseAPI.main:app --reload
(The backend running on http://127.0.0.1:8000)

Step 2: Start the Streamlit Frontend
streamlit run frontend/app.py
(Access the UI in your browser at http://localhost:8501)

USAGE INSTRUCTIONS

Enter the Document Type (e.g., NDA, Employment Contract, Lease Agreement).

Input the Parties Involved (e.g., John Doe (Employer), Jane Smith (Employee)).

Enter Terms & Conditions (separate each bullet point/clause using semicolons ';').

Specify the Effective Date.

Click "Generate Document".

Preview the output in the dark-themed view or click "Click to Edit Document" to make custom adjustments.

Click your preferred download button (.TXT, .DOCX, or .PDF).

========================================================================
Made by Naveen
