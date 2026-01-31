def detect_report_type(text):
    text = text.lower()

    if "cbc" in text or "hemoglobin" in text or "mcv" in text:
        return "CBC"

    if "cholesterol" in text or "triglyceride" in text:
        return "LIPID"

    if "bilirubin" in text or "sgot" in text or "sgpt" in text:
        return "LFT"

    if "creatinine" in text or "urea" in text:
        return "KFT"

    return "UNKNOWN"
