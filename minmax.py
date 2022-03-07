import random


def min_(array):
    if len(array) == 0:
        return None
    elif len(array) == 1:
        return array[0]
    else:
        minval = min_(array[1:])
        min1 = array[0]
        if minval < min1:
            min1 = minval
        return min1


def max_(array):
    if len(array) == 0:
        return None
    elif len(array) == 1:
        return array[0]
    else:
        maxval = max_(array[1:])
        max1 = array[0]
        if maxval > max1:
            max1 = maxval
        return max1


def minmax(array):
    return min_(array), max_(array)


print(min_([1,2,3,4,5,-9,99,89]))
print(max_([1,2,3,4,5,-9,99,89]))
print(minmax([1,2,3,4,5,-9,99,89, 365, 4265]))


values = []
for i in range(50):
    values.append(random.randint(-100, 100))

print(values)
print(minmax(values))
