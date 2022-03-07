def bubble_sort(array):
    for i in range(len(array)):
        print("I", i) 
        for j in range(len(array) - 1, i, -1):
            print("J", j)
            print("Compare i, j", array[i], array[j])
            if array[j] < array[i]:
                print("swap")
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
            print(array)
    return array



array = [3, 5, 1, 8]

print(bubble_sort(array))

