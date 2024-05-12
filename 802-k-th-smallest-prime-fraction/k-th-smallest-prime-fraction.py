from heapq import heapify,heappop,heappush
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []
        heapify(heap)
        ind = 1
        for i in range(n):
            for j in range(i+1,n):
                ind += 1
                heappush(heap,(-arr[i]/arr[j],[arr[i],arr[j]]))
                if len(heap)>k:
                    heappop(heap)
        return heappop(heap)[1]