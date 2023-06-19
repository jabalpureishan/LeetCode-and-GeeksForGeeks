class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        Max = 0 
        start = 0
        for i in gain:
            start += i
            Max = max(Max,start)
        return Max