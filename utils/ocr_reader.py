from PIL import Image
import pytesseract


def extract_text_from_image(image_path):
    """
    Extract text from image using Tesseract OCR.
    On Streamlit Cloud, Tesseract is NOT available,
    so this function gracefully falls back.
    """

    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text

    except pytesseract.TesseractNotFoundError:
        # 🔴 This ALWAYS happens on Streamlit Cloud
        return (
            "OCR is not available on this deployment environment.\n\n"
            "Please use the Text Input tab, or run this project locally "
            "to enable OCR-based image analysis."
        )

    except Exception as e:
        return f"OCR failed due to unexpected error: {str(e)}"
