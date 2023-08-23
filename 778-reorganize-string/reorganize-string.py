class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] =d.get(i,0) + 1
        hmap = sorted(d.items(),key=lambda x:x[1],reverse=True)
        #print(d,hmap)
        if hmap[0][1]>((len(s)+1)//2):
            return ""
        arr = [""]*len(s)
        start = 0
        for i in hmap:
            while(d[i[0]]>0):
                if start>=len(s):
                    start = 1
                arr[start] = i[0]
                d[i[0]] -= 1
                start += 2
        return "".join(arr)