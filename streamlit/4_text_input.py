import streamlit as st
st.header("read inputs")

n1=st.number_input("enter n1 int value(between 10 and 300):",min_value=1,max_value=300,step=10)
n2=st.number_input("enter n2 int value:",step=10)

sum=n1+n2


st.write("Sum of 2 Numbers:")
st.success(sum)