import streamlit as st

st.set_page_config(
    page_title="Doc Assist",
    page_icon="🥼",
)

st.markdown("# Data Dictionary")

data_dict = {
    "trtbps": "Resting Blood Pressure:",
    "chol": "Cholesterol:",
    "fbs": "Fasting Blood Sugar:",
    "restecg": "Resting Electrocardiographic Results:",
    "thalachh": "Maximum Heart Rate Achieved:",
    "oldpeak": "ST Depression Induced by Exercise Relative to Rest:",
    "slp": "Slope:",
    "caa": "Number of Major Vessels:",
    "thall": "Thalium Stress Test Result:",
    "exng": "Exercise Induced Angina:",
    "output": "Target Variable:"
}

styled_dict = {
    "trtbps": "This variable represents the patient's resting blood pressure measured in millimeters of mercury (mm Hg)",
    "chol": "Cholesterol level in milligrams per deciliter (mg/dl), obtained via a BMI sensor",
    "fbs": "Indicates whether the patient's fasting blood sugar level exceeds 120 mg/dl. Value 1 indicates true (fasting blood sugar > 120 mg/dl), while 0 indicates false",
    "restecg": "Values:\n0: Normal\n1: ST-T wave abnormality\n2: Left ventricular hypertrophy\nRefers to an irregularity or deviation from the normal pattern observed in the ST segment between the S and T waves. Left ventricular hypertrophy is characterized by the enlargement or thickening of the muscle wall of the left ventricle of the heart, often occurring as a response to chronic high blood pressure",
    "thalachh": "Maximum heart rate achieved during any stress test, an important indicator of cardiovascular health and fitness",
    "oldpeak": "Previous peak ST depression observed in the electrocardiogram (ECG) induced by exercise relative to rest. ST depression is measured in millimeters (mm)",
    "slp": "Represents the slope of the peak exercise ST segment in the ECG. Different slope values indicate varying degrees of upsloping, flat, or downsloping ST segments",
    "caa": "Indicates the number of major coronary vessels colored by fluoroscopy, indicative of the severity of coronary artery disease",
    "thall": "Result of the thallium stress test, ranging from 0 to 3",
    "exng": "Indicates whether the patient experienced angina (chest pain) induced by exercise. Value 1 denotes 'Yes' (angina induced by exercise), while 0 denotes 'No'.",
    "output": "Target variable indicating the presence (1) or absence (0) of heart disease."
}

for key, value in data_dict.items():
    st.markdown(f"**{value}**")
    st.write(styled_dict[key])
    st.write("")
