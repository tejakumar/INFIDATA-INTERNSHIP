import mysql.connector
myconn=mysql.connector.connect(
    host="localhost", user="root", passwd="", database="company")
cur=myconn.cursor()
try:
    cur.execute('delete from employee  where eid=12345')
    myconn.commit()
    print("employee record has been deleted")
except Exception as e:
    print("can not process:",e)
    myconn.rollback()
myconn.close()