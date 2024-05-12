from heapq import heapify,heappop,heappush
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        ans = []
        for i in range(n):
            for j in range(i+1,n):
                ans.append([arr[i]/arr[j],[arr[i],arr[j]]])
        ans.sort()
        return ans[k-1][1]