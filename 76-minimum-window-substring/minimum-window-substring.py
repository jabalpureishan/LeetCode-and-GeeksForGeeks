
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        p = t
        if len(p)>len(s):
            return ""
        ds,dp,left,have,Min,Minl = {},{},0,0,"#",float("inf")
        for i in p:
            dp[i] = dp.get(i,0) + 1
            ds[i] = 0
        need = len(dp)
        for right in range(len(s)):
            i = s[right]
            if i in ds:
                ds[i] += 1
                if ds[i]==dp[i]:
                    have += 1
            while(have==need):
                if right-left+1<Minl:
                    Minl = right-left+1
                    Min = s[left:right+1]
                j = s[left]
                if j in ds:
                    ds[j] -= 1
                    if ds[j]<dp[j]:
                        have -= 1
                left += 1
        if Min=="#":
            return ""
        return Min