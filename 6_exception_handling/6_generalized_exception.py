l1=[2,3,4,5]
try:
    print("list element is:",l1[4])
except ZeroDivisionError as e:
    print("ur trying to divide an int num by zero")
    print("e value is:",e)
except IndexError as e:
    print("u are trying to accept out of range index")
    print("e value:",e)
except Exception as e:
    print("i am at generaised exception block")
    print("e value:",e)
print("end")