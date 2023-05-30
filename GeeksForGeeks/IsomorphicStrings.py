class Solution:
    def areIsomorphic(str1,str2):
        D = {}
        l1 = len(str1)
        l2 = len(str2)
        Done = set()
        if l1!=l2:
            return False
        for i in range(l1):
            first = str1[i]
            second = str2[i]
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







    print(areIsomorphic("pijthbsfy","fvladzpbf"))
    print(areIsomorphic("wfca","yssy"))
    print(areIsomorphic("paper","title"))
    print(areIsomorphic("badc","baba"))
    print(areIsomorphic("xudzhi","ftakcz"))