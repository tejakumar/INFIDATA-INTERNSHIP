n1 = 10
n2 = 0

try:
    result = n1 / n2
except ZeroDivisionError:
    print("Oops! Division by zero is not allowed.")
else:
    print("No exception occurred.")
finally:
    print("Finally block executed.")
print("end")