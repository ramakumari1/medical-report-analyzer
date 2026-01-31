from utils.ocr_reader import extract_text_from_image

text = extract_text_from_image("data/raw_reports/report_image.png")
print(text)
