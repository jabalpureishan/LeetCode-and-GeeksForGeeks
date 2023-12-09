class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        n = len(nums)
        d = {}
        Max = 0
        nmax = 0
        mele = nums[0]
        for right in range(n):
            d[nums[right]] = d.get(nums[right],0) + 1
            if d[nums[right]]>Max:
                Max = d[nums[right]]
            while Max>k:
                d[nums[left]] -= 1
                if d[nums[left]]+1==Max:
                    Max = max(d.values())
                left += 1
            nmax = max(nmax,right-left+1)
        return nmax
                
            
        