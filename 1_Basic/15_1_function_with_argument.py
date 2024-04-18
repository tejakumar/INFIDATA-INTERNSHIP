print("function with argument")
n1=int(input("enter n1"))
n2=int(input("enter n2"))
def add(a,b):     #function definition
    result = a+b
    print("add of {0} & {1} is {2}".format(n1,n2,result))
def mul(a,b):
    result = a*b
    print("mul of {0} & {1} is {2}".format(n1,n2,result))
print("function program")
add(n1,n2)  #calling function
print("end of the program")