"""
!time limit exceeded
"""
import sys
sys.set_int_max_str_digits(43000)
class Solution:
    def divisible(s,m):
        length = len(word)
        out = []
        for i in range(1,length+1):

            if (int(word[:i])%m)==0 :
                out.append(1)
            else:
                out.append(0)
        return out
    print(divisible("998244353",3))
    print(divisible("1010",10))



