class Solution:
    def trailingZeroes(self, n: int) -> int:
        num,count = 5,0
        while(num<=n):
            count += n//num
            num *= 5
        return count

