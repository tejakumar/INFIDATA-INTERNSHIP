f=open("hobby.txt",mode='w')
list=[]
for i in range(5):
    data=input("enter ur hobby:")
    list.append(data)
    list.append('\n')
f.writelines(list)
f.close()
