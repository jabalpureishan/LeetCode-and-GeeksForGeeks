class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        set_,Max = set(nums),-1
        for i in set_:
            if i>0 and -i in set_:
                Max = max(Max,i)
        return Max
        