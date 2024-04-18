value=10
def disp(s):
    global value
    value=5
    if s%7==0:
        value=value+s
    else:
        value=value-s
    print(value,end="?")
disp(49)
print(value)