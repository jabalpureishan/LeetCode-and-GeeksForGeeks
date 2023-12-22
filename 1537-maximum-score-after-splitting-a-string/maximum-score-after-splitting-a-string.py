class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        o = s.count("1")
        z = 0
        Max = 0
        for i in range(n-1):
            if s[i]=="1":
                o -= 1
            else:
                z += 1
            Max = max(Max,o+z)
        return Max
        