import mysql.connector
myconn=mysql.connector.connect(
    host="localhost", user="root", passwd="", database="company")
cur=myconn.cursor()
try:
    cur.execute('select ename,eid,designation,salary from employee where eid=123')
    result=cur.fetchall()
    print("name id designation salary")
    print("___________________________")
    for i in result:
        print("%s,%d,%s,%f"%(i[0],i[1],i[2],i[3]))
except Exception as e:
    print(" can not process:",e)