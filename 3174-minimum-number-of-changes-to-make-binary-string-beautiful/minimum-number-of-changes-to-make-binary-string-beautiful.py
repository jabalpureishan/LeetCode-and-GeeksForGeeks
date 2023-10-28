class Solution:
    def minChanges(self, s: str) -> int:
        length,ans = len(s),0
        if length==1:
            return ans
        for i in range(0,length,2):
            if s[i]=="0" and s[i+1]=="1" or s[i]=="1" and s[i+1]=="0":
                ans += 1
        return ans
        