import streamlit as st 
import requests as r
nme=[]
regNo=[]
Age=[]
st.header("Registration form")
fullNum=st.text_input("Full Name : ")
fatherName = st.text_input("Father name : ")
motherName = st.text_input("Mother name : ")
age=st.slider("Age(in years) : ",1,100)
gender=st.radio("Gender :",["Male","Female"])
nationality=st.selectbox("Nationality :",["Indian","other"])
email=st.text_input("E-mail : ")
submit=st.button("submit")
if submit==True:
    if len(fullNum)==0 or len(fatherName)==0 or len(motherName)==0 or len(email)==0:
        st.error("Fill all feilds above")
    mail=email
    if mail.find("@")<0:
            st.error("Enter a valid email")
