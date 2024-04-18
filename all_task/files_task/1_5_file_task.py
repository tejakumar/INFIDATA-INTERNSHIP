l1=[12,23,34,45,56,67]
f=open('list.txt',mode='w')
for item in l1:
    f.write(str(item)+'\n')
f.close()