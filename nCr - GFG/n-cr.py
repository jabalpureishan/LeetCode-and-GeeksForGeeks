#User function Template for python3
import math
class Solution:
    def nCr(self, n, r):
        if n<r:
            return 0
        mod = 10**9 + 7
        N = math.factorial(n)
        R = math.factorial(r)
        Res = (N//(R*(math.factorial(n-r))))
        Res = Res%mod
        return Res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends