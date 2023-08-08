#User function Template for python3

class Solution:
        
    def minSwap (self,arr, n, k) : 
        window = 0
        for i in arr:
            if i<=k:
                window += 1
        swap = 0
        for i in arr[:window]:
            if i>k:
                swap += 1
        final = swap
        slides = n - window
        for i in range(slides):
            if arr[i]>k:
                swap -= 1
            if arr[window]>k:
                swap += 1
            window += 1
            final = min(swap,final)
        return final
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ob=Solution()
    ans = ob.minSwap(arr, n, k)
    print(ans)
    





# } Driver Code Ends