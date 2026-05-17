from pathlib import Path

import streamlit as st

from app_common import PDF_DOWNLOAD_NAME, PROJECT_PDF


def render():
    st.title("About the Project")
    st.markdown(
        """
This application is based on the **Bachelor of Engineering** internship project
**“Heart Disease Prediction”** submitted by **Akanksha Vaghela** (230343131023)
in partial fulfillment of the degree in **Computer Science and Engineering** at
**Narnarayan Shashtri Institute of Technology**, under **Gujarat Technological University, Ahmedabad** (academic year 2026).
        """
    )

    st.subheader("Overview")
    st.markdown(
        """
Heart disease risk, when estimated early from patient vitals and symptoms, can help doctors
adapt diagnosis and treatment for each person. This project uses **machine learning** so users
can enter clinical inputs—such as age, sex, chest pain type, resting blood pressure, cholesterol,
blood sugar, ECG results, max heart rate, exercise angina, and related markers—and receive a
quick indication of whether they may have a higher or lower chance of heart disease.

The system is designed for everyday use and for healthcare workflows: patients can check risk
without visiting a clinic immediately, while clinicians can enter symptoms and obtain a fast,
data-driven prediction to support further evaluation.
        """
    )

    st.subheader("How it works")
    st.markdown(
        """
- **Technology:** Python with **K-Nearest Neighbors (KNN)** classification (`n_neighbors=8`) and **scikit-learn**.
- **Dataset:** Standardized features from a heart-disease dataset (`dataset.csv`).
- **User flow:** Enter health parameters on the home page and click **Predict** to see whether the model
  suggests a high or low chance of heart disease.
- **Original deliverable:** Desktop application with main input form and separate result views for healthy
  and unhealthy predictions, as documented in the project report.
        """
    )

    st.subheader("Project outcomes")
    st.markdown(
        """
The project successfully implements heart-disease prediction from basic inputs that can be
collected in a laboratory or clinical setting. It demonstrates how symptom- and vitals-based
machine learning can support early awareness and triage when a patient wants to understand
possible risk before a full hospital visit.
        """
    )

    st.subheader("Known limitations")
    st.markdown(
        """
- Prediction accuracy may be lower than commercial clinical systems.
- Larger datasets can increase processing time.
- The model indicates general heart-disease risk rather than a specific cardiac condition.
        """
    )

    st.subheader("Future enhancements")
    st.markdown(
        """
Possible improvements include adding more dataset attributes, a more interactive UI, a mobile app,
and integration with hospital databases for richer patient history.
        """
    )

    st.subheader("Full project report")
    st.write("Download the complete PDF report for chapters on system design, snapshots, and references.")

    if PROJECT_PDF.is_file():
        pdf_bytes = PROJECT_PDF.read_bytes()
        st.download_button(
            label="Download project report (PDF)",
            data=pdf_bytes,
            file_name=PDF_DOWNLOAD_NAME,
            mime="application/pdf",
            type="primary",
        )
        st.caption(f"Source file: `{PROJECT_PDF.name}`")
    else:
        st.warning(f"Project report not found at `{Path(PROJECT_PDF).name}`.")
