print("function with no argument")
n1=int(input("enter n1"))
n2=int(input("enter n2"))
def add():     #function definition
    result = n1+n2
    print("add of {0} & {1} is {2}".format(n1,n2,result))
def mul():
    result = n1*n2
    print("mul of {0} & {1} is {2}".format(n1,n2,result))
print("function program")
add()  #calling function
print("end of the program")