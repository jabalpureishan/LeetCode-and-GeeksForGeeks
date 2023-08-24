class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        d,count = {},0
        for i in nums:
            if i in d:
                count += d[i]
            d[i+k] = d.get(i+k,0) + 1
            #d[k-i] = d.get(k-i,0) + 1
        return count