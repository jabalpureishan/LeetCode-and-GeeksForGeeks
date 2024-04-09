class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ind,n,alpha,hmap,s, = 0,len(s),"abcdefghijklmnopqrstuvwxyz",{},list(s)
        for i,j in enumerate(alpha):
            hmap[j] = i
        while ind<n and k>0:
            pos = hmap[s[ind]]
            Min = s[ind]
            for i in range(pos-k,pos+k+1):
                #print("comparing",s[ind],alpha[i%26])
                Min = min(Min,alpha[i%26])
            #print("replaced",s[ind],Min,"k:",k)
            #print(pos-hmap[Min],26-(pos-hmap[Min]))
            diff = pos-hmap[Min]
            k -= min(diff,26-(diff))
            #print("k:",k)
            s[ind] = Min
            ind += 1
        return "".join(s)