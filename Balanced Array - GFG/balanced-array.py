#User function Template for python3

class Solution:
    def minValueToBalance(self,a,n):
        middle = n//2
        return abs(sum(a[:middle])-sum(a[middle:]))


#{ 
 # Driver Code Starts
#Initial Template for Python 3





t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.minValueToBalance(a,n)
    print(ans)

# } Driver Code Ends