
import streamlit as st
import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image
import tempfile
import os

st.set_page_config(page_title="PDF OCR Extractor", layout="centered")
st.title("📄 OCR PDF Text Extractor")

st.write("Upload a scanned PDF file and extract its text using Tesseract OCR.")

# Upload PDF
uploaded_file = st.file_uploader("Choose a scanned PDF file", type=["pdf"])

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
    with st.spinner("Converting PDF pages to images..."):
        try:
            images = convert_from_bytes(uploaded_file.read(), dpi=300)
        except Exception as e:
            st.error(f"Error converting PDF: {e}")
            st.stop()

    extracted_text = ""
    for i, image in enumerate(images):
        st.write(f"🔍 OCR on page {i+1}")
        text = pytesseract.image_to_string(image, lang='eng')
        extracted_text += f"\n\n--- Page {i+1} ---\n\n{text}"

    st.text_area("📝 Extracted Text", extracted_text, height=300)

    # Save to downloadable text file
    if extracted_text:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as tmp_file:
            tmp_file.write(extracted_text)
            tmp_file_path = tmp_file.name

        with open(tmp_file_path, "rb") as f:
            st.download_button(
                label="💾 Download Text File",
                data=f,
                file_name=f"{os.path.splitext(uploaded_file.name)[0]}.txt",
                mime="text/plain"
            )

        os.remove(tmp_file_path)
