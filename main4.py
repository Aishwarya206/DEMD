from flask import Flask,render_template,request
import streamlit as st

def praxis():
    st.title("Learning streamlit")
    name = st.text_input("Student_name","Type here")
    num = st.text_input("Roll no","Type here")
    result = ""
    if st.button("Print_result"):
        st.success(f"The Student name is {name} with number {num}")

if __name__ == "__main__":
    praxis()
