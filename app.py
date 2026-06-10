import streamlit as st
from pypdf import PdfReader

st.title("📄 Resumidor de PDF (sin IA)")

uploaded_file = st.file_uploader("Sube tu archivo PDF", type="pdf")

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text

def summarize_200_words(text):
    words = text.split()
    return " ".join(words[:200])

if uploaded_file is not None:
    text = extract_text(uploaded_file)

    if text.strip():
        summary = summarize_200_words(text)

        st.subheader("Resumen (máx 200 palabras):")
        st.success(summary)
    else:
        st.error("No se pudo leer el PDF")
        
