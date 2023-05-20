class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        Sum = 0 
        s = s + "$"
        current = s[0]
        for i in s:
            if i==current:
                count += 1
            else:
                Sum += (count*(count + 1))//2
                count = 1
                current = i
        return Sum%(10**9 + 7)
                