def power(x, y):
    if x == 0:
        if y == 0:
            return None
        else:
            return 0
    else:
        if y == 0:
            return 1
        elif y == 1:
            return x
        else:
            return x * power(x, y-1)

print(power(0, 0))
print(power(0, 1))
print(power(1, 1))
print(power(1, 0))
print(power(3, 4))
print(power(2, 10))
