
def bubblesort(array):

    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


Array = [9, 5, 7, 3, 2, 5, 7, 8, 4, 2, 4, 6]

print(bubblesort(Array))

