# Student Performance Prediction

A simple machine-learning project that predicts a student's final academic score using basic academic features such as attendance, study hours, internal marks, and assignments.

## Live Demo

**[GitHub Pages Browser Demo](https://DivyanshWatma29.github.io/student-performance-prediction/)** (Note: This is a static frontend-only demonstration of the prediction flow.)

## Objective

The objective of this project is to create a simple supervised machine learning model that predicts final student marks based on their academic habits and internal assessments, and to provide this prediction through a simple web interface.

## Features

- Predict final marks
- Use attendance
- Use study hours
- Use internal marks
- Use assignments
- Simple Flask interface

## How It Works

Dataset ? preprocessing ? Linear Regression ? prediction ? Flask interface

## Technologies Used

- Python
- Pandas
- scikit-learn
- Flask
- HTML/CSS

## Dataset

- **attendance**: Percentage of classes attended (0-100).
- **study_hours**: Weekly self-study hours.
- **internal_marks**: Score in internal assessments (0-100).
- **assignments**: Number of assignments completed.
- **final_marks**: The target variable to predict (0-100).

## Machine Learning Model

The project uses a **Linear Regression** model because the target variable is continuous and the relationship between features (like study hours) and final marks can be effectively modeled linearly.

## Model Evaluation

- R² Score: {R2_PLACEHOLDER}
- MAE: {MAE_PLACEHOLDER}
- RMSE: {RMSE_PLACEHOLDER}

## Project Structure

\\\
student-performance-prediction/
+-- app.py                # Flask web application
+-- train_model.py        # ML training script
+-- student_data.csv      # Dataset
+-- requirements.txt      # Python dependencies
+-- templates/
¦   +-- index.html        # Web interface
+-- docs/                 # GitHub pages static demo
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
3. Run the Flask application:
   \\\ash
   python app.py
   \\\
4. Open \http://127.0.0.1:5000\ in your browser.

## Limitations

- The dataset is relatively small and synthetic.
- Linear Regression assumes a strict linear relationship, which may not capture complex student behaviors.

## GitHub
[https://github.com/DivyanshWatma29/student-performance-prediction](https://github.com/DivyanshWatma29/student-performance-prediction)
