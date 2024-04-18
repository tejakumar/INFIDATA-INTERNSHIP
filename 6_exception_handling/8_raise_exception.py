try:
    raise IndexError("demo through raise keyword")
except IndexError as e:
    print("am an index error")#explicit call to except block
    print("e value:",e)
print("end")