l1=[2,3,4,5]
n1=int(input("enter n1 int value"))
n2=int(input("enter n2 int value"))
try:
    div=n1/n2
    print("result of is:",l1[4])
except Exception as e:
    print("i am at generaised exception block")
    print("e value:",e)
print("end")