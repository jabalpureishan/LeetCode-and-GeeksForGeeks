class Solution:
    def makeFancyString(self, s: str) -> str:
        s = list(s)
        for i in range(2,len(s)):
            if s[i]==s[i-1]==s[i-2]:
                s[i-2] = ""
        return "".join(s)
        