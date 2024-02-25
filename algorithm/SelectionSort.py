def selectionSort(array: []) -> []:
    for i in range(len(array) - 1):
        lowest_index = i
        for j in range(i + 1, len(array), 1):
            if array[j] < array[lowest_index]:
                lowest_index = j
        if lowest_index != i:
            array[i], array[lowest_index] = array[lowest_index], array[i]

    return array


print(selectionSort([5, 2, 1, 8, 6, 9, 3]))
