print("funtion with arbitrary argument")
def add(*n):#n[0]=3,n[1]=4,n[2]=5
    sum=n[0]+n[1]+n[2]
    print("sum of all number:",sum)
add(3,4,5)