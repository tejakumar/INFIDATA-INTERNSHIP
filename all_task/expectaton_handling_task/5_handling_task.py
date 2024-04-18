a=6.5
try:
    print(a)
except NameError:(
    print("varaiable not defined"))
except ValueError:
    print("the value must be an interger")