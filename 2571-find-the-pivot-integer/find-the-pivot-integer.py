class Solution:
    def pivotInteger(self, n: int) -> int:
        sum1,sum2 = (n*(n+1))//2,0
        for i in range(1,n+1):
            sum2 += i
            if sum2==sum1:
                return i
            sum1 -= i
        return -1
        