import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

import asyncio
import os
from sydney import SydneyClient

import sys
import path

from dotenv import load_dotenv




st.set_page_config(
    page_title="Doc Assist",
    page_icon="🥼",
)

st.markdown("# Heart Attacks Can Attack Anyone")

dir = path.Path(__file__).absolute().parent

# Adding the parent directory to sys.path
sys.path.append(dir)
# Constructing the path to the CSV file
path_to_df= dir.parent / 'heart_1.csv'

# Load the existing DataFrame
heart = pd.read_csv(path_to_df)

# Column name replacements
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

# Apply column name replacements
heart.rename(columns=replace, inplace=True)

# Plotting
plt.figure(figsize=(10,10))
sns.distplot(heart[heart['Target'] == 0]["Age"], color='green',kde=True,) 
sns.distplot(heart[heart['Target'] == 1]["Age"], color='red',kde=True)
plt.title('Attack versus Age')
plt.xlabel('Age')
plt.ylabel('Density')
st.pyplot(plt)

# Quiz Section
st.markdown("## Lifestyle Quiz")
st.write("Answer the following questions to get personalized lifestyle recommendations:")

# Physical Activity
physical_activity = st.radio("How often do you engage in physical activity?", options=["Sedentary", "Light exercise", "Moderate exercise", "Intense workouts"])
fav_physical = st.text_input("What physical activity do you enjoy the most? (Eg: Swimming, Hiking, Dancing, etc.)")
# Current Health Conditions
health_conditions = st.text_input("Do you have any existing health conditions? (e.g., diabetes, hypertension, cholesterol)")
medications = st.text_input("Are you taking any medications? (Please specify)")

# Dietary Preferences
diet_type = st.radio("What type of diet do you follow?", options=["Vegetarian", "Vegan", "Omnivore"])
diet_restrictions = st.text_input("Any dietary restrictions or allergies? (e.g., gluten-free, lactose intolerance)")
food_preferences = st.text_input("Any specific foods you love or dislike?")
meal_times = st.text_input("When do you typically have your meals? (e.g., breakfast, lunch, dinner)")
cooking_skills = st.radio("How comfortable are you with cooking?", options=["Novice", "Intermediate", "Expert"])

# Stress Management
stress_management = st.radio("How do you manage stress?", options=["Meditation", "Exercise", "Socializing"])

# Sleep Patterns
sleep_hours = st.number_input("How many hours of sleep do you get on average?", min_value=0)

# Hydration
hydration = st.radio("How much water do you drink daily?", options=["Less than 4 glasses", "4-8 glasses", "More than 8 glasses"])

# Social Support
social_support = st.text_input("Do you have a support system for maintaining heart health? (e.g., family, friends, online communities)")

# Other
smoke = st.radio("Do you smoke?", options=["Yes, regularly", "Yes, occasionally", "No, but I used to", "No, but I'm trying to quit", "No, never"])

load_dotenv()

# Access the variables
BING_COOKIES = os.getenv("BING_COOKIES")


async def main(answers) -> str:
    async with SydneyClient() as sydney:
        question = 'Based on the preferences of this person, create a schedule, health guideline, recommended diet plan, and a smoking quit plan if they smoke. Alongisde provide recommendations for support groups to help him/her improve their heart health that is customized to their interests. Be sure to make the plan as customized to the interests of the person as possible: '+str(answers)
        response = await sydney.ask(question, citations=True)
        return response.encode('ascii', 'ignore').decode('ascii')

# Function to generate plan and download it
def generate_and_download_plan(answers):
    plan = asyncio.run(main(answers))
    with open("heart_health_plan.txt", "w") as file:
        file.write(plan)
    return "heart_health_plan.txt"


# Submit Button
if st.button("Submit"):
    answers = [physical_activity, fav_physical, diet_type, diet_restrictions, health_conditions, medications,
               stress_management, sleep_hours, hydration, meal_times, food_preferences, cooking_skills, social_support, smoke]

    # Lifestyle Tips Section
    st.markdown("## Generic Tips")
    st.write("1. Maintain a healthy diet --> fruits, vegetables, and whole grains.")
    st.write("2. Engage in regular physical activity --> walking, jogging, or swimming.")
    st.write("3. Quit smoking, limit alcohol, or other drugs.")
    st.write("4. Manage stress through relaxation techniques --> meditation or yoga.")
    st.write("5. Monitor your blood pressure, cholesterol levels, and weight regularly.")
    st.write("6. Get at least 7-8 hours of sleep per night.")
    st.write("7. Drink at least 8 glasses of water to stay hydrated.")

    st.markdown("## Personalized Plan")
    plan_file_path = generate_and_download_plan(answers)
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    st.success("Plan generated successfully!")
    st.markdown("## Download Plan")
    st.write("Click the button below to download your personalized plan.")
    if st.download_button(label="Download Plan", data=open(plan_file_path, "rb"), file_name="heart_health_plan.txt"):
        st.success("Plan downloaded successfully!")

