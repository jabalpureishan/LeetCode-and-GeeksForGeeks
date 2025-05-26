class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def find(nums,k):
            hmap = defaultdict(int)
            left = count = 0
            for right in range(len(nums)):
                hmap[nums[right]] += 1
                while len(hmap)>k:
                    hmap[nums[left]] -= 1
                    if hmap[nums[left]]==0:
                        hmap.pop(nums[left])
                    left += 1
                count += right - left + 1
            return count

        return find(nums,k) - find(nums,k-1)

        