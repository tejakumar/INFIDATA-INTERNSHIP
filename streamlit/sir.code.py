import streamlit as st
import mysql.connector
# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="",database="infidata")
# creating the cursor object
cur = myconn.cursor()

st.title("Database Operation")


#side bar
st.sidebar.title("Select the operations")
st.sidebar.markdown("Select the options accordingly:")

choice = st.sidebar.selectbox('Select',('INSERT','UPDATE', 'DISPLAY','DELETE'))
#selected_status = st.sidebar.selectbox('Select number',options=['2N','3N'])
if choice == 'INSERT':
    f_name = st.text_input("Employee First_Name:")
    l_name = st.text_input("Employee Last_Name:")
    emp_id = st.number_input("Employee Id:")
    j_grade = st.text_input("Enter J_Grade")
    dept_id = st.number_input("Enter Dept_Id")
    salary = st.number_input("Enter Salary")
    j_id = st.number_input("Enter J_Id:")
    dept_name = st.text_input("Enter Dept_Name:")
    mobile = st.number_input("Mobile:")
    email = st.text_input("Email")

    def add():
        sql = ("insert into employee(f_name,l_name,emp_id,j_grade,dept_id,salary,j_id,dept_name,mobile,email) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

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

elif choice == 'UPDATE':
    def update():
        try:
            cur.execute('update employee set dept_name="iug" where emp_id=20')
            myconn.commit()
            st.write("table has been updated")
        except Exception as e:
            st.write("can not process:", e)
            myconn.rollback()

    def set_state(i):
        st.session_state.stage = i
        st.write("i value is:", i)

    st.info("click a button to proceed:")

    if 'stage' not in st.session_state:
        st.session_state.stage = 0

    if st.session_state.stage == 0:
        st.button('update', on_click=set_state, args=[1])

    if st.session_state.stage >= 1:
        update()

elif choice == 'DISPLAY':
    def display():
        try:
            cur.execute("select * from employee")
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

elif choice == 'delete':
    def delete():
        try:
            st.number_input('enter emp ID to delete:')

            #cur.execute('delete from employee where emp_id=20')
            myconn.commit()
            st.write("employee record has been deleted")

        except Exception as e:
            st.write("can not process:",e)
            myconn.rollback()


    def set_state(i):
        st.session_state.stage = i
        st.write("i value is:", i)

    st.write("click a button to proceed:")

    if 'stage' not in st.session_state:
        st.session_state.stage = 0

    if st.session_state.stage == 0:
        st.button('delete', on_click=set_state, args=[1])

    if st.session_state.stage >= 1:
        delete()