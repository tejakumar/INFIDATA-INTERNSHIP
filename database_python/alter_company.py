import mysql.connector
#create the connection object
myconn=mysql.connector.connect(host="localhost", user="root", passwd="", database="company")
#creating the cursor object
cur=myconn.cursor()
try:
    #adding a column branchname to the table employee
    cur.execute("alter table employee add salary float(20)")
    print("table has been altered")
except Exception as e:
    myconn.rollback()
    print("cannot process",e)
myconn.close()