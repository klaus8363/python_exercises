def factorial(n):
    print("factorial ", n)
    if n < 0:
        return "Cannot compute factorial of negative integers."
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))

