class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        Num = n
        done = set()
        while Num>1 :
            Sum = 0
            while Num>0 :
                R = Num%10
                Sum += R**2
                Num = Num//10
            Num = Sum
            if Num == 1 :
                return True
            if Num in done:
                return False
            done.add(Num)
        else:
            return False
