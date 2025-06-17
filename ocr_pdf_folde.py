import os
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# --- Configuration ---
INPUT_FOLDER = "pdfs"
OUTPUT_FOLDER = "ocr_output"
DPI = 300  # Higher DPI = better OCR results

# If using Windows and Tesseract is not in your PATH, uncomment and update this:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Process each PDF file in the folder
for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(INPUT_FOLDER, filename)
        print(f"Processing {filename}...")

        # Convert PDF pages to images
        try:
            images = convert_from_path(pdf_path, dpi=DPI)
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")
            continue

        # Extract text from each page image
        full_text = ""
        for i, image in enumerate(images):
            print(f"  OCR on page {i+1}...")
            text = pytesseract.image_to_string(image, lang='eng')
            full_text += f"\n\n--- Page {i+1} ---\n\n{text}"

        # Save text to .txt file
        output_file = os.path.join(OUTPUT_FOLDER, f"{os.path.splitext(filename)[0]}.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(full_text)

        print(f"Saved OCR text to {output_file}")

print("✅ Done.")

'''
project/
├── ocr_pdf_folder.py
├── pdfs/
│   ├── scanned_doc1.pdf
│   ├── scanned_doc2.pdf
├── ocr_output/

'''
