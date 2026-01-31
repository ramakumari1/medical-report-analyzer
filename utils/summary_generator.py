def generate_clinical_summary(values, risks):
    summary = []

    if "hemoglobin" in values:
        hb = values["hemoglobin"]

        if hb < 12:
            summary.append(f"Hemoglobin is low ({hb} g/dL), suggesting anemia.")
        elif hb > 16:
            summary.append(
                f"Hemoglobin is high ({hb} g/dL), which may indicate dehydration or polycythemia."
            )
        else:
            summary.append(f"Hemoglobin level is within the normal range ({hb} g/dL).")

    if "rbc" in values:
        summary.append(f"RBC count is {values['rbc']} million/cumm.")

    if "wbc" in values:
        summary.append(f"WBC count is {values['wbc']} cells/cumm.")

    if "platelet" in values:
        summary.append(f"Platelet count is {values['platelet']} lakhs/cumm.")

    if not summary:
        return "No significant clinical parameters could be interpreted."

    return " ".join(summary)
