import mysql.connector
#create the connection object
myconn=mysql.connector.connect(host="localhost", user="root", passwd="", database="college")
#creating the cursor object
cur=myconn.cursor()
try:
    #adding a column branchname to the table employee
    cur.execute("alter table student add mobile varchar(20) not null")
    print("table has been altered")
except Exception as e:
    myconn.rollback()
    print("cannot process",e)
myconn.close()