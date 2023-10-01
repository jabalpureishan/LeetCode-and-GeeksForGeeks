class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        length,window,Sum = len(s),k,0
        num = 1

        for i in range(k):
            Sum += ((ord(s[i]) - 96)*num)
            num *= power
        #print(Sum)
        if Sum%modulo==hashValue:
            return s[:k]
        Pow = pow(power,k-1)
        for i in range(length-k):
            Sum -= ord(s[i])-96
            Sum //= power
            Sum += (ord(s[window]) - 96)*Pow            
            if Sum%modulo==hashValue:
                return s[i+1:window+1]
            window += 1
        