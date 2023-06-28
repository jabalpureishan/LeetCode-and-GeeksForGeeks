class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        length = len(intervals)
        intervals.append([float("inf"),0])
        #print(intervals)
        output = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(length):
            if intervals[i+1][0]<=end:
                end = max(end,intervals[i+1][1])
            else:
                output.append([start,end])
                start = intervals[i+1][0]
                end = intervals[i+1][1]
        return output