class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        prime = [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, True]
        Min,Max = float("inf"),float("-inf")
        for ind,val in enumerate(nums):
            if prime[val]:
                Min,Max = min(Min,ind),max(Max,ind)
        return Max-Min
        