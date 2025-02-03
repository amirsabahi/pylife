from typing import List, Optional


class Solution:
	def getEvenDigitNumbers(self, arr: List[int]) -> Optional[List[int]]:
		# add your logic here
		result = []
		count = 0
		for i in range(len(arr)):
			n = arr[i]
			while n > 0:
				count+=1
				n=n/10
				if round(n)==0:
					break 
			if count%2 == 0:
				result.append(arr[i])	
			
		return result		

solution = Solution()	
print(solution.getEvenDigitNumbers([5, 42, 564, 5775, 34, 123, 454, 1, 45, 3556, 23442]))