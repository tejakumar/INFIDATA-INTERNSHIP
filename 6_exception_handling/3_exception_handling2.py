list1=[1,2,3]
try:
    print("list element is:",list1[2])
    print("list element is:",list1[3])

except IndexError as y:
    print("the above index is out of range")
    print("y value is:",y)
print('end')