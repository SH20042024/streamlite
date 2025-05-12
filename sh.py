from flask import Flask, render_template, request,flash
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('bestmodel.joblib')

# Mapping dictionaries (نفس اللي درّبتي بيهم النموذج)
gender_map = {"Male": 1, "Female": 0}
yes_no_map = {"Yes": 1, "No": 0}
satisfaction_map = {"Low": 0, "Medium": 1, "High": 2}
diet_map = {"Healthy": 0, "Average": 1, "Unhealthy": 2}
degree_map = {"Bachelor": 0, "Master": 1, "PhD": 2, "Other": 3}
profession_map = {
    "Student": 0, "Architect": 1, "Teacher": 2, "Digital Marketer": 3,
    "Content Writer": 4, "Chef": 5, "Doctor": 6, "Pharmacist": 7,
    "Civil Engineer": 8, "UX/UI Designer": 9, "Educational Consultant": 10,
    "Manager": 11, "Lawyer": 12, "Entrepreneur": 13
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form

    # Convert form inputs to numerical values using mapping
    gender = gender_map[data['gender']]
    age = int(data['age'])
    profession = profession_map[data['profession']]
    academic_pressure = yes_no_map[data['academic_pressure']]
    work_pressure = yes_no_map[data['work_pressure']]
    cgpa = float(data['cgpa'])
    study_satisfaction = satisfaction_map[data['study_satisfaction']]
    job_satisfaction = satisfaction_map[data['job_satisfaction']]
    sleep_duration = float(data['sleep_duration'])
    dietary_habits = diet_map[data['dietary_habits']]
    degree = degree_map[data['degree']]
    suicidal_thoughts = yes_no_map[data['suicidal_thoughts']]
    work_study_hours = float(data['work_study_hours'])
    financial_stress = yes_no_map[data['financial_stress']]
    family_history = yes_no_map[data['family_history']]

    # Feature array for prediction
    features = np.array([[gender, age, profession,
                          academic_pressure, work_pressure, cgpa,
                          study_satisfaction, job_satisfaction, sleep_duration,
                          dietary_habits, degree, suicidal_thoughts,
                          work_study_hours, financial_stress, family_history]])

    prediction = model.predict(features)[0]

    if prediction == 1:
      result_text = "⚠️ L'utilisateur montre des signes de dépression."
      quran_verse = "﴿ ألا بذكر الله تطمئن القلوب ﴾ — [الرعد:28]"
      alert_type = "error"
    else:
       result_text = "✅ L'utilisateur ne montre pas de signes de dépression."
       quran_verse = ""
       alert_type = "success"

    return render_template('result.html', prediction_text=result_text, quran_verse=quran_verse, alert_type=alert_type)
if __name__ == '__main__':
    app.secret_key = 'clé_secrète'
    app.run(debug=True)

