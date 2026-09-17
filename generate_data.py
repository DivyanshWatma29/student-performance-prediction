import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

attendance = np.random.randint(50, 101, n)
study_hours = np.random.randint(1, 15, n)
internal_marks = np.random.randint(30, 101, n)
assignments = np.random.randint(0, 11, n)

# Generate final marks with some noise
final_marks = (
    0.3 * attendance + 
    1.5 * study_hours + 
    0.4 * internal_marks + 
    2 * assignments + 
    np.random.normal(0, 3, n)
)

final_marks = np.clip(final_marks, 0, 100)

df = pd.DataFrame({
    'attendance': attendance,
    'study_hours': study_hours,
    'internal_marks': internal_marks,
    'assignments': assignments,
    'final_marks': np.round(final_marks, 2)
})

df.to_csv('student_data.csv', index=False)
print('Generated student_data.csv')
