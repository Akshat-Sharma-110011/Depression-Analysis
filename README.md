# Depression Analysis Dashboard 🧠

This is a Streamlit-based web application designed to analyze a dataset on student depression, with a focus on various factors such as age, gender, profession, degree, stress, sleep, dietary habits, and more. The application allows users to explore data insights visually and interactively using Plotly graphs.

## Features 📊

- **Overview 📝**: Displays general information about the dataset, including summary statistics and missing values.
- **Effects by Age 👶👴**: Analyzes the relationship between age groups and depression rates.
- **Gender, Profession & Degree 🧑‍💼🎓**: Provides insights into how depression rates vary across gender, profession, and degree.
- **Stress & Satisfaction 😰😌**: Examines the impact of stress factors (e.g., academic pressure, financial stress) and satisfaction on depression levels.
- **Sleep & Diet 🛏️🥗**: Explores the relationship between sleep duration, dietary habits, and depression.

The dashboard is designed to be intuitive and user-friendly, with visualizations that help communicate insights effectively.

## Technologies Used ⚙️

- **Streamlit**: Used for creating the interactive web application.
- **Plotly**: Used for generating interactive visualizations (heatmaps, bar charts, box plots, etc.).
- **Pandas**: Used for data manipulation and analysis.
- **Scikit-learn**: Used for label encoding of categorical variables.
- **Python**: Core programming language used to build the application.

## Installation 🔧

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/depression-analysis-dashboard.git
   cd depression-analysis-dashboard
   ```

2. Set up a Python virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts ctivate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

   Your browser should open with the app running at `http://localhost:8501`.

## Dataset 📑

The dataset used for this analysis contains information about student depression, including demographic details and factors contributing to mental health. It was sourced from [Kaggle](https://www.kaggle.com/datasets/ikynahidwin/depression-student-dataset).

## Usage 📈

Once the app is running, users can interact with the various sections in the sidebar:
- **Overview 📝**: Displays basic information and summary statistics of the dataset.
- **Effects by Age 👶👴**: Visualizes depression rates by age group.
- **Gender, Profession & Degree 🧑‍💼🎓**: Visualizes how gender, profession, and degree affect depression rates.
- **Stress & Satisfaction 😰😌**: Visualizes how stress and satisfaction factors are related to depression.
- **Sleep & Diet 🛏️🥗**: Visualizes the relationship between sleep, diet, and depression.

You can filter the data and explore the results by selecting different options in the sidebar.

## Contributing 🤝

If you'd like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request. Please make sure to write clear commit messages and follow good coding practices.

## License ⚖️

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits 🙌

- Developed by [Akshat Sharma](https://github.com/Akshat-Sharma-110011)
- Dataset from [Kaggle - Depression Student Dataset](https://www.kaggle.com/datasets/ikynahidwin/depression-student-dataset)
