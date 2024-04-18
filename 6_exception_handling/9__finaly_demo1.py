n1=10
n2=0
try:
    div=n1/n2
    print("res of div:",div)
except IndexError as e:
    print('am at IndexError except block')
    print("e value:",e)
finally:
    print("am at finally block")
    print("executing at finally block")
print("end")