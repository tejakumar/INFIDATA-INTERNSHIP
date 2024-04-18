import streamlit as st

st.header("Salary")
salary= st.number_input("Enter your salary: ")
years_of_service = st.number_input("Enter the number of years of service: ")
if years_of_service > 10:
    bonus_percentage = 10
elif years_of_service >= 6:
    bonus_percentage = 8
else:
    bonus_percentage = 5
bonus_amount = (bonus_percentage / 100) * salary

st.write("years of service, your bonus amount is:",bonus_amount )