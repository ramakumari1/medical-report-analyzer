from utils.text_cleaner import clean_medical_text
from utils.extractor import extract_values
from utils.report_classifier import classify_report
from rules.risk_rules import evaluate_risks


def process_medical_report(text):
    cleaned = clean_medical_text(text)
    values = extract_values(cleaned)
    risks = evaluate_risks(values)
    report_type = classify_report(cleaned)

    return cleaned, values, risks, report_type


def process_medical_image(image_path):
    # OCR disabled on cloud
    cleaned = "Image OCR disabled on cloud deployment."
    values = {}
    risks = []
    report_type = "Image OCR (Disabled on Cloud)"

    return cleaned, values, risks, report_type
