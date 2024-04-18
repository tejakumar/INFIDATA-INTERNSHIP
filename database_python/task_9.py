import mysql.connector
myconn=mysql.connector.connect(
    host="localhost", user="root", passwd="", database="infidata")
cur=myconn.cursor()
try:
    # Reading the Employee data
    cur.execute("select f_name,j_grade,salary from employee where salary between 20000 and 40000")

    # fetching the rows from the cursor object
    result = cur.fetchall()
    # printing the result
    for x in result:
        print("%s %s %d" %(x[0],x[1],x[2]))
except Exception as e:
    print("can not process",e)
