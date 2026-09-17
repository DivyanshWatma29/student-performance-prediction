import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(page_title="Student Performance Prediction", page_icon="??")

st.title("Student Performance Prediction ??")
st.write("Enter the student's academic details below to predict their final score.")

# Load the trained model
@st.cache_resource
def load_model():
    try:
        with open('model.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

model = load_model()

if model is None:
    st.error("Error: Trained model not found. Please run 'train_model.py' to generate 'model.pkl'.")
else:
    # Input forms
    col1, col2 = st.columns(2)
    
    with col1:
        attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0, value=85.0, step=1.0)
        study_hours = st.number_input("Study Hours (per week)", min_value=0.0, max_value=168.0, value=3.0, step=0.5)
        
    with col2:
        internal_marks = st.number_input("Internal Marks (out of 100)", min_value=0.0, max_value=100.0, value=70.0, step=1.0)
        assignments = st.number_input("Assignments Completed", min_value=0, max_value=50, value=8, step=1)
        
    if st.button("Predict Score", type="primary"):
        # Prediction
        features = np.array([[attendance, study_hours, internal_marks, assignments]])
        pred = model.predict(features)[0]
        
        # Clip score between 0 and 100
        final_score = min(max(pred, 0), 100)
        
        st.success(f"### Predicted Final Marks: **{final_score:.2f}** / 100")
        
    st.markdown("---")
    st.caption("Model used: **Linear Regression**")
