import mysql.connector
#create the connection object
myconn=mysql.connector.connect(
    host='localhost',user='root',password='',database='company')
cur=myconn.cursor()
sql='insert into employee(ename,eid,dept,designation,mobile,email,exp,place,salary) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#the row values are provied in the form of tuple
name=input("enter emp name:")
eid=int(input("enter emp id:"))
dept=input("enter dept name:")
designation=input("enter designation:")
mobile=input("enter mobile num:")
email=input("enter ur email:")
exp=int(input("enter exp in years:"))
place=input("enter ur work place:")
salary=float(input("enter ur salary:"))

val=(name,eid,dept,designation,mobile,email,exp,place,salary)
try:
    cur.execute(sql,val)
    myconn.commit()
    print('data inserted')
except Exception as e:
    print('can not process',e)
    myconn.rollback()
print(cur.rowcount,"record inserted")
myconn.close()
