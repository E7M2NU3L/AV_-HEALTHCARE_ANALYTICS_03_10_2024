import streamlit as st

test_input_columns = ['Hospital_code', 'Hospital_type_code', 'City_Code_Hospital',
       'Hospital_region_code', 'Available Extra Rooms in Hospital',
       'Department', 'Ward_Type', 'Ward_Facility_Code', 'City_Code_Patient', 'Type of Admission',
       'Bed Grade', 'Visitors with Patient', 'Age',
       'Admission_Deposit']

st.title("AV Healthcare Analysis - Feb 2025")
st.write("Patient Severity Predictor Model")

with st.form(key="patient_analyser"):
    inputs = []
    for columns in test_input_columns:
        value = st.number_input(columns)
        inputs.append(value)

    submit_button = st.form_submit_button(label="Predict")