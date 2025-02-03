class Solution(object):
    def merge(self, A, m, B, n):
        result = []
        pointer1 = 0
        pointer2 = 0
        A1=[]
        B1=[]
        for i in A:
            if i !=0:
                A1.append(i)
        for i in B:
            if i !=0: 
                B1.append(i)
        A=A1
        B=B1
     
        while pointer1<len(A1) or pointer2<len(B1):
            if pointer1>= len(A1):
                result.append(B1[pointer2])
                pointer2= pointer2+1
            elif pointer2>=len(B1):
                result.append(A1[pointer1])
                pointer1= pointer1+1
            elif A[pointer1]< B1[pointer2]:
                result.append(A1[pointer1])
                pointer1=pointer1+1
            else:
                result.append(B1[pointer2])
                pointer2=pointer2+1
			
        return result

solution = Solution()
print(solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)) # [1,2,2,3,5,6]