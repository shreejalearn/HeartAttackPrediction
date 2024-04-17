import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Doc Assist",
    page_icon="🥼",
)

st.markdown("# Taking A Closer Look")

heart = pd.read_csv('C:/Users/shree/Documents/Disease/heart_1.csv')

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

# Function to plot KDE distribution
def plot_distribution(data, column, target, ax):
    sns.kdeplot(data=data, x=column, hue=target, fill=True, palette=["#8000ff", "#da8829"], alpha=.5,
                linewidth=0, ax=ax)
    ax.set_xlabel(column.capitalize().replace('_', ' '))
    ax.set_ylabel("")
    ax.grid(color='#000000', linestyle=':', axis='y', zorder=0, dashes=(1, 5))

# Function to plot text annotation
def plot_text_annotation(text, ax):
    ax.text(0.5, 0.5, text,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=18,
            fontweight='bold',
            fontfamily='serif',
            color='#000000')

# Plotting
columns_to_plot = ['Age', 'Resting_Pressure', 'Cholesterol', 'Maximum_Heart_Rate', 'Old_Peak', 'Chest_Pain', 'Major_Vessels', 'Sex', 'Thallium_Rate', 'Resting_Ecg_Results', 'Fasting_Blood_Sugar', 'Exercise_Induced_Angina', 'Slope']
fig, axs = plt.subplots(len(columns_to_plot), 2, figsize=(18, 24))
fig.subplots_adjust(wspace=0.5, hspace=0.5)

for i, column in enumerate(columns_to_plot):
    plot_text_annotation(f"Distribution of {column}\naccording to\nTarget Variable\n___________", axs[i, 0])
    plot_distribution(heart, column, "Target", axs[i, 1])

# Remove spines for all subplots
for ax in axs.flat:
    for i in ["top", "left", "right"]:
        ax.spines[i].set_visible(False)

# Show the plot
st.pyplot(fig)
