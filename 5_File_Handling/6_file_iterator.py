f=open("myfile1.txt",mode='r')
for i in f:
    data=i.split()
    print(data)
    print("values type is:",type(data))
f.close()