
# Plus One: Add one to the integer represented by an array.

from typing import List


def sum_one_integer(array: List[int]) -> List[int]:
    n = len(array)
    for i in range(n-1, -1 ,-1):
        if array[i]<9:
            array[i]+=1
            return array
        array[i]=0

    return [1]+array


print(sum_one_integer([1,1,1])) # [1,1,2]
print(sum_one_integer([1,9,9])) # [2,0,0]
print(sum_one_integer([9,9,9])) # [1,0,0,0]

