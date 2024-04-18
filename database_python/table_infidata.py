import mysql.connector
myconn=mysql.connector.connect(
    host="localhost", user="root", passwd="", database="infidata")
cur=myconn.cursor()
try:
    data=cur.execute("create table employee1(f_name varchar(30),l_name varchar(30),emp_id int(4) primary key,j_grade varchar(30),dept_id varchar(20),salary int(5),j_id varchar(30),dept_name varchar(30),mobile varchar(10),email varchar(20))")
    print("your table is created successfully")
except Exception as e:
    print("can not process",e)
myconn.close()
