import streamlit as st
import mysql.connector
st.header("employee registration")
# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="",database="college")
# creating the cursor object
cur = myconn.cursor()

st.title("Database Operation")
st.markdown("please give the inputs")

#side bar
st.sidebar.title("Select the operations")
st.sidebar.markdown("Select the options accordingly:")

choice = st.sidebar.selectbox('Select',('INSERT', 'DISPLAY'))
#selected_status = st.sidebar.selectbox('Select number',options=['2N','3N'])
if choice == 'INSERT':

    f_name = st.text_input("Employee First_Name:")
    l_name = st.text_input("Employee Last_Name:")
    emp_id = st.text_input("Employee Id:")
    j_grade = st.text_input("Enter J_Grade")
    dept_id = st.text_input("Enter Dept_Id")
    salary = st.text_input("Enter Salary")
    j_id = st.text_input("Enter J_Id:")
    dept_name = st.text_input("Enter Dept_Name:")
    mobile = st.text_input("Mobile:")
    email = st.text_input("Email")


    def add():
        sql = "insert into demo(f_name,l_name,emp_id,j_grade,dept_id,salary,j_id,dept_name,mobile,email) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"
        # The row values are provided in the form of tuple
        val = (emp_id,f_name,l_name,j_grade,dept_id,salary,j_id,dept_name,mobile,email)
        try:
            # inserting the values into the table
            cur.execute(sql, val)
            myconn.commit()  # commit the transaction
            st.success("data inserted")

        except Exception as e:
            print("can not process", e)
            myconn.rollback()


    def set_state(i):
        st.session_state.stage = i
        st.write("i value is:", i)

    st.info("click a button to proceed:")

    if 'stage' not in st.session_state:
        st.session_state.stage = 0

    if st.session_state.stage == 0:
        st.button('ADD', on_click=set_state, args=[1])

    if st.session_state.stage >= 1:
        add()




elif choice == 'DISPLAY':
    def display():
        try:
            cur.execute("select * from demo")
            # fetching the rows from the cursor object
            result = cur.fetchall()

            st.table(result)

        except Exception as e:
            print("can not process", e)
            myconn.rollback()


    def set_state(i):
        st.session_state.stage = i
        st.write("i value is:", i)


    st.info("click a button to proceed:")

    if 'stage' not in st.session_state:
        st.session_state.stage = 0

    if st.session_state.stage == 0:
        st.button('Display', on_click=set_state, args=[1])

    if st.session_state.stage >= 1:
        display()