#User function Template for python3

class Solution:
    def isPatternPresent(self, S , P):
        if P[0]=="^" and S.startswith(P[1:]):
            return 1
        elif P[-1]=="$" and S.endswith(P[:-1]):
            return 1
        elif P in S:
            return 1
        return 0



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        P=input()
        S=input()
        
        ob = Solution()
        print(ob.isPatternPresent(S,P))
# } Driver Code Ends