class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        Max = 0
        for i in nums:
            d[i] = d.get(i,0) + 1
            Max = max(Max,d[i])
        count = 0
        for i in d:
            if d[i]==Max:
                count += Max
        return count
        