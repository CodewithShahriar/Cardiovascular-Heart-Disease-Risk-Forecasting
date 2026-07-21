
import streamlit as st
import pandas as pd
import joblib

model = joblib.load('heart_model.pkl')

st.title("Cardiovascular Heart Disease Prediction System")
st.write("Check the patient's heart status using clinical data.")

age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", options=[1, 0], format_func=lambda x: "Male" if x==1 else "Female")
cp = st.selectbox("Chest Pain Type (0-3)", options=[0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", min_value=50, max_value=250, value=120)
chol = st.number_input("Serum Cholestoral in mg/dl", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[1, 0], format_func=lambda x: "True" if x==1 else "False")
restecg = st.selectbox("Resting Electrocardiographic Results (0-2)", options=[0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=250, value=150)
exang = st.selectbox("Exercise Induced Angina", options=[1, 0], format_func=lambda x: "Yes" if x==1 else "No")
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox("Slope of the Peak Exercise ST Segment (0-2)", options=[0, 1, 2])
ca = st.selectbox("Number of Major Vessels Coloured by Flourosopy (0-4)", options=[0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (0-3)", options=[0, 1, 2, 3])

if st.button("Predict Heart Health"):
    input_data = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    input_df = pd.DataFrame([input_data], columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])
    prediction = model.predict(input_df)
    
    if prediction[0] == 0:
        st.success('The patient is unlikely to have heart disease.')
    else:
        st.error('Warning: The patient shows symptoms of heart disease!')
