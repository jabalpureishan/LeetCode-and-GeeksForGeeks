class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = cost = Max = 0
        n = len(s)
        for right in range(n):
            cost += abs(ord(s[right])-ord(t[right]))
            while cost>maxCost:
                cost -= abs(ord(s[left])-ord(t[left]))
                left += 1
            Max = max(Max,right-left+1)
        return Max
        