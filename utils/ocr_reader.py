# OCR is completely disabled for Streamlit Cloud
# This file intentionally contains NO pytesseract usage

def extract_text_from_image(image_path):
    return (
        "OCR is disabled in the cloud deployment.\n\n"
        "Reason: Streamlit Cloud does not support the Tesseract OCR engine.\n\n"
        "Please use the Text Input tab or run this project locally to enable OCR."
    )
