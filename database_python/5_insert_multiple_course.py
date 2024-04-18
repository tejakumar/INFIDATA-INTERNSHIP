import mysql.connector
#create the connection object
myconn=mysql.connector.connect(
    host='localhost',user='root',password='',database='collage')
cur=myconn.cursor()
sql='insert into student(name,id,branch,mobile) values(%s,%s,%s,%s)'
#the row values are provied in the form of tuple
val=[('mohan',124,'ece','345256'),('manu',123,'cse','4653575677'),('hari',324,'ece','33454646')]
try:
    cur.executemany(sql,val)
    myconn.commit()
    print(cur.rowcount,'record inserted')
except Exception as e:
    print('can not process',e)
    myconn.rollback()
myconn.close()
