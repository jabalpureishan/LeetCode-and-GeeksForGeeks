class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        heap = []
        heapify(heap)
        arr.sort()
        n = len(arr)
        med = arr[(n-1)//2]
        for i in arr:
            heappush(heap,(abs(med-i),i))
            if len(heap)>k:
                heappop(heap)
        ans = [i[1] for i in heap]
        return ans
        