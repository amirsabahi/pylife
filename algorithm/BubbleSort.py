def bubble(array) -> []:
    print('start')
    counter = len(array) - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        counter -= 1
    return array


print(bubble([102, 20, 12, 5, 1, 2, 60]))
