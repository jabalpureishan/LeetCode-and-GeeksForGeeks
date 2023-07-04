from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        d1 = {}
        for i in s1:
            d1[i] = d1.get(i,0) + 1
        curr = s2[:window]
        d2 = {}
        for i in curr:
            d2[i] = d2.get(i,0) + 1
        if d1==d2:
            return True
        slides = len(s2) - window
        for j in range(slides):
            d2[s2[window]] = d2.get(s2[window],0) + 1
            d2[s2[j]] -= 1
            if d2[s2[j]]==0:
                d2.pop(s2[j])
            if d1==d2:
                return True
            window += 1
        return False