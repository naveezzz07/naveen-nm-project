import streamlit as st
import requests
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ai_core.generator import sanitize_text, format_docx, format_pdf, format_html_preview

st.set_page_config(page_title="LegalEase", layout="centered")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("Image/Logo.png", use_container_width=True)
    except Exception:
        pass

st.markdown("<h2 style='text-align: center;'>LegalEase AI Legal Document Generator</h2>", unsafe_allow_html=True)

document_type = st.text_input("Document Type", placeholder="e.g., Freelance Work Contract")
parties = st.text_area("Parties Involved", placeholder="e.g., Jane Doe (Service Provider), TechNova Inc. (Client)")
terms = st.text_area("Terms & Conditions (Use semicolons for bullet points)", placeholder="e.g., Payment within 30 days; Confidentiality must be maintained")
dates = st.text_input("Effective Date", placeholder="e.g., April 15, 2025")

if st.button("Generate Document"):
    if not document_type or not parties or not terms or not dates:
        st.error("Please fill in all fields.")
    else:
        with st.spinner("Generating legal document..."):
            try:
                response = requests.post("http://localhost:8000/generate", json={
                    "document_type": document_type,
                    "parties": parties,
                    "terms": terms,
                    "dates": dates
                })
                
                if response.status_code == 200:
                    generated_text = sanitize_text(response.json().get("document", ""))
                    st.success("Document Generated Successfully!")
                    st.session_state.generated_text = generated_text
                    st.session_state.document_type = document_type
                    st.session_state.show_edit = False
                else:
                    st.error(f"Error from API: {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("Failed to connect to backend. Make sure FastAPI is running on port 8000 (run `uvicorn legalEaseAPI.main:app --reload`).")

if "generated_text" in st.session_state:
    styled_html = format_html_preview(st.session_state.generated_text)
    st.markdown(f"<div>{styled_html}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    if st.button("Click to Edit Document"):
        st.session_state.show_edit = not st.session_state.show_edit
        
    if st.session_state.get("show_edit"):
        edited_text = st.text_area("Edit Document Below:", st.session_state.generated_text, height=300)
        st.session_state.generated_text = edited_text
        
    st.markdown("---")
    
    txt_data = st.session_state.generated_text
    docx_data = format_docx(st.session_state.generated_text, st.session_state.document_type)
    pdf_data = format_pdf(st.session_state.generated_text, st.session_state.document_type)
    
    clean_name = st.session_state.document_type.replace(' ', '_').lower()
    
    st.download_button("📄 Download as .TXT", data=txt_data, file_name=f"{clean_name}.txt")
    st.download_button("📝 Download as .DOCX", data=docx_data, file_name=f"{clean_name}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    st.download_button("📕 Download as .PDF", data=pdf_data, file_name=f"{clean_name}.pdf", mime="application/pdf")
