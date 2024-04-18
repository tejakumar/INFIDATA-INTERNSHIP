import mysql.connector
myconn=mysql.connector.connect(
    host="localhost", user="root", passwd="", database="infidata")
cur=myconn.cursor()
try:
    # Reading the Employee data
    cur.execute("select dept_id,dept_name from employee where dept_id not between 100 and 110")

    # fetching the rows from the cursor object
    result = cur.fetchall()
    # printing the result
    for x in result:
        print("%d %s" %(x[0],x[1]))
except Exception as e:
    print("can not process",e)