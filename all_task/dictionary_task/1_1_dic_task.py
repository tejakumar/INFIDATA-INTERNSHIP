d1={1:10,2:20,3:30,4:40}
key=int(input("enter a key to search:"))
if key in d1:
    print("the key",key,"exists in d1")
else:
    print("the key",key,"not exists in d1")