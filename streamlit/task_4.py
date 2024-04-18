import streamlit as st
st.header("total number of working days")
total_working_days =st.number_input("Enter the total number of working days:")
total_days_absent =st.number_input("Enter the total number of days absent:")

percentage_attended = ((total_working_days - total_days_absent) / total_working_days) * 100

if percentage_attended < 75:
    st.write("Percentage of class attended:", percentage_attended, "%")
    st.write("You are not eligible to take the exams due to low attendance")
else:
    st.write("Percentage of class attended:", percentage_attended,"%")
    st.write("You are eligible to take the exams")