import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import plotly.express as px

# Load your dataset
try:
    df = pd.read_csv("depression.csv")
except FileNotFoundError:
    st.error("The dataset file 'depression.csv' was not found. 🧐")

# Drop the 'id' column
df = df.drop(columns=['id'])

st.set_page_config(page_title="Depression Analysis 🧠", page_icon="🧠", layout="wide")

# Sidebar for navigation
st.sidebar.image('depression.png')

# Sidebar navigation
st.sidebar.title("Choose Your Overview 📊")
option = st.sidebar.radio("Select analysis", ["1. Overview 📝", "2. Effects by Age 👶👴", "3. Gender, Profession & Degree 🧑‍💼🎓",
                                              "4. Stress & Satisfaction 😰😌", "5. Sleep & Diet 🛏️🥗"])

st.sidebar.markdown('---')
st.sidebar.markdown("### Check out the [Depression Test 🧑‍⚕️](https://depression-checker-cb3p.onrender.com)")

# 1. Overview of Data 📝
if option == "1. Overview 📝":
    st.title("Overview of the Data 🧑‍💻")
    st.write(
        "The dataset contains data on student depression, including various factors such as age, gender, profession, and more.")
    st.write(f"Number of rows: {df.shape[0]}, Number of columns: {df.shape[1]}")
    st.write("Columns in the dataset: ", df.columns)
    st.write(df.describe())
    st.write("Missing values in the dataset: ", df.isnull().sum())

    # Convert categorical columns to numerical for correlation matrix
    df_corr = df.copy()

    # Label encode categorical columns (e.g., Gender, Profession, Degree, etc.)
    label_encoder = LabelEncoder()
    categorical_columns = ['Gender', 'Profession', 'Degree', 'City', 'Sleep Duration', 'Dietary Habits',
                           'Have you ever had suicidal thoughts ?',
                           'Family History of Mental Illness']

    for col in categorical_columns:
        df_corr[col] = label_encoder.fit_transform(df_corr[col])

    # Shortening column names for better display
    df_corr.columns = [col[:8] for col in df_corr.columns]

    # Plotting a heatmap to show correlations using Plotly
    st.subheader("Correlation Heatmap 🔥")
    corr_matrix = df_corr.corr()
    fig_plotly = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='Blues',
        colorbar=dict(title="Correlation Value")
    ))
    fig_plotly.update_layout(
        title="Correlation Heatmap 🔥",
        xaxis_title="Features",
        yaxis_title="Features",
        autosize=True,
        width=1000,
        height=600
    )
    st.plotly_chart(fig_plotly, use_container_width=True)

    st.write("""
    **Interpretation**: The heatmap visualizes the correlation between various features. It shows a notable correlation between `Academic Pressure` and `Stress`, with a negative correlation between `Sleep Duration` and depression.
    """)
    st.markdown('---')

# 2. Effects by Age 👶👴
elif option == "2. Effects by Age 👶👴":
    st.title("Age-wise Depression Analysis 📊")
    st.markdown('---')
    # Define age bins based on unique age values
    age_bins = [18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 60]
    age_labels = ["18-22", "23-26", "27-30", "31-34", "35-38", "39-42", "43-46", "47-50", "51-54", "55-58", "59+"]

    # Group ages into these bins
    df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)

    # Group by Age Group and Depression and calculate proportions
    age_depression = df.groupby(['Age Group', 'Depression']).size().unstack(fill_value=0)
    age_depression = age_depression.div(age_depression.sum(axis=1), axis=0)  # Normalize to proportions
    age_depression = age_depression.reset_index()

    # Age-wise Depression plot
    fig = px.bar(age_depression, x='Age Group', y=age_depression.columns,
                 title="Depression Rate by Age Group 🧑‍🦳👶",
                 labels={'Age Group': 'Age Group', 'value': 'Proportion of Depression'},
                 barmode="stack")
    st.plotly_chart(fig, use_container_width=True, key="age_depression_chart")

    st.write("""
    **Interpretation**: Younger age groups (18-30 years) exhibit higher rates of depression compared to older groups.
    """)

    with st.expander("View Suicidal Thoughts vs Depression Interpretation 🤔"):
        st.write("""
        Students who have reported experiencing suicidal thoughts show higher depression rates, emphasizing the need for support for at-risk individuals.
        """)

    # Add Suicidal Thoughts vs Depression plot
    fig7 = px.bar(df, x="Have you ever had suicidal thoughts ?", color="Depression",
                  title="Suicidal Thoughts vs Depression 💭", barmode="stack")
    st.plotly_chart(fig7, use_container_width=True, key="suicidal_thoughts_depression_chart")

    st.markdown('---')

# 3. Gender, Profession & Degree 🧑‍💼🎓
elif option == "3. Gender, Profession & Degree 🧑‍💼🎓":
    st.title("Gender, Profession & Degree vs. Depression 👩‍🏫💼")
    st.markdown('---')

    # Dropdown menus for Gender, Profession, Degree
    gender_selected = st.multiselect('Select Gender 👨‍⚖️👩‍⚖️', options=df['Gender'].unique(), default=df['Gender'].unique())
    profession_selected = st.multiselect('Select Profession 👨‍💻👩‍🔬', options=df['Profession'].unique(), default=df['Profession'].unique())
    degree_selected = st.multiselect('Select Degree 🎓', options=df['Degree'].unique(), default=df['Degree'].unique())

    st.write(f"Selected Gender: {gender_selected}, Profession: {profession_selected}, Degree: {degree_selected}")

    # Filter the dataset based on dropdown selections using .isin()
    filtered_df = df[df['Gender'].isin(gender_selected) &
                     df['Profession'].isin(profession_selected) &
                     df['Degree'].isin(degree_selected)]

    if filtered_df.empty:
        st.write("No data available for the selected filters. 😞")
    else:
        # Gender vs Depression plot
        fig1 = px.bar(filtered_df, x="Gender", color="Depression", title="Gender vs Depression 👩‍🦳", barmode="stack")
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('---')

        # Profession vs Depression plot
        fig2 = px.bar(filtered_df, x="Profession", color="Depression", title="Profession vs Depression 💼",
                      barmode="stack")
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('---')

        # Degree vs Depression plot
        fig3 = px.bar(filtered_df, x="Degree", color="Depression", title="Degree vs Depression 🎓", barmode="stack")
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown('---')

        st.write(""" **Interpretation**: The selected filters show how depression rates differ based on the chosen gender, profession, and degree. 📊""")
    st.markdown('---')

# 4. Stress & Satisfaction 😰😌
elif option == "4. Stress & Satisfaction 😰😌":
    st.title("Stress, Satisfaction, and Depression 😰😌")
    st.markdown('---')

    stress_factors = ['Academic Pressure', 'Work Pressure', 'CGPA', 'Study Satisfaction',
                      'Job Satisfaction', 'Financial Stress', 'Work/Study Hours']

    for factor in stress_factors:
        with st.expander(f"View {factor} vs Depression Plot 📊"):
            fig = px.box(df, x="Depression", y=factor, title=f"{factor} vs Depression 📉")
            st.plotly_chart(fig, use_container_width=True, key=f"{factor}_depression_boxplot")

    st.write("""
    **Interpretation for Academic Pressure**: Higher academic pressure correlates with increased depression levels among students.
    """)

    st.markdown('---')

# 5. Sleep & Diet 🛏️🥗
elif option == "5. Sleep & Diet 🛏️🥗":
    st.title("Sleep Duration & Dietary Habits Effects on Depression 🛏️🥗")
    st.markdown('---')

    # Sleep Duration vs Depression
    with st.expander("View Sleep Duration vs Depression Plot 💤"):
        fig5 = px.histogram(df, x="Sleep Duration", color="Depression", barmode="stack",
                            title="Sleep Duration vs Depression 💤")
        st.plotly_chart(fig5, use_container_width=True, key="sleep_duration_depression_histogram")

    st.write("""
    **Interpretation**: Shorter sleep durations correlate with higher depression levels, emphasizing the importance of adequate sleep.
    """)

    # Dietary Habits vs Depression
    with st.expander("View Dietary Habits vs Depression Plot 🥗"):
        fig6 = px.histogram(df, x="Dietary Habits", color="Depression", barmode="stack",
                            title="Dietary Habits vs Depression 🥦")
        st.plotly_chart(fig6, use_container_width=True, key="dietary_habits_depression_histogram")

    st.write("""
    **Interpretation**: Poor dietary habits are associated with higher depression levels, indicating the importance of a balanced diet for mental health.
    """)

    st.markdown('---')

# 6. Footer with Credits 🏆
st.markdown("""
    Developed by [Akshat Sharma](https://github.com/Akshat-Sharma-110011) | Data from [Source](https://www.kaggle.com/datasets/ikynahidwin/depression-student-dataset) 🌐
""")
