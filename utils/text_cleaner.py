import re

def clean_medical_text(text):
    text = text.lower()

    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    # Remove phone numbers
    text = re.sub(r'\b\d{5,}\b', '', text)

    # Remove repeated hospital boilerplate words
    remove_words = [
        "laboratory report", "department of pathology",
        "consultant", "verified by", "end of report",
        "specimen", "method", "reference", "normal range"
    ]

    for w in remove_words:
        text = text.replace(w, '')

    return text.strip()
