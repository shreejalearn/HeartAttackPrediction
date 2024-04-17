import streamlit as st
import pandas as pd
import path
import sys


dir = path.Path(__file__).absolute().parent

# Adding the parent directory to sys.path
sys.path.append(dir)
# Constructing the path to the CSV file
path_to_df= dir.parent / 'heart_1.csv'

# Load the existing DataFrame
heart = pd.read_csv(path_to_df)

replace = {
    'age': 'Age',
    'sex': 'Sex',
    'cp': 'Chest_Pain',
    'trestbps': 'Resting_Pressure',
    'chol': 'Cholesterol',
    'fbs': 'Fasting_Blood_Sugar',
    'restecg': 'Resting_Ecg_Results',
    'thalach': 'Maximum_Heart_Rate',
    'exang': 'Exercise_Induced_Angina',
    'oldpeak': 'Old_Peak',
    'slope': 'Slope',
    'ca': 'Major_Vessels',
    'thal': 'Thallium_Rate',
    'target': 'Target'
}

st.markdown("# Welcome a New Patient!")

# Collect user input
age = st.number_input("Age", min_value=0, max_value=120, value=50)
sex = st.radio("Sex", ["Male", "Female"])
chest_pain = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
resting_pressure = st.number_input("Resting Pressure", min_value=0, max_value=300, value=120)
cholesterol = st.number_input("Cholesterol", min_value=0, value=200)
blood_sugar = st.selectbox("Fasting Blood Sugar", ["Lower than 120mg/ml", "Greater than 120mg/ml"])
ecg_results = st.selectbox("Resting ECG Results", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
max_heart_rate = st.number_input("Maximum Heart Rate", min_value=0, max_value=300, value=150)
exercise_angina = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
old_peak = st.number_input("Old Peak", min_value=0.0, value=1.0)
slope = st.selectbox("Slope", ["Upsloping", "Flat", "Downsloping"])
major_vessels = st.number_input("Major Vessels", min_value=0, max_value=4, value=0)
thallium_rate = st.selectbox("Thallium Rate", ["Normal", "Fixed Defect", "Reversable Defect"])
target = st.selectbox("Target", ["Heart Disease", "Healthy"])

# Preprocess user input
sex = 1 if sex == "Male" else 0

blood_sugar = 1 if blood_sugar == "Lower than 120mg/ml" else 0

exercise_angina = 1 if exercise_angina == "Yes" else 0

ecg_results_normal = 1 if ecg_results == "Normal" else 0

chest_pain_value = 0
if chest_pain == "Typical Angina":
    chest_pain_value = 0
elif chest_pain == "Atypical Angina":
    chest_pain_value = 1
elif chest_pain == "Non-anginal Pain":
    chest_pain_value = 2
elif chest_pain == "Asymptomatic":
    chest_pain_value = 3

slope_value = 0
if slope == "Upsloping":
    slope_value = 0
elif slope == "Flat":
    slope_value = 1
elif slope == "Downsloping":
    slope_value = 2

thallium_normal = 0
if thallium_rate == "Normal":
    thallium_normal = 0
elif thallium_rate == "Fixed defect":
    thallium_normal = 1
else:
    thallium_normal = 2

target = 1 if target == "Heart Disease" else 0

# Create a new row DataFrame
new_row = {
    'age': [age],
    'sex': [sex],
    'cp': [chest_pain_value],
    'trestbps': [resting_pressure],
    'chol': [cholesterol],
    'fbs': [blood_sugar],
    'restecg': [ecg_results_normal],
    'thalach': [max_heart_rate],
    'exang': [exercise_angina],
    'oldpeak': [old_peak],
    'slope': [slope_value],
    'ca': [major_vessels],
    'thal': [thallium_normal],
    'target': [target]
}


if st.button("Add New Record"):
  # Concatenate the new row with the existing DataFrame and assign it back to 'heart'

  new_row_df = pd.DataFrame(new_row)

  heart = pd.concat([heart, new_row_df], ignore_index=True)

  # Fix indentation
  st.write("Data was added!")
  st.write(heart, index=False)
