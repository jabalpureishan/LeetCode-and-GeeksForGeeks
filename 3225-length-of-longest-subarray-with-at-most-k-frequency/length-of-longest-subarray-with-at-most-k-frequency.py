class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d,Max,left,n = defaultdict(int),0,0,len(nums)
        for right in range(n):
            d[nums[right]] += 1
            while d[nums[right]]>k:
                d[nums[left]] -= 1
                left += 1
            Max = max(Max,right-left+1)
        return Max
        