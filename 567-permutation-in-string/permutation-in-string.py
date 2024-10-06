from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        d2 =  Counter(s2[:l1])
        d1 = Counter(s1)
        if d1==d2:
            return True
        for i in range(l1,len(s2)):
            d2[s2[i]] += 1
            d2[s2[i-l1]] -= 1
            if d1==d2:
                return True

        return False
        
        