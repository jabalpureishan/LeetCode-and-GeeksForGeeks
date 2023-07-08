class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Max = j = 0
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
            #print("d:",d)
            curr = max(d.values())
            #print("curr:",curr)
            #print("len",i-j+1)
            #print(((i-j+1))>k)
            while(((i-j+1)-curr)>k):
                d[s[j]] -= 1
                #print("d--",d)
                j += 1
                curr = max(d.values())
                #print("curr00",curr)
            Max = max(Max,i-j+1)
        return Max