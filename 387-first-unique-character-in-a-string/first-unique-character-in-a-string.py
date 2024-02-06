class Solution:
    def firstUniqChar(self, s: str) -> int:
        D={}
        L = len(s)
        def get_index(s,i,L):
            for j in range(L):
                if(s[j]==i):
                    return(j)

        for i in s:
            D[i]=0
        for i in s:
            D[i]+=1
        for i in D:
            if(D.get(i)==1):
                return(get_index(s,i,L))
        return(-1)
     