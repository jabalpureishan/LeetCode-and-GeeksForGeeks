class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        i,Sum = 2,1
        while i*i<=num:
            if num%i==0:
                Sum += i
                if num//i!=i:
                    Sum += num//i
            i += 1
        return Sum==num
        