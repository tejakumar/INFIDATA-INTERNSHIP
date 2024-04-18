import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor=mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE  infidata")
    print("database created successfully")
except Exception as e:
  print("can not process:",e)


