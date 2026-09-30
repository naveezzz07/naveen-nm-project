#!/bin/bash
echo "Starting LegalEase Backend and Frontend..."

uvicorn legalEaseAPI.main:app --reload &
BACKEND_PID=$!
sleep 3
streamlit run frontend/app.py
trap "kill $BACKEND_PID" EXIT
