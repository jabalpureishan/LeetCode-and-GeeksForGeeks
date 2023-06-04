class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        d = {}
        length = len(chars)
        for i in range(length):
            d[chars[i]] = vals[i]
        Max = float("-inf")
        curr = 0
        for i in s:
            if i in d:
                curr += d[i]
            else:
                curr += ord(i) - 96
            if curr>Max :
                Max = curr
            if curr<0 :
                curr = 0
        Max = max(0,Max)
        return Max
