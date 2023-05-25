class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dp = {}
        length = len(s)
        window = 0
        output = []
        for i in p:
            window += 1
            dp[i] = dp.get(i,0) + 1
        #print("dp:",dp)
        #initial d
        ds = {}
        for i in s[:window]:
            ds[i] = ds.get(i,0) + 1
        if dp==ds:
            output.append(0)
        slides = length - window
        for j in range(slides):
            sub = s[j]
            add = s[window]
            ds[add] = ds.get(add,0) + 1
            ds[sub] = ds.get(sub) - 1
            if ds.get(sub)==0:
                ds.pop(sub)
            if ds==dp:
                output.append(j+1)
            window += 1
        return output


        
        