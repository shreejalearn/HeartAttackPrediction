import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sys
import path

# Set page configuration
st.set_page_config(
    page_title="Doc Assist",
    page_icon="🥼",
)

# Sidebar message
st.sidebar.success("Select a detailed view")

# Styling
st.markdown(
    """
    <style>
    .st-ba {
        background-color: #faf9f7;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        text-align: center;
    }
    .st-cq {
        font-size: 28px;
        font-weight: bold;
        color: #B47B84;
    }
    .st-intro-wrapper {
        text-align: center;
        margin-bottom: 30px;
    }
    .st-intro {
        font-size: 26px;
        color: #CAA6A6;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .st-intro2 {
        font-size: 22px;
        color: #C7C8CC;
        margin-bottom: 20px;
    }
    .dataframe {
        width: 100%;
        overflow-x: auto;
    }
    .plot-title {
        color: #665c5c;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Content
st.markdown(
    """
    <div class="st-ba">
        <p class="st-cq">Welcome To DocAssist</p>
    </div>
    <div class="st-intro-wrapper">
        <p class="st-intro">Empowering Every Beat, One Record at a Time</p>
        <p class="st-intro2">Hosting 300+ unique medical records</p>
    </div>
    """,
    unsafe_allow_html=True
)

dir = path.Path(__file__).absolute().parent

# Adding the parent directory to sys.path
sys.path.append(dir)
# Constructing the path to the CSV file
path_to_df = dir / 'heart_1.csv'

# Reading the CSV file with pandas
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

# Image
image_url = "https://www.houstonmethodist.org/-/media/images/contenthub/article-images/heart-and-vascular/hub_covidheart_article.ashx?mw=1382&hash=4F81121C362DEA5FD559CD17D4B5624C"
st.image(image_url, caption='We care, you should too.', use_column_width=True)

# Display DataFrame
st.markdown('<h3 class="plot-title">Past Medical Records</h3>', unsafe_allow_html=True)
st.write(heart, index=False)

# Bar plot for target counts
st.markdown('<h3 class="plot-title">Equal Data</h3>', unsafe_allow_html=True)
target_counts = heart["Target"].value_counts().sort_index(ascending=True)
target_counts_df = pd.DataFrame({'Heart Attack Status': target_counts.index, 'Count': target_counts.values})
fig = px.bar(target_counts_df, x='Heart Attack Status', y='Count', 
             color_discrete_sequence=px.colors.qualitative.Set3)
fig.update_layout(xaxis_title="Heart Attack Stats", yaxis_title="Count", title_x=0.5, font_size=16, showlegend=False)
fig.update_layout(xaxis_title_text='Heart Attack Stats')
st.plotly_chart(fig, use_container_width=True)

# Histograms
fig = make_subplots(rows=2, cols=2, subplot_titles=('Chest Pain', 'Resting Pressure', 'Cholesterol', 'Maximum Heart Rate'))
fig.add_trace(go.Histogram(x=heart['Chest_Pain'], name='Chest Pain'), row=1, col=1)
fig.add_trace(go.Histogram(x=heart['Resting_Pressure'], name='Resting Pressure'), row=1, col=2)
fig.add_trace(go.Histogram(x=heart['Cholesterol'], name='Cholesterol'), row=2, col=1)
fig.add_trace(go.Histogram(x=heart['Maximum_Heart_Rate'], name='Maximum Heart Rate'), row=2, col=2)
fig.update_layout(height=600, width=800, title_x=0.5, font_size=20, font_family='Courier New')
st.plotly_chart(fig, use_container_width=True)

# Age counts bar plot
age_counts = heart["Age"].value_counts().sort_index(ascending=True)
fig, ax = plt.subplots(figsize=(10, 6))
age_counts.plot(kind='bar', color='skyblue', ax=ax)
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)
fig.tight_layout()
st.pyplot(fig)

# Sex counts pie chart
sex_counts = heart["Sex"].value_counts().sort_index(ascending=True)
plt.figure(figsize=(8, 6))
colors = plt.cm.Set3.colors
plt.pie(sex_counts, colors=colors, startangle=140, autopct='%1.1f%%')
labels = ['Female', 'Male']
plt.axis('equal')
legend = plt.legend(labels, title="Sex Distribution", loc="best", bbox_to_anchor=(1, 1))
legend.set_bbox_to_anchor((1.2, 1))
st.pyplot(plt)
