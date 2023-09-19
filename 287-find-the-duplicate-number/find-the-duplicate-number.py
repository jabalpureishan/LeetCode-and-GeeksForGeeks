class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        D = {}
        for i in nums:
            D[i]=0
        for i in nums:
            D[i]+=1
        for i in D:
            if D.get(i)>1 :
                return i