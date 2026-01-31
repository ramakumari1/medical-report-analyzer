import re

def extract_medical_values(text):
    values = {}
    text = text.lower()

    # Fix common OCR mistakes
    text = text.replace("haemosibin", "hemoglobin")
    text = text.replace("haemoglobin", "hemoglobin")

    def find_value(keyword, max_chars=40):
        block = re.search(rf"{keyword}(.{{0,{max_chars}}})", text)
        if block:
            nums = re.findall(r"\d+\.?\d*", block.group(1))
            if nums:
                return float(nums[0])
        return None

    values_map = {
        "hemoglobin": "hemoglobin",
        "rbc": "rbc",
        "wbc": "wbc",
        "platelet": "platelet",
        "mcv": "mcv",
        "mch": "mch",
        "mchc": "mchc",
        "rdw": "rdw"
    }

    for key, label in values_map.items():
        val = find_value(key)
        if val is not None:
            values[label] = val

    return values
