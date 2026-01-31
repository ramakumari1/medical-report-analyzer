def format_extracted_values(values):
    rows = []

    ranges = {
        "hemoglobin": (12, 16),
        "rbc": (3.8, 5.0),
        "wbc": (4000, 11000),
        "platelet": (150000, 450000),
        "mcv": (80, 100),
        "mch": (27, 33),
        "mchc": (32, 36),
        "rdw": (11, 16)
    }

    for test, value in values.items():
        low, high = ranges.get(test, (None, None))

        if low and value < low:
            status = "Low"
            color = "red"
        elif high and value > high:
            status = "High"
            color = "red"
        else:
            status = "Normal"
            color = "green"

        rows.append((test.upper(), value, status, color))

    return rows
