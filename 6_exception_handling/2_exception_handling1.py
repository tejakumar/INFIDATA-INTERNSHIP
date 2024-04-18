n1=int(input("enter n1 int value"))
n2=int(input("enter n2 int value"))
try:
    div=n1/n2
    print("res of div:",div)
except ZeroDivisionError as e:
    print("urtryingto divide an int num by zero")
    print("e value is:",e)
print("n1 value:",n1)
print("n2 value:",n2)
print("end")