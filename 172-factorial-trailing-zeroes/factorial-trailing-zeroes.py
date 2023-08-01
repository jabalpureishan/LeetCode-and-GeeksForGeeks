import sys
sys.set_int_max_str_digits(100000000)
from math import factorial
class Solution:
    def trailingZeroes(self, n: int) -> int:
        n = str(factorial(n))
        count = 0
        for i in range(-1,-(len(n)+2),-1):
            if n[i]=="0":
                count += 1
            else:
                break
        return count

