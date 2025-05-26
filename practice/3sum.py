

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = set()
        positive = []
        negative = []
        zero = []
        nums.sort()
        for x in nums:
            if x>0:
                positive.append(x)

        for x in nums:
            if x==0:
                zero.append(x)

        for x in nums:
            if x<0:
                negative.append(x)
        Pos, Neg = set(positive), set(negative)
        if len(zero) > 2:
            triplets.add((0,0,0))
            
        if zero:
            for n in Neg:
                if  -1*n in Pos:
                    triplets.add((-1*n, 0, n)) 
        for i in range(len(negative)):
            for j in range(i+1, len(negative)):
                target = -1* (negative[i] + negative[j])
                if target in Pos:
                    triplets.add((negative[i], negative[j], target))
            
        for i in range(len(positive)):
            for j in range(i+1, len(positive)):
                target = -1* (positive[i] + positive[j])
                if target in Neg:
                    triplets.add(tuple(sorted([positive[i], positive[j], target])))
        print(triplets)
        result=[]
        for item in triplets:
            result.append(item)
        return result          

sln = Solution()
# sln.threeSum([-1,0,1,2,-1,-4])    
# sln.threeSum([0,1,-1])     
# sln.threeSum([0,0,0,])  
# sln.threeSum([0,0,0,0,])  
# sln.threeSum([1,2,-2,-1])  
# sln.threeSum([-2,0,1,1,2])  
sln.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10])  


