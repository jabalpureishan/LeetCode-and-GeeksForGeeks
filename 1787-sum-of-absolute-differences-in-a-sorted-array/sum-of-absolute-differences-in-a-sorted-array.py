class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums) - 1 
        sum_ = sum(nums)
        prev = 0
        ans = []
        for i in range(n+1):
            sum_ -= nums[i]
            ans.append((sum_-(nums[i]*(n-i))+(nums[i]*i-prev)))
            prev += nums[i]
        return ans
        