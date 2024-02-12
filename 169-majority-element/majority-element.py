class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        D={}
        n = len(nums)
        for i in nums:
            D[i]=0
        for i in nums:
            D[i]+=1
        for i in D:
            if(D.get(i)>(n/2)):
                return(i)