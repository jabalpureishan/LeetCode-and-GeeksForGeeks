class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negcount = 0
        for i in nums:
            if i<0:
                negcount+=1
            if i==0:
                return 0
        if negcount%2==0:
            return 1
        return -1
