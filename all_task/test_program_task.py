def read():
    global name,id,branch,age
    name=input('enter student name:')
    id=int(input('enter student id:'))
    branch=input('enter student branch:')
    age=int(input('enter student age:'))

def avg():
    test1=int(input('enter your test1 marks:'))
    test2=int(input('enter your test2 marks:'))
    test3=int(input('enter your test3 marks:'))
    avg=test1+test2+test3/3
    print('the average is:',avg)
def display():
    print("student name:",name)
    print("student id:",id)
    print("student branch:",branch)
    print("student age:",age)
read()
avg()








