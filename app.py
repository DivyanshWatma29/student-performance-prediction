from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    model = None
    print("Error loading model. Make sure to run train_model.py first.")

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None
    if request.method == 'POST':
        try:
            # Read inputs
            attendance = float(request.form['attendance'])
            study_hours = float(request.form['study_hours'])
            internal_marks = float(request.form['internal_marks'])
            assignments = float(request.form['assignments'])
            
            # Simple validation
            if not (0 <= attendance <= 100):
                error = "Attendance must be between 0 and 100."
            elif study_hours < 0:
                error = "Study hours cannot be negative."
            elif not (0 <= internal_marks <= 100):
                error = "Internal marks must be between 0 and 100."
            elif assignments < 0:
                error = "Assignments cannot be negative."
            else:
                # Predict
                if model:
                    features = np.array([[attendance, study_hours, internal_marks, assignments]])
                    pred = model.predict(features)[0]
                    prediction = round(min(max(pred, 0), 100), 2)
                else:
                    error = "Model is not available."
        except ValueError:
            error = "Please enter valid numeric values."
            
    return render_template('index.html', prediction=prediction, error=error)

if __name__ == '__main__':
    app.run(debug=True)
