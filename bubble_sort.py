# Bubble sort implementation in python

def bubble_sort(array):
    for i in range(len(array)):
        print("I={}".format(i))
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[i]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
            print("J={}".format(j), array)
    return array


array = [3, 5, 1, 8, -9, 81, 72, -75, 45, 89, 654]

print(bubble_sort(array))
