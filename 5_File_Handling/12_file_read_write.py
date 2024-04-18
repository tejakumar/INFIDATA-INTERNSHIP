f=open("myfile2.txt",mode='r+')#r+(both read and write program
f.write("hello python\n")
f.write("hello java programming")
f.write("hello web programming")
print("hi")
data1=f.readlines()
print(data1)
print("end")
f.close()