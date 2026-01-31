import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from utils.text_cleaner import clean_medical_text
from utils.extractor import extract_medical_values
from rules.risk_rules import detect_health_risks
from utils.report_classifier import detect_report_type
from utils.ocr_reader import extract_text_from_image


def process_medical_report(text):
    cleaned_text = clean_medical_text(text)
    values = extract_medical_values(cleaned_text)
    risks = detect_health_risks(values)
    report_type = detect_report_type(cleaned_text)
    return cleaned_text, values, risks, report_type


def process_medical_image(image_path):
    # OCR is disabled on cloud, this returns a safe message
    raw_text = extract_text_from_image(image_path)
    cleaned_text = clean_medical_text(raw_text)
    values = extract_medical_values(cleaned_text)
    risks = detect_health_risks(values)
    report_type = "Image OCR (Disabled on Cloud)"
    return cleaned_text, values, risks, report_type
