class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def count(nums,k,n):
            hmap,left,ans = defaultdict(int),0,0
            for right in range(n):
                hmap[nums[right]] += 1
                while len(hmap)>k:
                    hmap[nums[left]] -= 1
                    if hmap[nums[left]]==0:
                        hmap.pop(nums[left])
                    left += 1
                ans += right-left+1
            return ans

        n = len(nums)
        return count(nums,k,n)-count(nums,k-1,n)
        