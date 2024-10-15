class Solution:
    def minimumSteps(self, s: str) -> int:
        a,count = list(s),0
        ind = 0
        while ind<len(s) and s[ind]!="1":
            ind += 1

        for i in range(ind+1,len(s)):
            if a[i]=="0":
                a[i],a[ind] = a[ind],a[i]
                count += i-ind
                ind += 1
                
        return count
        