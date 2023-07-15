class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        m = {}
        length = len(s)
        for i in range(minSize,maxSize+1):
            window = i
            slides = length - window
            d = {}
            for j in s[:window]:
                d[j] = d.get(j,0) + 1
            #print("first d:",d)
            if len(d)<=maxLetters:
                m[s[:window]] = m.get(s[:window],0) + 1
            for j in range(slides):
                d[s[window]] = d.get(s[window],0) + 1
                d[s[j]] -= 1
                #print("d:",d)
                #print("j:",j)
                #print("s[j]",s[j])
                if d[s[j]]==0:

                    d.pop(s[j])
                #print("d:",d)
                if len(d)<=maxLetters:
                    #print("curr:",s[j+1:window+1])
                    m[s[j+1:window+1]] = m.get(s[j+1:window+1],0) + 1
                window += 1
        ans = m.values()
        if len(ans)==0:
            return 0
        return max(ans)