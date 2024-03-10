class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        ans = 0
        for i in happiness:
            heappush(heap,i)
            if len(heap)>k:
                heappop(heap)
        for i in range(k-1,-1,-1):
            curr = max(0,heappop(heap)-i)
            print(curr)
            ans += curr
        return ans

        