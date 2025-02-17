import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image


pickle_in = open(r'/content/classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
    return 'Welcome'

def prediction(Age, Diabetes, BloodPressureProblems, AnyTransplants,
       AnyChronicDiseases, Height, Weight, KnownAllergies,
       HistoryOfCancerInFamily, NumberOfMajorSurgeries):
       bmi=Weight/((Height/100)**2)
       obese=int(bmi>30)
       healthyweight=int((bmi>18.5)*(bmi<24.9))
       underweight=int((bmi<18.5))
       overweight=int((bmi>24.9)*(bmi<30))
       riskyperson=int(obese*(NumberOfMajorSurgeries>0)+obese*AnyTransplants+obese*Diabetes
+obese*AnyChronicDiseases+obese*BloodPressureProblems+(NumberOfMajorSurgeries>0)*AnyTransplants+(NumberOfMajorSurgeries>0)*Diabetes+(NumberOfMajorSurgeries>0)*AnyChronicDiseases+(NumberOfMajorSurgeries>0)*BloodPressureProblems+AnyTransplants*Diabetes+AnyTransplants*AnyChronicDiseases*BloodPressureProblems+Diabetes*AnyChronicDiseases+Diabetes*BloodPressureProblems
+AnyChronicDiseases*BloodPressureProblems)
       prediction = classifier.predict(
        [[Age, Diabetes, BloodPressureProblems, AnyTransplants,
       AnyChronicDiseases, Height, Weight, KnownAllergies,
       HistoryOfCancerInFamily, NumberOfMajorSurgeries, bmi, obese, healthyweight, underweight, overweight, riskyperson]])
       print(prediction)
       return prediction



def main():

    st.title("Insurance Premium Price Prediction")


    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Insurance Premium Price Prediction App </h1>
    </div>
    """


    st.markdown(html_temp, unsafe_allow_html = True)


    a = st.number_input("Please enter your age")
    b = st.number_input("Enter 1 if you have diabetes and 0 otherwise")
    c = st.number_input("Enter 1 if you have blood pressure problems and 0 otherwise")
    d = st.number_input("Enter 1 if you have had any transplants and 0 otherwise")
    e = st.number_input("Enter 1 if you have any chronic diseases and 0 otherwise")
    f = st.number_input("Enter your height in centimeters")
    g = st.number_input("Enter your weight in kilograms")
    h = st.number_input("Enter 1 if you have any allergies and 0 otherwise")
    i = st.number_input("Enter 1 if you have a family history of cancer and 0 otherwise")
    j = st.number_input("Enter the number of major surgeries you have undergone")

    result =""


    if st.button("Predict Insurance Premium Price"):
      result = prediction(a,b,c,d,e,f,g,h,i,j)
    st.success('The Insurance Premium Price is Rs.{}'.format(result))

if __name__=='__main__':
    main()