# 🧠 OCR PDF Text Extractor

A Python utility that scans a folder of **scanned PDF documents (image-based)** and converts each page into **machine-readable text** using Tesseract OCR.

Perfect for turning image-only PDFs into searchable `.txt` files for further processing with LLMs or text analysis tools.

---

## 📂 Features

- 📄 Converts each page of a scanned PDF into an image
- 🧠 Uses Tesseract OCR to extract text from those images
- 📁 Saves output text to `.txt` files in a separate output folder
- 🛠️ Easy to configure and extend

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/ocr-pdf-text-extractor.git
cd ocr-pdf-text-extractor
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

**Also install Tesseract OCR engine:**

- **Windows:** [Tesseract Windows Installer](https://github.com/tesseract-ocr/tesseract)
- **macOS:** `brew install tesseract`
- **Linux:** `sudo apt install tesseract-ocr`

If Tesseract is not in your PATH (especially on Windows), set it manually inside the script:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## 📜 Usage

1. Place your scanned PDF files inside the `pdfs/` directory.
2. Run the script:

```bash
python ocr_pdf_folder.py
```

3. Extracted `.txt` files will be saved to `ocr_output/`, one per PDF.

---

## 🗂️ Folder Structure

```
ocr-pdf-text-extractor/
├── ocr_pdf_folder.py         # Main script
├── pdfs/                     # Input folder for scanned PDFs
├── ocr_output/               # Output folder for extracted .txt files
└── requirements.txt          # Python dependencies
```

---

## 🧪 Example

A scanned file `invoice.pdf` will generate:

```
ocr_output/invoice.txt
```

Each page will be marked like:

```
--- Page 1 ---

[Text here]

--- Page 2 ---

[Text here]
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤖 Future Enhancements

- Export to Markdown or JSON
- GUI version (Tkinter or Streamlit)
- Language selection for OCR
- Parallel processing for speed

---

## 💡 Built With

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [pdf2image](https://github.com/Belval/pdf2image)
- [Pillow (PIL)](https://pillow.readthedocs.io/)

---

## 🙌 Contribute

Feel free to fork this repo and submit a pull request! Suggestions and bug reports are welcome via [Issues](https://github.com/yourusername/ocr-pdf-text-extractor/issues).

