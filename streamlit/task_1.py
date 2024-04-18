import streamlit as st
st.header("electricity bill")
customer_name =st.text_input ("Enter customer name: ")
customer_id =st.number_input("Enter customer id:")
units = st.number_input("Enter the number of units: ")

if units <= 100:
    total_bill = 0
elif units <= 200:
    total_bill = (units - 100) * 5
else:
    total_bill = 100 * 5 + (units - 200) * 10

st.write("Customer Name:", customer_name)
st.write("Customer ID:", customer_id)

st.write("Electricity Bill: Rs", total_bill)
