def detect_health_risks(values: dict) -> list:
    """
    Detects health risks based on extracted medical values
    """

    risks = []

    # Anemia check
    if "hemoglobin" in values:
        hb = values["hemoglobin"]
        if hb < 12:
            risks.append({
                "risk": "Possible Anemia",
                "reason": f"Hemoglobin is {hb} g/dL (Normal > 12)"
            })

    # Diabetes check
    if "glucose" in values:
        glucose = values["glucose"]
        if glucose >= 126:
            risks.append({
                "risk": "Diabetes Risk",
                "reason": f"Glucose is {glucose} mg/dL (Normal < 126)"
            })

    # Blood pressure check
    if "systolic_bp" in values and "diastolic_bp" in values:
        sys_bp = values["systolic_bp"]
        dia_bp = values["diastolic_bp"]

        if sys_bp >= 140 or dia_bp >= 90:
            risks.append({
                "risk": "High Blood Pressure",
                "reason": f"BP is {sys_bp}/{dia_bp} mmHg (Normal < 140/90)"
            })

    return risks
if __name__ == "__main__":
    sample_values = {
        "hemoglobin": 9.5,
        "glucose": 145,
        "systolic_bp": 150,
        "diastolic_bp": 95
    }

    detected_risks = detect_health_risks(sample_values)

    for risk in detected_risks:
        print(f"⚠️ {risk['risk']}")
        print(f"   Reason: {risk['reason']}\n")
