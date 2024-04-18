import mysql.connector
#create the connection object
myconn=mysql.connector.connect(host="localhost", user="root", password="", database="college")
#creating the cursor object
cur=myconn.cursor()
sql="insert into student(name,id,branch,mobile) values (%s,%s,%s,%s)"
#the row values are provided in the form of tuple
val=("mahesh",201,"ece","9377737387")
try:
    #inserting the values into the table
    cur.execute(sql,val)
    myconn.commit()
    print("data inserted")           #commit the transcation
except Exception as e:
    print("can not process",e)
    myconn.rollback()
myconn.close()