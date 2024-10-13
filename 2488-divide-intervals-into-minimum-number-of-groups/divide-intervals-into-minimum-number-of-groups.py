class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [[intervals[0][1],intervals[0][0]]]
        heapify(heap)
        for i in range(1,len(intervals)):
            if heap[0][0]<intervals[i][0]:
                heappop(heap)
            heappush(heap,[intervals[i][1],intervals[i][0]])
        return len(heap)

        