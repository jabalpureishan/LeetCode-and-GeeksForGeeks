class Solution:
    def beautySum(self, s: str) -> int:
        length = len(s)
        total = 0
        for i in range(2,length+1):
            window = i
            slides = length - window
            d = {}
            for j in s[:window]:
                d[j] = d.get(j,0) +1
            total += max(d.values()) - min(d.values()) 
            for j in range(slides):
                d[s[window]] = d.get(s[window],0) + 1
                window+=1
                d[s[j]] -= 1
                if d[s[j]]==0:
                    d.pop(s[j])
                total += max(d.values()) - min(d.values())
        return total