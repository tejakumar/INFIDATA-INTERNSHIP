f=open("myfile1.txt",mode='r')
data1=f.read(11)
print(data1)

data2=f.read(4)
print(data2)
f.close()