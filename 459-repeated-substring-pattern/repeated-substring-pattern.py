class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(1,length//2+1):
            if s[:i]*(length//i)==s:
                return True
        return False