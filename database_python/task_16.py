
import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="infidata")
# creating the cursor object
cur = myconn.cursor()
try:
    # Reading the Employee data

    cur.execute("select mobile from employee where mobile like '%___3__'")
    # fetching the rows from the cursor object
    result = cur.fetchall()
    # printing the result
    for i in result:
        print("%s " % (i[0]))

except Exception as e:
    print("cannot process",e)
    myconn.rollback()
myconn.close()
