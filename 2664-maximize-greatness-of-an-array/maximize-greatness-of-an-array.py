class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        print("nums:",nums)
        p1,p2 = 0,1
        count = 0
        while p2<n and p1<p2:
            while p2<n and nums[p2]<=nums[p1]:
                p2 += 1
            if p2<n and nums[p2]>nums[p1]:
                p2 += 1
                count += 1
            p1 += 1
        return count
        