class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        sum = a+b
        sum = bin(sum)
        sum = sum[2:]
        return sum
        