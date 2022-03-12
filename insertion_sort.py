# Insertion sort in Python
'''
Best Case: O(n)
Average Case: O(n^2)
Worst Case: O(n^2)
'''


def insertion_sort(array):
    for i in range(1, len(array)):
        print("I={}".format(i))
        key = array[i]
        j = i
        while j > 0 and key < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
            print("J={}".format(j), array)
        array[j] = key

    return array


#array = [3, 5, 1, 8, -9, 81, 72, -75, 45, 89, 654]
array = [6, 2, 4, 9, 3, 7]

print(insertion_sort(array))
