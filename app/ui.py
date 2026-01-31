from app.backend import process_medical_report, process_medical_image
import streamlit as st
import pandas as pd
import os
from datetime import datetime

from backend import process_medical_report, process_medical_image
from utils.ui_formatter import format_extracted_values
from utils.summary_generator import generate_clinical_summary


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Medical NLP Analyzer",
    layout="wide"
)

st.title("🩺 Medical Report Analyzer (OCR + NLP)")
st.caption("Analyze medical reports using OCR and Natural Language Processing")


# ---------------- SESSION STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

if "latest" not in st.session_state:
    st.session_state.latest = None


# ---------------- HELPER ----------------
def calculate_severity(risks):
    if len(risks) >= 3:
        return "High"
    elif len(risks) == 2:
        return "Medium"
    elif len(risks) == 1:
        return "Low"
    return "Normal"


# ---------------- TABS ----------------
tabs = st.tabs(["📸 Image Upload", "📝 Text Input", "📊 Results", "🕘 History"])


# =================================================
# 📸 IMAGE UPLOAD TAB
# =================================================
with tabs[0]:
    st.subheader("Upload Medical Report Image")

    image_file = st.file_uploader(
        "Choose a report image",
        type=["png", "jpg", "jpeg"]
    )

    if image_file:
        st.image(image_file, caption="Uploaded Report", use_column_width=True)

        image_path = os.path.join("data/raw_reports", image_file.name)
        with open(image_path, "wb") as f:
            f.write(image_file.getbuffer())

        if st.button("🔍 Analyze Image"):
            cleaned, values, risks, report_type = process_medical_image(image_path)
            severity = calculate_severity(risks)

            st.session_state.latest = {
                "cleaned": cleaned,
                "values": values,
                "risks": risks,
                "severity": severity,
                "report_type": report_type
            }

            st.session_state.history.append({
                "time": datetime.now(),
                "severity": severity,
                "report_type": report_type,
                "risk_count": len(risks)
            })

            st.success("Image analyzed successfully. Go to Results tab.")


# =================================================
# 📝 TEXT INPUT TAB
# =================================================
with tabs[1]:
    st.subheader("Enter Medical Report Text")

    text_input = st.text_area(
        "Paste medical report here",
        height=220
    )

    if st.button("🔍 Analyze Text") and text_input.strip():
        cleaned, values, risks, report_type = process_medical_report(text_input)
        severity = calculate_severity(risks)

        st.session_state.latest = {
            "cleaned": cleaned,
            "values": values,
            "risks": risks,
            "severity": severity,
            "report_type": report_type
        }

        st.session_state.history.append({
            "time": datetime.now(),
            "severity": severity,
            "report_type": report_type,
            "risk_count": len(risks)
        })

        st.success("Text analyzed successfully. Go to Results tab.")


# =================================================
# 📊 RESULTS TAB
# =================================================
with tabs[2]:
    if st.session_state.latest is None:
        st.info("Run an analysis to see results.")
    else:
        data = st.session_state.latest

        # ---- Report Type ----
        st.subheader("🧾 Report Type Detected")
        st.info(data["report_type"])

        # ---- Clinical Interpretation ----
        st.subheader("🩺 Clinical Interpretation")
        summary_text = generate_clinical_summary(
            data["values"], data["risks"]
        )
        st.success(summary_text)

        # ---- Clinical Table ----
        st.subheader("📋 Clinical Summary")

        rows = format_extracted_values(data["values"])

        if rows:
            df = pd.DataFrame(
                rows,
                columns=["Test", "Value", "Status", "Color"]
            )

            def highlight(row):
                return [
                    "",
                    "",
                    f"color:{row['Color']}; font-weight:bold;",
                    ""
                ]

            st.dataframe(
                df.style.apply(highlight, axis=1),
                use_container_width=True
            )
        else:
            st.warning("No key clinical values extracted from this report.")

        # ---- Risks ----
        st.subheader("⚠️ Health Risks")
        if data["risks"]:
            for r in data["risks"]:
                st.warning(f"{r['risk']} — {r['reason']}")
        else:
            st.success("No major health risks detected.")

        # ---- Severity ----
        st.subheader("📈 Severity Level")
        sev = data["severity"]

        if sev == "High":
            st.error("HIGH RISK")
        elif sev == "Medium":
            st.warning("MEDIUM RISK")
        elif sev == "Low":
            st.info("LOW RISK")
        else:
            st.success("NORMAL")

        # ---- Processed OCR Text (DEBUG ONLY) ----
        with st.expander("🔍 View Processed Text (For Reference)"):
            st.text(data["cleaned"])

        # ---- Download ----
        report_text = f"""
REPORT TYPE:
{data['report_type']}

SEVERITY:
{data['severity']}

EXTRACTED VALUES:
{data['values']}

RISKS:
{data['risks']}
"""
        st.download_button(
            "⬇️ Download Report",
            report_text,
            file_name="medical_report_analysis.txt"
        )


# =================================================
# 🕘 HISTORY TAB
# =================================================
with tabs[3]:
    if not st.session_state.history:
        st.info("No history available.")
    else:
        for h in reversed(st.session_state.history):
            st.write(f"🕒 {h['time'].strftime('%Y-%m-%d %H:%M:%S')}")
            st.write(f"Report Type: **{h['report_type']}**")
            st.write(f"Severity: **{h['severity']}**")
            st.write(f"Risks detected: {h['risk_count']}")
            st.markdown("---")
