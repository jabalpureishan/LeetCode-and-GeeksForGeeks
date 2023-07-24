class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for i in range(2,len(s)+1):
            d = {}
            for j in s[:i]:
                d[j] = d.get(j,0) +1
            total += max(d.values()) - min(d.values()) 
            for j in range(len(s)-i):
                d[s[i]] = d.get(s[i],0) + 1
                i+=1
                d[s[j]] -= 1
                if d[s[j]]==0:
                    d.pop(s[j])
                total += max(d.values()) - min(d.values())
        return total