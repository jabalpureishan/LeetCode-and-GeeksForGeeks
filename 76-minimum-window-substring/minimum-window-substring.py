from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        p = t
        d,left,Min,Minl,c = {},0,"##",float("inf"),{}
        for i in p:
            d[i] = 0
            c[i] = c.get(i,0) + 1
        def check(c,d):
            for i in d:
                if d[i]<c[i]:
                    return False
            return True
        #print("initial:",d)
        for right in range(len(s)):
            #print("curr:",s[right])
            if s[right] in d:
                #print("in d")
                d[s[right]] += 1
            #print("befor:",s[left:right+1])
            #print("before:",d)

            while(check(c,d)):
                #print("while chalu")
                if right-left+1<Minl:
                    Minl = right - left + 1
                    Min = s[left:right+1]
                if s[left] in d:
                    d[s[left]] -= 1
                left += 1


                

                
            #print("after:",s[left:right+1])
            
        if Min =="##":
            return ""
        return Min