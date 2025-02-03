class MergeSort:
    def sort(self, arr):
        mid = round(len(arr)/2)
        left = arr[:mid]
        right = arr[mid:]

        if len(arr) <= 1:
            return arr

        left = self.sort(left)
        right = self.sort(right)
    
        return self.merge(left, right)
    
    def merge(self, arr1, arr2):
        result = []
        i = 0
        j=0
        while i<len(arr1) and j<len(arr2):
           if arr1[i]< arr2[j]:
                result.append(arr1[i])
                i+=1
           else:
                result.append(arr2[j])
                j+=1    
        result += arr1[i:]
        result += arr2[j:]
        return result


mergSort = MergeSort()
sortedArray = mergSort.sort([3,2,1,4,5,6,7,-8,9,10])
print(sortedArray)        