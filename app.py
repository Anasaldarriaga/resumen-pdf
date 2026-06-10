import streamlit as st
from pypdf import PdfReader

# Título
st.title("📄 Resumidor de PDF (máx 200 palabras)")

# Subir archivo
uploaded_file = st.file_uploader("Sube tu archivo PDF", type="pdf")

# Extraer texto del PDF
def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content

    return text

# Resumen máximo 200 palabras
def summarize_200_words(text):
    words = text.split()
    limited_words = words[:200]
    return " ".join(limited_words)

# Lógica principal
if uploaded_file is not None:
    text = extract_text(uploaded_file)

    if text.strip():
        summary = summarize_200_words(text)

        st.subheader("Resumen (máx 200 palabras):")
        st.success(summary)
    else:
        st.error("No se pudo leer el PDF")
