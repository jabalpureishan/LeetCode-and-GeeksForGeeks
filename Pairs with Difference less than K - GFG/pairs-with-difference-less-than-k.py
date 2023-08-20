#User function Template for python3

class Solution:
    def countPairs(self,a, n, k): 
        a.sort()
        l,count = 0,0
        for r in range(n):
            while((a[r] - a[l])>=k):
                l += 1
            count += r - l
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n,k = map(int, input().strip().split())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.countPairs(arr, n, k))


# } Driver Code Ends