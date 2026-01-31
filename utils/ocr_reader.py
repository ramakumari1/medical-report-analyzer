def extract_text_from_image(image_path):
    """
    OCR is DISABLED on Streamlit Cloud.

    Reason:
    Streamlit Cloud does not support system-level binaries
    like the Tesseract OCR engine.

    This function intentionally avoids calling pytesseract
    to prevent runtime crashes.
    """

    return (
        "OCR is disabled in the cloud deployment.\n\n"
        "Reason: Streamlit Cloud does not support the Tesseract OCR engine.\n\n"
        "Please use the Text Input tab to analyze reports, "
        "or run this project locally to enable image-based OCR."
    )
