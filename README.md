# Student Performance Prediction

A simple machine-learning project that predicts a student's final academic score using basic academic features such as attendance, study hours, internal marks, and assignments.

## Live Demo

**[Streamlit Live App](https://share.streamlit.io/)** *(Note: You can deploy this easily for free on Streamlit Community Cloud and place the link here!)*

## Objective

The objective of this project is to create a simple supervised machine learning model that predicts final student marks based on their academic habits and internal assessments, and to provide this prediction through a simple interactive web app using Streamlit.

## Features

- Predict final marks
- Use attendance
- Use study hours
- Use internal marks
- Use assignments
- Simple Streamlit Python interface

## How It Works

Dataset ? preprocessing ? Linear Regression ? prediction ? Streamlit UI

## Technologies Used

- Python
- Pandas
- scikit-learn
- Streamlit

## Dataset

- **attendance**: Percentage of classes attended (0-100).
- **study_hours**: Weekly self-study hours.
- **internal_marks**: Score in internal assessments (0-100).
- **assignments**: Number of assignments completed.
- **final_marks**: The target variable to predict (0-100).

## Machine Learning Model

The project uses a **Linear Regression** model because the target variable is continuous and the relationship between features (like study hours) and final marks can be effectively modeled linearly.

## Model Evaluation

- R² Score: 0.9127
- MAE: 2.6318
- RMSE: 3.2038

## Project Structure

\\\
student-performance-prediction/
+-- app.py                # Streamlit web application
+-- train_model.py        # ML training script
+-- student_data.csv      # Dataset
+-- model.pkl             # Trained model (generated)
+-- requirements.txt      # Python dependencies
\\\

## Run Locally

1. Install dependencies:
   \\\ash
   pip install -r requirements.txt
   \\\
2. Train the model:
   \\\ash
   python train_model.py
   \\\
3. Run the Streamlit application:
   \\\ash
   streamlit run app.py
   \\\

## Limitations

- The dataset is relatively small and synthetic.
- Linear Regression assumes a strict linear relationship, which may not capture complex student behaviors.

## GitHub
[https://github.com/DivyanshWatma29/student-performance-prediction](https://github.com/DivyanshWatma29/student-performance-prediction)
