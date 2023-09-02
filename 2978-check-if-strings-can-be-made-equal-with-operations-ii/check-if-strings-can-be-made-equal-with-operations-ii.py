class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        f1,f2,f3,f4 = {},{},{},{}
        length = len(s1)
        for i in range(0,length,2):
            f1[s1[i]] = f1.get(s1[i],0)  + 1
            f2[s2[i]] = f2.get(s2[i],0)  + 1
        for i in range(1,length,2):
            f3[s1[i]] = f3.get(s1[i],0)  + 1
            f4[s2[i]] = f4.get(s2[i],0)  + 1
        return f1==f2 and f3==f4
        