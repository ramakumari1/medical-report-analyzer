
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from utils.text_cleaner import clean_medical_text
from utils.extractor import extract_values
from rules.risk_rules import detect_risks
from utils.summary_generator import generate_clinical_summary





def process_medical_report(text):
    cleaned_text = clean_medical_text(text)
    report_type = detect_report_type(cleaned_text)

    extracted_values = extract_medical_values(cleaned_text)
    risks = detect_health_risks(extracted_values)

    return cleaned_text, extracted_values, risks, report_type


def process_medical_image(image_path):
    raw_text = extract_text_from_image(image_path)
    return process_medical_report(raw_text)
