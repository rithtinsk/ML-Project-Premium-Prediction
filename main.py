import streamlit as st
from predict_help import predict

st.title('Health Insurance Cost Predictor')

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', 'other'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}




# Row 1
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input("Age", min_value=18, max_value=100)
with col2:
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
with col3:
    bmi_category = st.selectbox("BMI", categorical_options['BMI Category'])

# Row 2
col4, col5, col6 = st.columns(3)
with col4:
    smoking_status = st.selectbox("Smoking Status", categorical_options['Smoking Status'])
with col5:
    region = st.selectbox("Region", categorical_options['Region'])
with col6:
    number_of_dependants = st.number_input("Number of Dependants", min_value=0, max_value=10, value=0, step=1)

# Row 3
col7, col8, col9 = st.columns(3)
with col7:
    employment_status = st.selectbox("Employment Status", categorical_options['Employment Status'])
with col8:
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
with col9:
    medical_history = st.selectbox("Medical Conditions",categorical_options['Medical History'])

# Row 4
col10, col11, col12 = st.columns(3)
with col10:
    insurance_plan = st.selectbox("Coverage Type", categorical_options['Insurance Plan'])
with col11:
    income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)
with col12:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Coverage Type': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Button to make prediction
if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f'Predicted Health Insurance Cost: {prediction}')
