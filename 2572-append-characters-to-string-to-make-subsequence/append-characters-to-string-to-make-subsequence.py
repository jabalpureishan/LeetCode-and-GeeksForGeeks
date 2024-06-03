class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ps,pt,lens,lent = 0,0,len(s),len(t)
        while ps<lens and pt<lent:
            if s[ps]==t[pt]:
                pt += 1
            ps += 1
        return lent - pt   