import streamlit as st
import pandas as pd
import pickle
pickle_in = open('rfc2.pkl', 'rb')
myclassifier = pickle.load(pickle_in)

st.header("Diabetes Predictor")
name = st.text_input("Name:")
pregnancy = st.number_input("No. of times pregnant:")
glucose = st.number_input("Plasma Glucose Concentration :")
bp =  st.number_input("Diastolic blood pressure (mm Hg):")
skin = st.number_input("Triceps skin fold thickness (mm):")
insulin = st.number_input("2-Hour serum insulin (mu U/ml):")
bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):")
dpf = st.number_input("Diabetes Pedigree Function:")
age = st.number_input("Age:")



   
if st.button("Submit"):
    prediction = myclassifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
    if prediction == 0:
        st.write('Congratulation',name,'You donot have diabetes')
    else:
        st.write(name,"  sorry  you are diabetic ")
    