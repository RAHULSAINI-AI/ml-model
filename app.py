import streamlit as st
# import sklearn
from predict_page import show_predict_page

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://png.pngtree.com/background/20210710/original/pngtree-teacher-s-college-classroom-coaching-training-background-picture-image_1034964.jpg");
             background-attachment: fixed;
             background-size: contain;

             font-style: large;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

show_predict_page()
