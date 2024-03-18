class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intv = intervals
        intv.append(newInterval)
        intv.sort()
        intv.append([float("inf"),0])
        start,end = intv[0][0],intv[0][1]
        n = len(intv)
        #print(intv)
        ans = []
        for i in range(n-1):
            if end>=intv[i+1][0]:
                #print("in")
                end = max(end,intv[i+1][1])
            else:
                #print("out")
                ans.append([start,end])
                start = intv[i+1][0]
                end = intv[i+1][1]
        return ans