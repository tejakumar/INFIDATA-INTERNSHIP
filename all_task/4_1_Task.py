print("enter 3 num:")
a=int(input("enter a num"))
b=int(input("enter a num"))
c=int(input("enter a num"))
def max(n1,n2,n3):
    if(n1>=n2)and(n2>=n3):
        largest=n1
    elif(n1>=n2)and(n2>=n3):
        largest=n2
    else:
        largest=n3
    return largest
print("max number is:",max(a,b,c))
