import streamlit as st
st.header("grade")
percentage =st.number_input("Enter the percentage:",step=10.0)

if percentage > 90:
    grade = 'A'
elif percentage > 80:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
else:
    grade = 'D'

st.write("Grade:", grade)