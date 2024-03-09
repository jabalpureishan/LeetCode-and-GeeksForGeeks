class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        d = {}
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                d[(arr[i],arr[j])] = arr[i]/arr[j]
        d = sorted(d.items(),key=lambda x:x[1])
        return list(d[k-1][0])
        