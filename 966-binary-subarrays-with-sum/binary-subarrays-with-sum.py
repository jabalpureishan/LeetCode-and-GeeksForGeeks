class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum_,d,count = 0,{0:1},0
        for i in nums:
            sum_ += i
            count += d.get(sum_-goal,0)
            d[sum_] = d.get(sum_,0) + 1
        return count