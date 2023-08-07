#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def removeReverse(self, S):
        L=len(S)
        D=True
        start=True
        while D:
            newstr=self.remRev(S,L,start)
            S=newstr[0]
            D=newstr[1]
            start=not start
            L-=1
        if start:
            return S[::-1]
        return S
    
    def remRev(self,S,L,start):
        if start:
            for i in range(L):
                for j in range(L-1,i,-1):
                    if S[i]==S[j]:
                        return S[:i]+S[i+1:], True
            return S,False
        else:
            for i in range(L-1,-1,-1):
                for j in range(i):
                    if S[i]==S[j]:
                        return S[:i]+S[i+1:], True
            return S,False

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.removeReverse(S)
        print(ans)


# } Driver Code Ends