import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai

st.title("📄 Resumidor Inteligente de PDF (~200 palabras)")

# API KEY
api_key = st.text_input("Ingresa tu API Key de Gemini", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

uploaded_file = st.file_uploader("Sube tu PDF", type="pdf")


# Extraer texto del PDF
def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


# IA resumen
def ai_summary(text):
    prompt = f"""
    Resume el siguiente texto de forma clara, concreta y bien estructurada.
    El resumen debe tener máximo 200 palabras.

    Texto:
    {text}
    """
    response = model.generate_content(prompt)
    return response.text


if uploaded_file and api_key:
    text = extract_text(uploaded_file)

    if text.strip():
        summary = ai_summary(text)

        st.subheader("Resumen (~200 palabras):")
        st.success(summary)
    else:
        st.error("No se pudo leer el PDF")
        
