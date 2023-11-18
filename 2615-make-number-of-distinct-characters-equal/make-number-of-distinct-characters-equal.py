class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        d1 = Counter(word1)
        d2 = Counter(word2)
        w1 = list(d1.keys())
        w2 = list(d2.keys())
        #print(w1,w2)
        def nikal(d,i):
            if d[i]==0:
                d.pop(i)

        def dal(d,i):
            d[i] = d.get(i,0) + 1
        #print(d1,d2)
        for i in w1:
            d1[i] -= 1
            nikal(d1,i)
            for j in w2:
                #print("d2before:",d2)
                dal(d1,j)
                dal(d2,i)
                d2[j] -= 1
                nikal(d2,j)

                if len(d1)==len(d2):
                    return True
                d2[i] -= 1
                nikal(d2,i)
                d1[j] -= 1
                nikal(d1,j)
                dal(d2,j)
                #print("d2after:",d2)
            dal(d1,i)
        return False

            