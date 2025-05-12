import streamlit as st
import pandas as pd
import joblib
import numpy as np
import streamlit as st

# CSS button style
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1503676260728-1c00da094a0b");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }

    .stButton > button {
        background-color: #ff69b4;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        padding: 10px 24px;
        transition: 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #ff85c1;
        transform: scale(1.05);
    }

    .block-container {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 20px;
    }

    h1, p, label {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)


st.title("🧠 Application de Détection de Dépression")
st.write("👋 Bienvenue ! Cette application vous aide à identifier les signes de dépression à l'aide de l'apprentissage automatique. Veuillez remplir le formulaire suivant.")

# Form inputs
gender = st.radio('Pick your gender', ['Male', 'Female'])
age = st.number_input('Age', 10, 92)
profession = st.selectbox("Profession",["Student","Architect","Teacher","Digital Marketer","Content Writer","Chef","Doctor","Pharmacist","Civil Engineer" ,"UX/UI Designer","Educational Consultant","Manager","Lawyer","Entrepreneur"])

academic_pressure = st.selectbox("Academic Pressure", ["Yes", "No"])
work_pressure = st.selectbox("Work Pressure", ["Yes", "No"])
cgpa = st.number_input("CGPA", min_value=0.0, max_value=4.0, step=0.01)

study_satisfaction = st.selectbox("Study Satisfaction", ["Low", "Medium", "High"])
job_satisfaction = st.radio("Job Satisfaction", ["Low", "Medium", "High"])
sleep_duration = st.slider("Sleep Duration (hours)", 0, 12)
dietary_habits = st.selectbox("Dietary Habits", ["Healthy", "Average", "Unhealthy"])
degree = st.selectbox("Degree", ["Bachelor", "Master", "PhD", "Other"])
suicidal_thoughts = st.selectbox("Have you ever had suicidal thoughts?", ["Yes", "No"])
work_study_hours = st.slider("Work/Study Hours", 0, 16)
financial_stress = st.selectbox("Financial Stress", ["Yes", "No"])
family_history = st.selectbox("Family History of Mental Illness", ["Yes", "No"])

model = joblib.load("bestmodel.joblib")

# Validation des entrées
if st.button("Soumettre"):
    try:
        cgpa_int =int(cgpa)

        # Encodage
        gender_num = 0 if gender == "Male" else 1
        age_num = age  # c'est déjà un entier
        profession_num = ["Student","Architect","Teacher","Digital Marketer","Content Writer","Chef",
                  "Doctor","Pharmacist","Civil Engineer","UX/UI Designer",
                  "Educational Consultant","Manager","Lawyer","Entrepreneur"].index(profession)

        gender_num = 0 if gender == "Male" else 1
        academic_pressure_num = 1 if academic_pressure == "Yes" else 0
        work_pressure_num = 1 if work_pressure == "Yes" else 0
        study_satisfaction_num = ["Low", "Medium", "High"].index(study_satisfaction)
        job_satisfaction_num = ["Low", "Medium", "High"].index(job_satisfaction)
        dietary_habits_num = ["Healthy", "Average", "Unhealthy"].index(dietary_habits)
        degree_num = ["Bachelor", "Master", "PhD", "Other"].index(degree)
        suicidal_thoughts_num = 1 if suicidal_thoughts == "Yes" else 0
        financial_stress_num = 1 if financial_stress == "Yes" else 0
        family_history_num = 1 if family_history == "Yes" else 0

        # Arrange input data in correct order
        input_data = np.array([[gender_num, age_num, profession_num,
                        academic_pressure_num, work_pressure_num, cgpa,
                        study_satisfaction_num, job_satisfaction_num, sleep_duration,
                        dietary_habits_num, degree_num, suicidal_thoughts_num,
                        work_study_hours, financial_stress_num, family_history_num]])
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.error("⚠️ L'utilisateur montre des signes de dépression.")
        else:
            st.success("✅ L'utilisateur ne montre pas de signes de dépression.")
    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")