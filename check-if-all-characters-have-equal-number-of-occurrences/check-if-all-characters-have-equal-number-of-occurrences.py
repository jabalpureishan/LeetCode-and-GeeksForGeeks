class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        check = d.get(s[0])
        for i in d.values():
            if i!=check:
                return False
        return True