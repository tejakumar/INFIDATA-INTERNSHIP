import mysql.connector
myconn=mysql.connector.connect(
    host="localhost", user="root", passwd="", database="infidata")
cur=myconn.cursor()
try:
    # Reading the Employee data
    cur.execute("select f_name,emp_id,salary from employee where salary in(18000,20000,30000,25000)")

    # fetching the rows from the cursor object
    result = cur.fetchall()
    # printing the result
    for x in result:
        print("%s %d %d" %(x[0],x[1],x[2]))
except Exception as e:
    print("can not process",e)