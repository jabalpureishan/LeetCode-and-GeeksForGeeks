class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        arr = [1]*n
        for i in range(k):
            for j in range(1,n):
                arr[j] += arr[j-1]
        return arr[-1]%(1000000007)
            