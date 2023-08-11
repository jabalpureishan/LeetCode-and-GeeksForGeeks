#User function Template for python3

class Solution:
    def maxTripletSum (self, arr,  n, K) : 
        hashmap,available = {},0
        for i in arr:
            hashmap[i] = hashmap.get(i,0) + 1
        for i in hashmap:
            available += hashmap[i] - 1
        K -= available
        if K<=0:
            return len(hashmap)
        else:
            return len(hashmap) - K



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, K = map(int, input().split())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.maxTripletSum(arr, n, K)
    print(res)



# } Driver Code Ends