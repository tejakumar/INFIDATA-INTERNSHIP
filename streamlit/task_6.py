import streamlit as st
st.header("number of days worked")
age =st.number_input("Enter your age: ")
gender =st.text_input("Enter your gender (M/F): ")
days_worked =st.number_input("Enter the number of days worked: ",step=30.0)

wages = 0

if age >= 18 and age < 30:
    if gender == 'M':
        wages = days_worked * 700
    elif gender == 'F':
        wages = days_worked * 750
elif age >= 30 and age <= 40:
    if gender == 'M':
        wages = days_worked * 800
    elif gender == 'F':
        wages = days_worked * 850

st.write("Wages earned: Rs", wages)