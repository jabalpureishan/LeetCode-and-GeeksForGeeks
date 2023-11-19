class Solution:
    def minimumSteps(self, s: str) -> int:
        ind,n,ans = 0,len(s),0
        for i in range(n):
            if s[i]=="0":
                ans += i-ind
                ind += 1
        return ans
