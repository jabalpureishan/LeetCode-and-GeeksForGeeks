class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_,Max = 0,0
        for i in nums:
            sum_ += i
            Max = max(Max,i)
        ans = (Max*(Max+1))//2 - sum_
        if ans==0 and 0 in set(nums):
            return Max + 1
        return ans
        