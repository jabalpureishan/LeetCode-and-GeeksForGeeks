#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        hmap,Sum,Max = {0:-1},0,0
        for ind,val in enumerate(arr):
            Sum += val
            if Sum-k in hmap:
                Max = max(Max,ind - hmap[Sum-k])
            if Sum not in hmap:
                hmap[Sum] = ind
        return Max
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends