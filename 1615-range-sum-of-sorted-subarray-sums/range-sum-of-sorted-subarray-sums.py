from heapq import heapify,heappop,heappush
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = []
        heapify(heap)
        for i in range(n):
            Sum = 0
            for j in range(i,n):
                Sum += nums[j]
                heappush(heap,-Sum)
                if len(heap)>right:
                    heappop(heap)
        ans = 0
        for i in range(right-left+1):
            ans += heappop(heap)
        return -ans%1000000007
        