import os
from PyPDF2 import PdfReader
from docx import Document

def extract_text(file_path):
    text = ""

    extension = os.path.splitext(file_path)[1].lower()

    # PDF
    if extension == ".pdf":
        try:
            reader = PdfReader(file_path)

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        except Exception as e:
            print("PDF Error:", e)

    # DOCX
    elif extension == ".docx":
        try:
            doc = Document(file_path)

            for para in doc.paragraphs:
                text += para.text + "\n"

        except Exception as e:
            print("DOCX Error:", e)

    return text