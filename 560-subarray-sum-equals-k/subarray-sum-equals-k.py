class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d,sum_,ans = {0:1},0,0
        for ind,val in enumerate(nums):
            sum_ += val
            curr = sum_ - k
            ans += d.get(curr,0)
            d[sum_] = d.get(sum_,0) + 1
        return ans