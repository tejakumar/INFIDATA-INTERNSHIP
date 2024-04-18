import streamlit as st
st.header("cost price of bike")
cost_price =st.number_input("Enter the cost price of the bike (in Rs): ",step=10.0)

if cost_price > 100000:
    road_tax = cost_price * 0.15
elif cost_price > 50000:
    road_tax = cost_price * 0.10
else:
    road_tax = cost_price * 0.05

st.write("Road Tax to be paid: Rs", road_tax)