import datetime
import streamlit as st

st.title("Registration form")

my_form=st.form(key="from-1")

fname=my_form.text_input("firstname:")
lname=my_form.text_input("lastname:")
email=my_form.text_input("email:")

gender=my_form.radio("gender",("male","female"))

age=my_form.slider("age:",1,70)

bday=my_form.date_input("enter birthdate:",min_value=datetime.date(2002,10,9))
address=my_form.text_area("enter address:")
file=my_form.file_uploader("upload ur resume")
submit=my_form.form_submit_button("submit")
st.write('Name is '+fname+'',lname)
st.write('Email is ',email)
st.write('Gender is',gender)
st.write('Age is',age)
st.write('Birthday is',bday)
st.write('Address is',address)
st.success(file)
