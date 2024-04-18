import mysql.connector
myconn=mysql.connector.connect(
    host="localhost", user="root", passwd="", database="infidata")
cur=myconn.cursor()
try:
    cur.execute('select f_name,l_name,emp_id,j_grade,dept_id,salary from employee where emp_id=200')
    result=cur.fetchall()
    print("f_name,l_name,emp_id,j_grade,dept_id,salary")
    print("___________________________")
    for i in result:
        print("%s %s %s %s %s %f"%(i[0],i[1],i[2],i[3],i[4],i[5]))
except Exception as e:
    print(" can not process:",e)