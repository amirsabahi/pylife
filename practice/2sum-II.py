class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l]+numbers[r] > target:
                r=r-1
            else:
                l=l+1    


sln = Solution()
result = sln.twoSum([1,2,3,4,4,9,56,90], 8)
print(result)

result = sln.twoSum([2,3,4], 6)
print(result)
result = sln.twoSum([2,7,11,15], 9)
print(result)

result = sln.twoSum([-1,0], -1)
print(result)
