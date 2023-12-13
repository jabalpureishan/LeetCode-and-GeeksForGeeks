#User function Template for python3
from math import sqrt
class Solution:
    def sieveOfEratosthenes(self, N):
        arr = [False]*2+[True]*(N-1)
        root = sqrt(N)
        i = 2
        ans = []
        while i<=N:
            if arr[i]:
                ans.append(i)
                for j in range(i*i,N+1,i):
                    arr[j] = False
            i += 1
        return ans
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends