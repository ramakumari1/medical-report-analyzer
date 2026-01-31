import re

def extract_values(text):
    """
    Extracts common CBC / lab values from medical text
    """
    values = {}
    text = text.lower()

    # OCR common fixes
    text = text.replace("haemoglobin", "hemoglobin")
    text = text.replace("haemosibin", "hemoglobin")

    def find_value(keyword, max_chars=40):
        match = re.search(rf"{keyword}.{{0,{max_chars}}}", text)
        if match:
            nums = re.findall(r"\d+\.?\d*", match.group())
            if nums:
                return float(nums[0])
        return None

    tests = {
        "hemoglobin": "hemoglobin",
        "rbc": "rbc",
        "wbc": "wbc",
        "platelet": "platelet",
        "mcv": "mcv",
        "mch": "mch",
        "mchc": "mchc",
        "rdw": "rdw"
    }

    for key, label in tests.items():
        value = find_value(key)
        if value is not None:
            values[label] = value

    return values
