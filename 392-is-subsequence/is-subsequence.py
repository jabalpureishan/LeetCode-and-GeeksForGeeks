class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptrs,ptrt = 0,0
        while ptrs<len(s) and ptrt<len(t):
            if s[ptrs]==t[ptrt]:
                ptrs += 1
            ptrt += 1
        return ptrs==len(s)
            

        