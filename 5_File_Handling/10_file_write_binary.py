l1=[61,62,63,64,66,67,91,92,93]
data=bytearray(l1)
f=open("myfile2.txt",mode='wb')
f.write(data)
f.close()
#data=f.read()