#User function Template for python3

class Solution:
    def rearrange(self, S, N):
        def ans(big,small,lenb,lens):
            diff = lenb - lens
            if diff>1:
                return -1
            s = ""
            for i in range(lens):
                s += big[i]
                s += small[i]
            if diff!=0:
                s += big[-1]
            return s
            

        lenv = 0
        lenc = 0
        v = []
        c = []
        vowels = {"a","e","i","o","u"}
        for i in S:
            if i in vowels:
                lenv += 1
                v.append(i)
            else:
                lenc += 1
                c.append(i)
        v.sort()
        c.sort()
        s = ""
        if lenv>lenc:
            return ans(v,c,lenv,lenc)
        elif lenv==lenc:
            if v>=c:
                #print("idhar aaya")
                return ans(c,v,lenc,lenv)
            else: 
                #print("yaha aaya")
                return ans(v,c,lenv,lenc)
        else:
            return ans(c,v,lenc,lenv)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N = int(input().strip())
        S = input().strip()
        ob=Solution()
        ans=ob.rearrange(S, N)
        print(ans)
# } Driver Code Ends