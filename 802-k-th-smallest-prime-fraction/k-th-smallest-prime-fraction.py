class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                heappush(heap,(-(arr[i] / arr[j]), arr[i], arr[j]))
                if len(heap)>k:
                    heappop(heap)
        return [heap[0][1],heap[0][2]]
        