import mysql.connector
myconn=mysql.connector.connect(
    host="localhost", user="root", passwd="", database="company")
cur=myconn.cursor()
try:
    cur.execute("select*from employee")
    result=cur.fetchall()
    for i in result:
        print(i)
except Exception as e:
    print("can not process:",e)
    myconn.rollback()
myconn.close()
