
class Shell:
"""
Sorts a sequence of strings from standard input using shell sort.
"""
    @classmethod
    def sort(cls, arr):
        N = len(arr)
        h = 1
        while h < N // 3:
            h = 3 * h + 1  # 1, 4, 13, 40...

        while h >= 1:
            for i in range(h, N):
                j = i
                while j >= h:
                    if arr[j] > arr[j - h]:
                        break
                    arr[j], arr[j - h] = arr[j - h], arr[j]
                    j -= h
            h //= 3
        return arr

    @classmethod
    def is_sorted(cls, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True


if __name__ == '__main__':
    import sys

    items = []
    for line in sys.stdin:
        items.extend(line.split())
    print('     items: ', items)
    print('Sort items: ', Shell.sort(items))
    assert Shell.is_sorted(items)
