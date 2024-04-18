import streamlit as st
st.header("temperature")
temp =st.number_input("Enter the temperature in Celsius: ",step=10)
if temp < 0:
    st.info("Freezing weather")
elif temp < 10:
    st.info("Very Cold weather")
elif temp < 20:
    st.info("Cold weather")
elif temp < 30:
    st.info("Normal in Temp")
elif temp < 40:
    st.info("It's Hot")
else:
    st.info("It's Very Hot")