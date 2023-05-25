class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        D = {}
        l1 = len(s)
        l2 = len(t)
        Done = set()
        if l1!=l2:
            return False
        for i in range(l1):
            first = s[i]
            second = t[i]
            if first not in D:
                if second in Done:
                    return False
                else:
                    Done.add(second)
                D[first] = second
            else:
                if second!=D.get(first):
                    return False
        return True
