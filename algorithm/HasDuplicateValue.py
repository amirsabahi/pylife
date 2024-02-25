def hasDuplicateValue(array):
    visited_numbers = {}
    for num in array:
        if num in visited_numbers and visited_numbers[num] == 1:
            return True
        else:
            visited_numbers[num] = 1
    return False


print(hasDuplicateValue([2, 5, 1, 4]))

print(hasDuplicateValue([2, 4, 1, 4]))
