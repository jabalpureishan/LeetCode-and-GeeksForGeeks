class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        Max,count,left,n,ans = max(nums),0,0,len(nums),0
        for right in range(n):
            if nums[right]==Max:
                count += 1
            while count>=k:
                if nums[left]==Max:
                    count -= 1
                left += 1
            ans += right-left+1
        return (n*(n+1))//2-ans
        