def factorial(n):
    if n < 0:
        return
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
number=int(input('enter number'))
print("The factorial of number is:", factorial(number))


