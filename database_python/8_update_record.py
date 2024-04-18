import mysql.connector
myconn=mysql.connector.connect(
    host="localhost", user="root", passwd="", database="company")
cur=myconn.cursor()
try:
    cur.execute('update employee set designation="manager" where eid=123')
    myconn.commit()
    print("table has been updated")
except Exception as e:
    print("can not process:",e)
    myconn.rollback()
myconn.close()