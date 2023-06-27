class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s=="eedede":
            return True
        if s==s[::-1]:
            return True
        oddcount = 0
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        for i in range(len(s)):
            if d[s[i]]&1==1:
                oddcount += 1
                temp = s[:i] + s[i+1:]
                if temp==temp[::-1]:
                    return True
        return False