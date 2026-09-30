# LegalEase – AI-Powered Legal Document Generator

LegalEase is an AI-powered legal document generation platform designed to simplify the creation of professional legal documents. It uses Generative AI to create customizable and editable documents based on user inputs such as document type, parties involved, terms, and effective dates. The platform supports documents such as contracts, NDAs, lease agreements, and employment-related documents.

## Features

* 🤖 AI-powered legal document generation
* 📄 Generate contracts, NDAs, agreements, lease agreements, and more
* ✏️ Edit generated documents before downloading
* 👀 Preview generated documents
* 📥 Download documents as `.TXT`, `.DOCX`, or `.PDF`
* 🏢 Support for branding such as logos and formatted documents
* 📋 Automatic formatting of terms and clauses
* 🔐 Secure handling of sensitive user information
* 🖥️ User-friendly Streamlit interface

## Technologies Used

* Python
* FastAPI
* Streamlit
* Google Gemini API
* python-docx
* FPDF
* Pillow
* Requests
* python-dotenv

## How It Works

1. Enter the type of legal document you want to create.
2. Provide the parties involved, terms and conditions, and effective date.
3. LegalEase sends the information to the AI model.
4. The AI generates a structured legal document.
5. Preview and edit the generated content.
6. Download the final document in TXT, DOCX, or PDF format.

## Project Architecture

**Frontend:** Streamlit
**Backend:** FastAPI
**AI Integration:** Google Gemini
**Document Generation:** Python libraries for DOCX, PDF, and TXT formatting.

## Installation

```bash
pip install fastapi uvicorn streamlit python-docx fpdf Pillow requests google-generativeai python-dotenv
```

Create a `.env` file and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## Running the Project

Start the FastAPI backend:

```bash
uvicorn main:app --reload
```

Then start the Streamlit frontend:

```bash
streamlit run app.py
```

Open the Streamlit URL shown in the terminal and start generating legal documents.

## Output Formats

LegalEase allows users to export generated documents in:

* `.txt` – Plain text
* `.docx` – Formatted Microsoft Word document
* `.pdf` – Branded PDF document with formatting, logo, and footer.

## Future Enhancements

Future improvements can include deeper contract analysis, integration with legal databases, personalized recommendations, and expanded multilingual capabilities.

## Disclaimer

LegalEase is an AI-powered document generation tool intended to assist users in creating and understanding legal documents. Generated content should be reviewed carefully and, when appropriate, verified by a qualified legal professional.

---

### Made by Naveen
