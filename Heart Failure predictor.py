import streamlit as st
import pandas as pd
import pickle
pickle_in = open('rfc3.pkl', 'rb')
myclassifier = pickle.load(pickle_in)

st.header("Heart Failure predictor")
    
name = st.text_input("Name:")
age = st.number_input("Age:")
sex=st.number_input("Enter your sex 1=M 0=F")
cp=st.number_input("Chest pain type ATA=1 NAP=2  ASY=0")
RBP = st.number_input("Resting Bp")
CHOL = st.number_input("Cholestrol:")
FB =  st.number_input("Fastingbs:")
REK = st.number_input("Resting Ekg Normal=1 , ST=2 ,LVH=0")
MHR = st.number_input("MaxHr:")
EA = st.number_input("Exercise Angina: N0=0 Yes=1")
OLD = st.number_input("oldpeak:")
ST = st.number_input("ST slope: FLAT=1 up=2" )
    


if st.button("Submit"):
    prediction = myclassifier.predict([[age, sex, cp, RBP, CHOL, FB, REK, MHR,EA,OLD,ST]])
    if prediction == 0:
        st.write('Congratulation',name,'You are not having to heart failure')
    else:
        st.write(name,"sorry but it seems like you are having heart failure.")
