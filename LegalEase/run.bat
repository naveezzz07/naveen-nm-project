@echo off
echo Starting LegalEase Backend and Frontend...

:: Start the FastAPI Backend
start cmd /k "uvicorn legalEaseAPI.main:app --reload"

:: Wait for a couple of seconds to ensure the backend starts
timeout /t 3 /nobreak >nul

:: Start the Streamlit Frontend
start cmd /k "streamlit run frontend/app.py"

echo Both services have been started.
