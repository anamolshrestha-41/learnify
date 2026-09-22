# Hospital Dataset Cleaning

## Objective

Perform data preprocessing on a hypertension dataset using Scikit-Learn.

## Dataset

The dataset contains patient-related information and a target variable:

- Age
- Salt_Intake
- Stress_Score
- BP_History
- Sleep_Duration
- BMI
- Medication
- Family_History
- Exercise_Level
- Smoking_Status
- Has_Hypertension

## Preprocessing

The project covers:

- Dataset inspection
- Missing value detection
- Duplicate detection
- Train-test split
- Numerical feature preprocessing
- Categorical feature preprocessing
- Median imputation
- Most-frequent imputation
- Standardization
- Min-Max normalization
- One-hot encoding
- Feature selection
- ColumnTransformer
- Pipeline

## Machine Learning

Model:

- Logistic Regression

## Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## Project Structure

```text
Hospital_Dataset_Cleaning/
│
├── data/
│   ├── raw/
│   │   └── hypertension_dataset.csv
│   └── processed/
│
├── models/
│   └── hypertension_model.pkl
│
├── notebooks/
│   └── hospital_preprocessing.ipynb
│
├── outputs/
│   └── plots/
│
├── README.md
└── requirements.txt