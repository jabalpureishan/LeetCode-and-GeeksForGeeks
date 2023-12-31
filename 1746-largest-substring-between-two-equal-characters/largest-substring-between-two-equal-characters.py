class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        n = len(s)
        Max = -1
        for  i in range(n):
            if s[i] in d:
                Max = max(Max,i-d[s[i]]-1)
            else:
                d[s[i]] = i
        return Max