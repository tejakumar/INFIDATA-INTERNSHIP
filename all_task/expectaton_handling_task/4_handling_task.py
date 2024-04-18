try:
    A=9.99999999/5
except(ArithematicError,IOError) as e:
    print(e)
else:
    print(a)
