class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = Sum = Max =  0
        for right in range(len(s)):
            Sum += abs(ord(s[right])-ord(t[right]))
            while Sum>maxCost:
                Sum -= abs(ord(s[left])-ord(t[left]))
                left += 1
            Max =  max(Max,right-left+1)
        return Max
        