import streamlit as st
import pandas as pd
import joblib

import numpy as np
from sklearn.preprocessing import RobustScaler


# User Interface
st.markdown("# Heart Attack Risk Score (Predict)")

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
thallium_rate = st.selectbox("Thallium Rate", ["Normal", "Fixed defect", "Reversible defect"])

# Preprocess user input
sex_male = 1 if sex == "Male" else 0
sex_female = 1 if sex == "Female" else 0

blood_sugar_lower = 1 if blood_sugar == "Lower than 120mg/ml" else 0
blood_sugar_greater = 1 if blood_sugar == "Greater than 120mg/ml" else 0

exercise_angina_yes = 1 if exercise_angina == "Yes" else 0
exercise_angina_no = 1 if exercise_angina == "No" else 0

ecg_results_normal = 1 if ecg_results == "Normal" else 0
ecg_results_stt_abnormality = 1 if ecg_results == "ST-T wave abnormality" else 0
ecg_results_lv_hypertrophy = 1 if ecg_results == "Left ventricular hypertrophy" else 0

slope_upsloping = 1 if slope == "Upsloping" else 0
slope_flat = 1 if slope == "Flat" else 0
slope_downsloping = 1 if slope == "Downsloping" else 0

thallium_normal = 1 if thallium_rate == "Normal" else 0
thallium_fixed = 1 if thallium_rate == "Fixed defect" else 0
thallium_reversible = 1 if thallium_rate == "Reversible defect" else 0

# Create a DataFrame with user input
user_input = pd.DataFrame({
    'Age': [age],
    'Sex_Male': [sex_male],
    'Sex_Female': [sex_female],
    'Chest_Pain_Typical Angina': [1 if chest_pain == "Typical Angina" else 0],
    'Chest_Pain_Atypical Angina': [1 if chest_pain == "Atypical Angina" else 0],
    'Chest_Pain_Non-anginal Pain': [1 if chest_pain == "Non-anginal Pain" else 0],
    'Chest_Pain_Asymptomatic': [1 if chest_pain == "Asymptomatic" else 0],
    'Resting_Pressure': [resting_pressure],
    'Cholesterol': [cholesterol],
    'Fasting_Blood_Sugar_Lower': [blood_sugar_lower],
    'Fasting_Blood_Sugar_Greater': [blood_sugar_greater],
    'Resting_Ecg_Normal': [ecg_results_normal],
    'Resting_Ecg_ST_T_Abnormality': [ecg_results_stt_abnormality],
    'Resting_Ecg_LV_Hypertrophy': [ecg_results_lv_hypertrophy],
    'Maximum_Heart_Rate': [max_heart_rate],
    'Exercise_Induced_Angina_Yes': [exercise_angina_yes],
    'Exercise_Induced_Angina_No': [exercise_angina_no],
    'Old_Peak': [old_peak],
    'Slope_Upsloping': [slope_upsloping],
    'Slope_Flat': [slope_flat],
    'Slope_Downsloping': [slope_downsloping],
    'Major_Vessels': [major_vessels],
    'Thallium_Normal': [thallium_normal],
    'Thallium_Fixed': [thallium_fixed],
    'Thallium_Reversible': [thallium_reversible]
})

# Button to trigger prediction
if st.button("Predict"):
    # Load the trained model
    model = joblib.load('C:/Users/shree/Documents/Disease/heart_attack_model.joblib')

    # Sample data for prediction

    extreme_min = [29, 0, 0, 80, 100, 0, 0, 60, 0, 0.0, 0, 0, 0, 1.25]  # Minimum values for all features
    extreme_max = [77, 1, 3, 200, 400, 1, 2, 202, 1, 6.2, 2, 3, 7, 2.0]  # Maximum values for all features

    data_to_predict = extreme_min

    # Calculate 'Cholesterol_BP_ratio' and append it to the list
    data_to_predict.append(data_to_predict[4] / data_to_predict[3])

    # Define the indices of the categorical columns used during training
    cat_cols = ['Sex', 'Exercise_Induced_Angina', 'Major_Vessels', 'Chest_Pain', 'Fasting_Blood_Sugar', 'Resting_Ecg_Results', 'Slope', 'Thallium_Rate']
    cat_col_indices = [1,8,11,2,5,6,10,12]
                    
    encoded_categorical = np.zeros((1, len(cat_col_indices)))
    for i, col_index in enumerate(cat_col_indices):
        val = data_to_predict[col_index]
        encoded_categorical[0][i] = val

    # Combine encoded and non-encoded variables into a single list
    combined_data = data_to_predict + encoded_categorical.tolist()[0]

    print(combined_data)

    # Scale the continuous part
    scaler = RobustScaler()
    scaled_combined = scaler.fit_transform([combined_data])
    # Reshape scaled_combined into a 2D array with a single row
    scaled_combined_2d = scaled_combined.reshape(1, -1)

    # Make prediction
    prediction = model.predict(scaled_combined_2d)
    if(prediction[0] == 0):
        st.write("Predicted Output: No Heart Attack")
    elif(prediction[0] == 1):
        st.write("Predicted Output: Heart Attack")
    else:
        st.write("Predicted Output: Unknown")
