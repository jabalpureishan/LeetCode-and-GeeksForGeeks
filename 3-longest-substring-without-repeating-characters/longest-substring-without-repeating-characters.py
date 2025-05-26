class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set  = set()
        j = 0
        Max = 0
        for i in range(len(s)):
            while s[i] in Set:
                Set.discard(s[j])
                j += 1
            Max = max(Max,i-j+1)
            Set.add(s[i])
        return Max
            
            
