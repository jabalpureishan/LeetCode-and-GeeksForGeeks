class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Max = j = curr = 0
        d = {}
        ele = s[0]
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
            if d[s[i]]>curr:
                curr = d[s[i]]
                ele = s[i]
            while(((i-j+1)-curr)>k):
                d[s[j]] -= 1
                if s[j]==ele:
                    ans = max(d.items(),key = lambda x:x[1])
                    ele = ans[0]
                    curr = ans[1]
                j += 1
            Max = max(Max,i-j+1)
        return Max