#User function Template for python3

class Solution:
    def minChange(self,S):
        d = {}
        for i in S:
            d[i] = d.get(i,0) + 1
        out = 0
        for i in d.values():
            out += i - 1
        return out


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S = input()
        
        ob = Solution()
        print(ob.minChange(S))
# } Driver Code Ends