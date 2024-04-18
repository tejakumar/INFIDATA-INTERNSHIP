l1=[2,3,4,5]
n1=int(input("enter n1 int value"))
n2=int(input("enter n2 int value"))
try:
    div=n1/n2
    print("div of{0} and {1} is {2}:".format(n1,n2,div))
    print("list element is:",l1[4])
except ZeroDivisionError as e:
    print("ur trying to divide an int num by zero")
    print("e value is:",e)
except IndexError as e:
    print("the above index is out of range")
    print("e value is:",e)
print('end')