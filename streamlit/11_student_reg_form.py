import streamlit as st

#Giving a title
st.title('Student Registration Form')

#creating a form
my_form=st.form(key='form-2')

#creating input fields
studentname=my_form.text_input('studentname:')
stu_id=my_form.text_input("Enter the student_id")
email=my_form.text_input('Email:')
branchname=my_form.text_input("Enter  branchname:")
MobileNumber=my_form.text_input('MobileNumber:')
#creating a submit button
Submit=my_form.form_submit_button('submit')
#the following gets updated after clicking on submit,printing the details of the fields that are submitted
st.write('Name is:',studentname)
st.write('student_id is:',stu_id)
st.write('email is:',email)
st.write('branchname is:',branchname)
st.write('MobileNumber is:',MobileNumber)
