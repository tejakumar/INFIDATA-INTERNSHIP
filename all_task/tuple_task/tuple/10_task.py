student=tuple()
global rollnum,name,branch
for i in range(3):
     rollnum=input("enter rollnum for student{}:".format(i+1))
     name=input("enter name for student{}:".format(i+1))
     branch=input("enter branch for student{}:".format(i+1))
student_details=(rollnum,name,branch)
print("student details stored in tuple:",student)



