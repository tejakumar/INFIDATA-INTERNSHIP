l1=[]
for i in range(1,10,2):
    l1.append(i)
print("l1 is:",l1)
num1=[i*i for i in range(5)]
print("num1 is:",num1)
num2=[i*i for i in range(1,10) if i%2==0]
print("num2 is:",num2)
num3=[i**3 for i in range(1,10)]
print("num3 is:",num3)