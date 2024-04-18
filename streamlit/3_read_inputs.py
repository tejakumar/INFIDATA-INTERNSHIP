 import streamlit as st
st.header("read inputs")

n1=st.number_input("enter n1 int value(between 10 and 30):",min_value=10,max_value=30)
n2=st.number_input("enter n2 int value:")

if(n1>n2):
    st.info("n1 is greater:")
else:
    st.info("n2 is greater:")