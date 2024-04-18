f=open("myfile1.txt",mode='r')
data1=f.read(1)
print(data1)

data2=f.read(2)
print(data2)

print("current file position:",f.tell())#get the current file cursor position

f.seek(6) #bring file cursor to specified position
print(f.read(2))

f.close()