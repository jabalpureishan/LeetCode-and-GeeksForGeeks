from heapq import heapify,heappush,heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heap.append(-i)
        heapify(heap)
        while len(heap)>1:
            print(heap)
            a = heappop(heap)
            b = heappop(heap)
            sub = a-b
            if sub!=0:
                heappush(heap,sub)
        if len(heap)==0:
            return 0
        return abs(heappop(heap))
            
        