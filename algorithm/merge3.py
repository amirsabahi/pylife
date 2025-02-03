from typing import List


class Solution:
	def merge(self, arr: List[int], endIndex: int) -> List[int]:
		# add your logic here
		pointer1= 0
		pointer2=endIndex+1
		result=[]
		while pointer1<endIndex+1 or pointer2<len(arr):
			if pointer1>endIndex:
				result.append(arr[pointer2])
				pointer2 = pointer2+1
			elif pointer2>= len(arr):
				result.append(arr[pointer1])
				pointer1 = pointer1 +1
			elif arr[pointer1]>=arr[pointer2]:
				result.append(arr[pointer2])
				pointer2 = pointer2+1
			else:
				result.append(arr[pointer1])
				pointer1 = 1+pointer1
		return result	

solution = Solution()
#print(solution.merge([1, 3 ,5,7 ,9 ,11 ,0 ,4 ,6, 8], 5)) 
print(solution.merge([3,3 ,9 ,11, 1, 3 ,3, 4], 3)) #