class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s,t = Counter(s),Counter(t)
        for i in s:
            if s[i]!=t.get(i,0):
                return False
        return True