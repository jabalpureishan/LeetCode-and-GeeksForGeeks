#User function Template for python3

class Solution:
    # Function to find the number 
    # of maximum pair sums 
    def MaximumSum(self, a, n): 
        if n==1:
            return 0
        a.sort()
        Max = a[-1] + a[-2]
        hmap,count = {},0
        for i in a:
            count += hmap.get(i,0)
            hmap[Max-i] = hmap.get(Max-i,0) + 1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    v = ob.MaximumSum(arr, n)
    print(v)
    
# } Driver Code Ends