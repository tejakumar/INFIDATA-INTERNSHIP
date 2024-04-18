import mysql.connector
myconn=mysql.connector.connect(
    host="localhost", user="root", passwd="", database="infidata")
cur=myconn.cursor()
try:
    data=cur.execute("create table employee(eid int(4) primary key,name varchar(20) not null,email varchar(20))")
    print("your table is created successfully")
except Exception as e:
    print("can not process",e)
myconn.close()
