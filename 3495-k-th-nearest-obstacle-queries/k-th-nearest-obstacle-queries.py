class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        ans,heap = [],[]
        heapify(heap)
        for i in queries:
            heappush(heap,-(abs(i[0])+abs(i[1])))
            if len(heap)>k:
                heappop(heap)
            if len(heap)==k:
                ans.append(-heap[0])
            else:
                ans.append(-1)
            #print(heap)
        return ans
        