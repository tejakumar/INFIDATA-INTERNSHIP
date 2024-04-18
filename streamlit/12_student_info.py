import streamlit as st
st.header("Employee Registration")
f_name=st.text_input("employee f_name:")
l_name=st.text_input("employee l_name:")
emp_id=st.text_input("emp_id:")
j_grade=st.text_input("j_grade:")
dept_id=st.text_input("dept_id:")
salary=st.text_input(" salary")
j_id=st.text_input(" j_id:")
dept_name=st.text_input("dept_id:")
mobile=st.text_input("employee Mobile:")
email=st.text_input("employee email")

def insert():
    import mysql.connector
    # Create the connection object
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="infidata")
    # creating the cursor object
    cur = myconn.cursor()

    sql = "insert into employee(f_name,l_name,emp_id,j_grade,dept_id,salary,j_id,dept_name,mobile,email) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # The row values are provided in the form of tuple
    val = (f_name,l_name,emp_id,j_grade,dept_id,salary,j_id,dept_name,mobile,email)
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