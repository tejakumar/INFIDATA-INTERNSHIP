a,b=5,0
try:
    div=a/b
    print("res is div:",div)
except ZeroDivisionError:
    print("hello")
except SyntaxError:
    print("hii")
except ValueError:
    print("okey")
else:
    print("bye")
