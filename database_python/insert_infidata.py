import mysql.connector
#create the connection object
myconn=mysql.connector.connect(
    host='localhost',user='root',password='',database='infidata')
cur=myconn.cursor()
sql='insert into employee(f_name,l_name,emp_id,j_grade,dept_id,salary,j_id,dept_name,mobile,email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#the row values are provied in the form of tuple
f_name=input("enter emp f_name:")
l_name=input("enter emp l_name:")
emp_id=int(input("enter emp_id:"))
j_grade=input("enter emp j_grade:")
dept_id=int(input("enter dept_id:"))
salary=int(input("enter ur salary:"))
j_id=input("enter j_id")
dept_name=input("enter dept_name")
mobile=input("enter mobile num:")
email=input("enter ur email:")

val=(f_name,l_name,emp_id,j_grade,dept_id,salary,j_id,dept_name,mobile,email)
try:
    cur.execute(sql,val)
    myconn.commit()
    print('data inserted')
except Exception as e:
    print('can not process',e)
    myconn.rollback()
print(cur.rowcount,"record inserted")
myconn.close()
