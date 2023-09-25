class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        snew,tnew = "",""
        for i in s:
            if i=="#":
                snew = snew[:-1]
            else:
                snew += i
        for i in t:
            if i=="#":
                tnew = tnew[:-1]
            else:
                tnew += i
        return snew==tnew
        