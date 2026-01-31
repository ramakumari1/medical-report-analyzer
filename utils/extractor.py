import os
import sys

# ---------------- PATH FIX FOR STREAMLIT CLOUD ----------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# ---------------- IMPORTS ----------------
from utils.text_cleaner import clean_medical_text
from utils.extractor import extract_medical_values
from rules.risk_rules import detect_health_risks
from utils.report_classifier import detect_report_type
from utils.summary_generator import generate_clinical_summary
from utils.ocr_reader import extract_text_from_image


# =================================================
# PROCESS TEXT REPORT
# =================================================
def process_medical_report(text: str):
    """
    Takes raw medical report text
    Returns: cleaned_text, extracted_values, risks, report_type
    """

    cleaned_text = clean_medical_text(text)
    values = extract_medical_values(cleaned_text)
    risks = detect_health_risks(values)
    report_type = detect_report_type(cleaned_text)

    return cleaned_text, values, risks, report_type


# =================================================
# PROCESS IMAGE REPORT (OCR)
# =================================================
def process_medical_image(image_path: str):
    """
    Takes path to medical report image
    Performs OCR + NLP
    Returns: cleaned_text, extracted_values, risks, report_type
    """

    raw_text = extract_text_from_image(image_path)
    cleaned_text = clean_medical_text(raw_text)
    values = extract_medical_values(cleaned_text)
    risks = detect_health_risks(values)
    report_type = detect_report_type(cleaned_text)

    return cleaned_text, values, risks, report_type
