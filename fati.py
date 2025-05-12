import streamlit as st
import pandas as pd
import joblib

st.title("🧠 Application de Détection de Dépression")
st.write("👋 Bienvenue ! Cette application vous aide à identifier les signes de dépression à l'aide de l'apprentissage automatique. Veuillez remplir le formulaire suivant.")

# Formulaire complet avec affichage des choix de l'utilisateur
gender = st.radio('Pick your gender', ['Male', 'Female'])
age=st.number_input('Age', 10, 92)
st.write(age)

profession = st.text_input("Profession")
st.write( profession)

academic_pressure = st.selectbox("Academic Pressure", ["Yes", "No"])
st.write("Pression académique :", academic_pressure)

work_pressure = st.selectbox("Work Pressure", ["Yes", "No"])
st.write("Pression au travail :", work_pressure)
cgpa = st.text_input("CGPA")
st.write("CGPA :", cgpa)
study_satisfaction = st.selectbox("Study Satisfaction", ["Low", "Medium", "High"])
st.write("Satisfaction des études :", study_satisfaction)

job_satisfaction = st.select_slider("Job Satisfaction", ["Low", "Medium", "High"])
st.write("Satisfaction professionnelle :", job_satisfaction)

sleep_duration = st.slider("Sleep Duration (hours)", 0, 12)
st.write("Durée de sommeil :", sleep_duration)

dietary_habits = st.selectbox("Dietary Habits", ["Healthy", "Average", "Unhealthy"])
st.write("Habitudes alimentaires :", dietary_habits)

degree = st.selectbox("Degree", ["Bachelor", "Master", "PhD", "Other"])
st.write("Diplôme :", degree)

suicidal_thoughts = st.selectbox("Have you ever had suicidal thoughts?", ["Yes", "No"])
st.write("Pensées suicidaires :", suicidal_thoughts)

work_study_hours = st.slider("Work/Study Hours", 0, 16)
st.write("Heures de travail/étude :", work_study_hours)

financial_stress = st.selectbox("Financial Stress", ["Yes", "No"])
st.write("Stress financier :", financial_stress)

family_history = st.selectbox("Family History of Mental Illness", ["Yes", "No"])
st.write("Antécédents familiaux :", family_history)
model = joblib.load("bestmodel.joblib")
# Bouton de validation
if st.button("Soumettre"):
    data = {
        "Gender": [gender],
        "Age": [age],
        "Profession": [profession],
        "Academic Pressure": [academic_pressure],
        "Work Pressure": [work_pressure],
        "CGPA": [cgpa],
        "Study Satisfaction": [study_satisfaction],
        "Job Satisfaction": [job_satisfaction],
        "Sleep Duration": [sleep_duration],
        "Dietary Habits": [dietary_habits],
        "Degree": [degree],
        "Have you ever had suicidal thoughts ?": [suicidal_thoughts],
        "Work/Study Hours": [work_study_hours],
        "Financial Stress": [financial_stress],
        "Family History of Mental Illness": [family_history],
        "Depression": ["Unknown"]
    }
    
    df = pd.DataFrame(data)
    st.success("✅ Données soumises avec succès :")
    st.write(df)
import numpy as np

if st.button("Prédire la dépression"):
    # Encodage des variables catégorielles
    gender_num = 0 if gender == "Male" else 1 if gender == "Female" else 2
    academic_pressure_num = 1 if academic_pressure == "Yes" else 0
    work_pressure_num = 1 if work_pressure == "Yes" else 0
    study_satisfaction_num = ["Low", "Medium", "High"].index(study_satisfaction)
    job_satisfaction_num = ["Low", "Medium", "High"].index(job_satisfaction)
    dietary_habits_num = ["Healthy", "Average", "Unhealthy"].index(dietary_habits)
    degree_num = ["Bachelor", "Master", "PhD", "Other"].index(degree)
    suicidal_thoughts_num = 1 if suicidal_thoughts == "Yes" else 0
    financial_stress_num = 1 if financial_stress == "Yes" else 0
    family_history_num = 1 if family_history == "Yes" else 0

    # Créer un tableau avec les données dans le bon ordre
    input_data = np.array([[gender_num, age, academic_pressure_num, work_pressure_num,
                            cgpa, study_satisfaction_num, job_satisfaction_num,
                            sleep_duration, dietary_habits_num, degree_num,
                            suicidal_thoughts_num, work_study_hours,
                            financial_stress_num, family_history_num]])

    # Faire la prédiction
    prediction = model.predict(input_data)[0]

    # Affichage du résultat
    if prediction == 1:
        st.error("⚠️ L'utilisateur montre des signes de dépression.")
    else:
        st.success("✅ L'utilisateur ne montre pas de signes de dépression.")
