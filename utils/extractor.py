import pdfplumber       # For extracting text from PDFs
import easyocr          # For OCR (Optical Character Recognition) on images
import os               # For file path handling

# Initialize EasyOCR reader (for English language)
reader = easyocr.Reader(['en'], gpu=False)

# Extract text from a PDF file using pdfplumber
def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            # Extract text from each page
            text += page.extract_text() + "\n"
    return text.strip()

# Extract text from an image (JPG, PNG, etc.) using EasyOCR
def extract_text_from_image(file_path: str) -> str:
    results = reader.readtext(file_path, detail=0)
    return "\n".join(results)

# Dispatcher: Calls appropriate function based on file extension
def extract_text(file_path: str) -> str:
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext in [".jpg", ".jpeg", ".png"]:
        return extract_text_from_image(file_path)
    else:
        raise ValueError("Unsupported file type. Upload PDF or image only.")
