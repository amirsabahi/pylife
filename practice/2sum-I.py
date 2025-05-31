from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            y=target-nums[i]
            if y in nums[i+1:]:
                return [i,(nums[i+1:].index(y))+len(nums[0: i+1])]    
            

sln = Solution()
print(sln.twoSum([2,7,11,15], 9))