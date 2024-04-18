import streamlit as st
st.header("Employee Registration")
f_name=st.text_input("Employee First_Name:")
l_name=st.text_input("Employee Last_Name:")
emp_id=st.text_input("Employee Id:")
j_grade=st.text_input("Enter J_Grade")
dept_id=st.text_input("Enter Dept_Id")
salary=st.text_input("Enter Salary")
j_id=st.text_input("Enter J_Id:")
dept_name=st.text_input("Enter Dept_Name:")
mobile=st.text_input("Mobile:")
email=st.text_input("Email")


def insert():
    import mysql.connector
    # Create the connection object
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="infidata")
    # creating the cursor object
    cur = myconn.cursor()

    sql = "insert into employee(f_name,l_name,emp_id,j_grade,dept_id,salary,j_id,dept_name,mobile,email) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # The row values are provided in the form of tuple
    val = (emp_id,f_name,l_name,j_grade,dept_id,salary,j_id,dept_name,mobile,email)
    try:
        # inserting the values into the table
        cur.execute(sql, val)
        myconn.commit()
        st.success("Registration Successful")
        st.write(cur.rowcount, "record inserted!")
    except Exception as e:
        print("can not process:", e)
        myconn.rollback()

    myconn.close()
def set_state(i):
    st.session_state.stage = i
    st.write("i value is:",i)

if 'stage' not in st.session_state:
    st.session_state.stage = 0

if st.session_state.stage == 0:
    st.button('SUBMIT', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    insert()