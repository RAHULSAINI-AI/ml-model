import streamlit as st
import pickle
import sklearn
import numpy as np

def load_model():
    with open('model_pkl' , 'rb') as f:
        lr = pickle.load(f)
    return lr

lr = load_model()

def show_predict_page():
    st.title("Indian Institute of Management, Gurugram")
    st.write("""#### Wants to get into India's top Buisness School...   """)
    st.write("## Admission Predictor ")

    gre = st.slider("GRE Score", 260, 340,295)
    toefl = st.slider("TOEFL Score", 0, 120, 100)
    uni_rate = st.selectbox("University Rating", [1,2,3,4,5],2)
    sop = st.selectbox("Statement of Purpose -(SOP) Strength", [1,2,3,4,5],3)
    lor = st.selectbox("Letter of Recommendation-(LOR) Strength",[1,2,3,4,5], 3)
    cgpa = st.slider("Undergraduate CGPA", 6.0, 10.0, 8.0, 0.01)
    res_exp = st.radio("Research Experience", ['YES' ,'NO'],1 )
    research = 1 if res_exp == 'YES' else 0
    
    ok = st.button("Calculate")
    if ok:
        X = [[gre, toefl, uni_rate, sop,lor, cgpa, research]]
        
        chance = lr.predict(X)
        st.sidebar.subheader(f"The probability of getting admission is {chance}")
