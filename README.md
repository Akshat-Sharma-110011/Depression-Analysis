# Depression Analysis Dashboard 🧠  

This is a comprehensive **Streamlit-based web application** designed to analyze and visualize student depression data, focusing on multiple contributing factors such as age, gender, profession, academic degree, stress levels, sleep patterns, dietary habits, and more. The dashboard provides users with interactive and visually appealing insights into the dataset, enabling better understanding and awareness of depression trends among students.

---

## Features 📊  

The **Depression Analysis Dashboard** offers the following key functionalities:  

### 1. **Overview 📝**  
- Displays essential information about the dataset, including:  
  - Summary statistics (mean, median, standard deviation, etc.)  
  - Distribution of variables (histograms, pie charts, etc.)  
  - Identification of missing or null values in the dataset.  
- Helps users gain a foundational understanding of the data before diving into detailed analyses.  

### 2. **Effects by Age 👶👴**  
- Analyzes depression rates across different age groups.  
- Provides visualizations such as bar charts, box plots, and heatmaps to show trends and variations by age.  
- Helps understand if certain age groups are more vulnerable to depression.  

### 3. **Gender, Profession & Degree 🧑‍💼🎓**  
- Examines depression rates based on gender, profession (e.g., student, working professional), and academic degree levels.  
- Visualizes trends through grouped bar charts, stacked charts, and scatter plots.  
- Enables a deeper understanding of how social and professional roles relate to mental health.  

### 4. **Stress & Satisfaction 😰😌**  
- Explores the impact of stress factors (e.g., academic stress, financial pressure, relationship challenges) on mental health.  
- Analyzes how overall life satisfaction influences depression levels.  
- Provides actionable insights using correlation heatmaps, violin plots, and custom sliders for interactive exploration.  

### 5. **Sleep & Diet 🛏️🥗**  
- Investigates the relationship between sleep duration, quality of sleep, and dietary habits with depression levels.  
- Displays trends using bubble charts, line graphs, and treemaps.  
- Highlights the importance of sleep hygiene and balanced nutrition in maintaining mental health.  

Each section of the dashboard allows users to filter the data based on custom inputs (e.g., gender, age group) and dynamically updates visualizations to reflect these choices.  

---

## Technologies Used ⚙️  

The application leverages the following technologies to ensure robust performance and an engaging user experience:  

- **[Streamlit](https://streamlit.io/):** For building the interactive and responsive web application.  
- **[Plotly](https://plotly.com/):** For creating interactive, high-quality visualizations like heatmaps, bar charts, and scatter plots.  
- **[Pandas](https://pandas.pydata.org/):** For data manipulation, cleaning, and exploratory data analysis (EDA).  
- **[Scikit-learn](https://scikit-learn.org/):** For encoding categorical variables, enabling seamless analysis.  
- **[Python](https://www.python.org/):** Core programming language used for all backend logic and data processing.  

---

## Installation 🔧  

Follow these steps to set up and run the project locally on your machine:  

### 1. **Clone the Repository:**  
```bash  
git clone https://github.com/your-username/depression-analysis-dashboard.git  
cd depression-analysis-dashboard  
```  

### 2. **Set Up a Virtual Environment (Recommended):**  
```bash  
python3 -m venv venv  
source venv/bin/activate  # For Windows, use `venv\Scriptsctivate`  
```  

### 3. **Install Dependencies:**  
Install the required Python libraries:  
```bash  
pip install -r requirements.txt  
```  

### 4. **Run the Streamlit App:**  
Launch the dashboard in your default web browser:  
```bash  
streamlit run app.py  
```  

The app will be available at **`http://localhost:8501`**.  

---

## Dataset 📑  

The dataset used in this project is titled **“Depression Student Dataset”**, sourced from [Kaggle](https://www.kaggle.com/datasets/ikynahidwin/depression-student-dataset). It contains the following key attributes:  

- **Demographics:** Age, gender, profession, degree.  
- **Mental Health Factors:** Depression severity levels, stress levels, life satisfaction.  
- **Lifestyle Factors:** Sleep duration, dietary habits, exercise routines.  

This dataset provides a well-rounded view of factors influencing student mental health, making it ideal for a multifaceted analysis.  

---

## Usage 📈  

After running the application, users can interact with the dashboard through the sidebar and navigate between the following sections:  

1. **Overview 📝:** Basic information, missing value analysis, and descriptive statistics.  
2. **Effects by Age 👶👴:** Visualizes age-related depression patterns.  
3. **Gender, Profession & Degree 🧑‍💼🎓:** Examines the role of gender and profession in depression rates.  
4. **Stress & Satisfaction 😰😌:** Correlates stress and satisfaction levels with mental health.  
5. **Sleep & Diet 🛏️🥗:** Highlights the significance of lifestyle factors like sleep and diet in managing depression.  

Users can also filter the dataset based on custom criteria and view updated visualizations in real time.  

---

## Contributing 🤝  

We welcome contributions to enhance this project! To contribute:  
1. Fork the repository.  
2. Create a feature branch:  
   ```bash  
   git checkout -b feature-name  
   ```  
3. Commit changes with clear and concise messages.  
4. Push to the branch and submit a pull request.  

Contributions can include:  
- Adding new visualizations.  
- Improving existing features.  
- Optimizing code for performance.  
- Writing detailed documentation.  

---

## License ⚖️  

This project is licensed under the **MIT License**, allowing you to freely modify and distribute the code while providing appropriate credit. For more details, see the [LICENSE](LICENSE) file.  

---

## Credits 🙌  

- **Developed by:** [Akshat Sharma](https://github.com/Akshat-Sharma-110011)  
- **Dataset:** [Kaggle - Depression Student Dataset](https://www.kaggle.com/datasets/ikynahidwin/depression-student-dataset)  
- **Acknowledgments:** Thanks to the Kaggle community for providing open datasets that make such projects possible.  

---  

This dashboard aims to foster awareness and understanding of student mental health, encouraging informed discussions and actionable strategies to combat depression.
