f=open('word.txt',mode='r')
data=f.readlines()
count=0
for i in data:
    print(i)
    count=count+1
print("number of lines:",count)
