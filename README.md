# DiabetesRiskClassifier

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📊 Overview
**DiabetesRiskClassifier** is a machine learning project that predicts an individual's diabetes status using health and lifestyle indicators. The model classifies risk into three stages:
- `0` = No Diabetes
- `1` = Prediabetes
- `2` = Diabetes

The goal is to support early intervention efforts and increase awareness of prediabetes risks using data-driven insights.

## 📁 Dataset
- **Source:** [Diabetes Health Indicators Dataset (Kaggle)](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data)
- **Records:** 253,680 entries
- **Features:** 21 indicators including BMI, hypertension, cholesterol, smoking, physical activity, and general health

## 🛠️ Tools & Libraries
- Python
- pandas, numpy
- scikit-learn
- matplotlib, seaborn
- Jupyter Notebooks

## 🧠 Machine Learning Workflow
- **Data Preprocessing:** Cleaning, encoding, scaling
- **Exploratory Data Analysis (EDA):** Correlations, class distribution, feature importance
- **Modeling:**
  - Logistic Regression
- **Evaluation:**
  - Accuracy, Recall, Precision, F1-score
  - Confusion Matrix
  - ROC-AUC (One-vs-Rest)

## 📈 Results
TBD

## 💡 Future Improvements
- TBD

## Project Directory Structure
DiabetesRiskClassifier/
│
├── data/                       
│   ├── README.md               # How to download the dataset using Kaggle API
│   └── download_kaggle_data.py # Script to fetch the dataset automatically
│
├── notebooks/                  
│   └── 01_eda.ipynb            # Exploratory Data Analysis
│   └── 02_modeling.ipynb       # Model training and evaluation
│
├── scripts/                    
│   └── preprocess.py           # (Optional) Preprocessing or helper functions
│
├── results/                    
│   └── accuracy_vs_model.png   # Plots, metrics, confusion matrices, etc.
│
├── environment.yaml            # Conda environment for reproducibility
├── requirements.txt            # Environment for pip users
├── .gitignore                  # Ignores large or sensitive files (e.g. kaggle.json)
├── README.md                   # Project overview and instructions
└── LICENSE                     # Open source license
