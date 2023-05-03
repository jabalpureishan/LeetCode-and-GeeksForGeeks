#User function Template for python3
from itertools import permutations
class Solution:
    def permutation(self,s):
        s = "".join(sorted(s))
        P = permutations(s)
        out = []
        for i in P:
            Ans = "".join(i)
            out.append(Ans)
        #out.sort()
        return out
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends