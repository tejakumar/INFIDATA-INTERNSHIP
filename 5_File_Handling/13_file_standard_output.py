import sys
a=int(input("enter a value:"))
b=int(input("enter b value:"))
result=a+b
sys.stdout=open("output1.txt",'w')
print("hello python!")
print("i have a output.")
print("addition result is:",result)


