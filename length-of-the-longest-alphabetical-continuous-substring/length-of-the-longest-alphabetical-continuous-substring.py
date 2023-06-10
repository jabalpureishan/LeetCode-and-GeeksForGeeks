class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        count = 1
        Max = 0
        s += "#"
        for i in range(1,len(s)):
            if((ord(s[i])-ord(s[i-1]))==1):
                count += 1
            else:
                Max = max(count,Max)
                count = 1
        return Max

