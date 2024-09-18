class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        tp,count = timePoints,0
        for i,j in enumerate(tp):
            tp[i] = 60*int(j[:2])+int(j[-2:])
            if tp[i]==0:
                count += 1
                if count>1: return 0
        print(tp)
        tp.sort()
        Min =  float("inf")
        for i in range(1,len(tp)):
            Min = min(Min,tp[i]-tp[i-1])
        if count>0:
            Min = min(Min,1440-tp[-1])
        Min = min(Min,1440-tp[-1]+tp[0])
        return Min