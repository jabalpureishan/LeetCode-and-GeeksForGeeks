class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [False]*2+[True]*(n-1)
        root = sqrt(n)
        i = 2
        count = 0
        while i<=root:
            if arr[i]:
                if i<n:
                    count += 1
                for j in range(i*i,n+1,i):
                    arr[j] = False
            i += 1

        for j in range(i,n):
            if arr[j]:
                count += 1
        return count
        