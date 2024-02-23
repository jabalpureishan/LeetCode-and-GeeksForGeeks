class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {0:1}
        sum_ = count = 0
        for i in nums:
            sum_ += i
            count += hmap.get(sum_-k,0)
            hmap[sum_] = hmap.get(sum_,0) + 1
        return count