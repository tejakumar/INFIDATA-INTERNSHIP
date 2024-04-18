import mysql.connector
myconn=mysql.connector.connect(
    host="localhost", user="root", passwd="", database="infidata")
cur=myconn.cursor()
try:
    # Reading the Employee data
    cur.execute("select f_name,l_name from employee where f_name like 'A%'")

    # fetching the rows from the cursor object
    result = cur.fetchall()
    # printing the result
    for x in result:
        print("%s %s" %(x[0],x[1]))
except Exception as e:
    print("can not process",e)