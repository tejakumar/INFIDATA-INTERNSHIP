import streamlit as st

# Initialize an empty dictionary to store employee data
employee_data = {}

# Streamlit UI for Employee Registration
st.title("Employee Registration System")

employee_name = st.text_input("Name")
employee_id = st.text_input("Employee ID")
employee_email = st.text_input("Email")

if st.button("Register"):
    if employee_id in employee_data:
        st.error("Employee ID already exists. Use Update option to modify.")
    else:
        employee_data[employee_id] = {"name": employee_name, "email": employee_email}
        st.success("Employee registered successfully.")

# Streamlit UI for Employee Update
st.subheader("Update Employee Information")

update_id = st.text_input("Employee ID to Update")
if st.button("Update"):
    if update_id in employee_data:
        new_name = st.text_input("New Name")
        new_email = st.text_input("New Email")
        employee_data[update_id]["name"] = new_name
        employee_data[update_id]["email"] = new_email
        st.success("Employee information updated successfully.")
    else:
        st.error("Employee ID not found.")

# Streamlit UI for Displaying Employee Information
st.subheader("Display Employee Information")

display_id = st.text_input("Employee ID to Display")
if st.button("Display"):
    if display_id in employee_data:
        employee = employee_data[display_id]
        st.write(f"Employee Name: {employee['name']}")
        st.write(f"Employee Email: {employee['email']}")
    else:
        st.error("Employee ID not found.")

# Streamlit UI for Deleting Employee Information
st.subheader("Delete Employee Information")

delete_id = st.text_input("Employee ID to Delete")
if st.button("Delete"):
    if delete_id in employee_data:
        del employee_data[delete_id]
        st.success("Employee information deleted successfully.")
    else:
        st.error("Employee ID not found.")