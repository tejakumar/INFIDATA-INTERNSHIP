import mysql.connector

myconn = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="infidata")
cur = myconn.cursor()
try:
    # Reading the Employee data
    cur.execute("select emp_id ,f_name,j_id,j_grade,salary from employee where j_grade!='developer'")

    # fetching the rows from the cursor object
    result = cur.fetchall()
    # printing the result
    for x in result:
        print("%d  %s  %s  %s %d" %(x[0],x[1],x[2],x[3],x[4]))
except Exception as e:
    print("can not process",e)