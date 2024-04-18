import mysql.connector
myconn=mysql.connector.connect(
    host="localhost", user="root", passwd="", database="company")
cur=myconn.cursor()
try:
    data=cur.execute("create table employee(ename varchar(30),eid int(4) primary key,dept varchar(20),designation varchar(20),mobile varchar(10),email varchar(20),exp int(3),place varchar(15))")
    print("your table is created successfully")
except Exception as e:
    print("can not process",e)
myconn.close()
