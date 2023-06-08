class Solution:
    def minOperations(self, n: int) -> int:
        if n%2==0:
            mid = n//2
        else:
            mid = (n-1)//2
        count = 0
        i = 1
        while(mid>0):
            count += n - i
            i += 2
            mid -= 1
        return count