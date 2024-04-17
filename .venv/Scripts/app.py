import streamlit as st
import pandas as pd
from streamlit_modal import Modal

import streamlit.components.v1 as components


# Content
st.markdown(
    """
    <div class="st-ba">
        <p class="st-cq">Welcome To DocAssist</p>
        <div class="st-define-wrapper">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


define = {
    "Chest Pain": "Chest pain type. 0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic",
    "Resting Blood Presure": "Measured in Millimeter of Mercury (mmHg)",
    "Cholesterol": "Measured in mg/dl - Obtained via a BMI sensor",
    "Fasting Blood Sugar": "Indicates whether the patient's fasting blood sugar level exceeds 120 mg/dl. Value 1 indicates true (fasting blood sugar > 120 mg/dl), while 0 indicates false",
    "Resting Ecg": "Resting electrocardiographic results. Value 0 indicates normal, 1 indicates having ST-T wave abnormality, 2 indicates left ventricular hypertrophy",
    "Left Ventricular Hypertrophy": "Characterized by the enlargement or thickening (hypertrophy) of the muscle wall of the left ventricle of the heart. Often correlated to blood pressure since it often occurs as a response to chronic high blood pressure",
    "Maximum Heart Rate": "Maximum heart rate achieved during any stress test --> important indicator of cardiovascular health and fitness",
    "Old Peak": "ST depression observed in ECG induced by exercise relative to rest - measured in millimeters (mm)",
    "Slope": "Slope of the peak exercise ST segment - 1: upsloping, 2: flat, 3: downsloping",
    "Major Vessels": "Number of major vessels (0-3) colored by fluoroscopy",
    "Thallium": "3 = normal; 6 = fixed defect; 7 = reversable defect",
    "Exercise Induced Angina": "Exercise-induced angina (1 = yes; 0 = no)",
    "Target": "Heart disease (1 = yes; 0 = no)"
}

def on_button_click():
    Modal(title="Define", body=define).open()
    
if st.button("Quick Check ❤️"):
    on_button_click()






# Read DataFrame
heart = pd.read_csv('C:/Users/shree/Documents/Disease/heart.csv')

# Column name replacements
replace = {
    'age': 'Age',
    'sex': 'Sex',
    'cp': 'Chest_Pain',
    'trtbps': 'Resting_Pressure',
    'chol': 'Cholesterol',
    'fbs': 'Fasting_Blood_Sugar',
    'restecg': 'Resting_Ecg_Results',
    'thalachh': 'Maximum_Heart_Rate',
    'exng': 'Exercise_Induced_Angina',
    'oldpeak': 'Old_Peak',
    'slp': 'Slope',
    'caa': 'Major_Vessels',
    'thall': 'Thallium_Rate',
    'output': 'Target'
}




# dummy_data = {
#     'Age': 0,
#     'Sex': 0,
#     'Chest_Pain': 0,
#     'Resting_Pressure': 0,
#     'Cholesterol': 0,
#     'Fasting_Blood_Sugar': 0,
#     'Resting_Ecg_Results': 0,
#     'Maximum_Heart_Rate': 0,
#     'Exercise_Induced_Angina': 0,
#     'Old_Peak': 0,
#     'Slope': 0,
#     'Major_Vessels': 0,
#     'Thallium_Rate': 0,
#     'Cholesterol_BP_Ratio': 0,
#     'Target': 0
#     }


# # Apply column name replacements
# heart.rename(columns=replace, inplace=True)

# # Display DataFrame
# st.subheader('Past Medical Records')
# st.write(heart, index=False)

# st.subheader('Add to Past Medical Records')
# new_data = {}
# for key, value in dummy_data.items():
#     new_value = st.number_input(f"Enter {key}:", value)
#     new_data[key] = new_value

# if st.button("Add Data"):
#     dummy_data.update(new_data)
#     new_row = pd.DataFrame([dummy_data])
#     heart.loc[len(heart.index)] = new_row
#     st.write("Data added successfully!")
#     st.write(heart, index=False)




# Styling
st.markdown(
    """
    <style>
    .st-ba {
        background-color: #f7f7f7;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 3.5%;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .st-cq {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        color: #FA7070;
    }
    .st-define {
            font-size: 18px;
            align-items: center;
    }
    .dataframe {
        width: 100%; /* Stretch the DataFrame */
        overflow-x: auto; /* Allow horizontal scrolling */
    }
    .st-define-wrapper {
        align-items: center;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

