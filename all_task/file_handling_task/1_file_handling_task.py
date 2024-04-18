f=open('myfile01.txt',mode='w')
f.write('hello python')
print('total no.of words in text file:',f.tell())
f.close()