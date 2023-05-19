class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        result = []
        i = 1
        while i*i <= n:
            if n % i == 0:
                result.append(i)
                if n//i != i:
                    result.append(n//i)
            i += 1
        if len(result)<k:
            return -1
        result.sort()
        return result[k-1]
