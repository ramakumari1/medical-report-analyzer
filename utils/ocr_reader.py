import os
import pytesseract
from PIL import Image


def extract_text_from_image(image_path):
    """
    OCR text extraction.
    Works locally where Tesseract is installed.
    Gracefully disables OCR on Streamlit Cloud.
    """

    # Streamlit Cloud environment check
    if os.environ.get("STREAMLIT_SERVER_RUNNING"):
        return (
            "OCR is disabled on Streamlit Cloud.\n\n"
            "Please use the Text Input tab or run this project locally "
            "to enable OCR-based image analysis."
        )

    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text

    except pytesseract.TesseractNotFoundError:
        return (
            "Tesseract OCR engine not found.\n\n"
            "OCR works only on local machines where Tesseract is installed."
        )
