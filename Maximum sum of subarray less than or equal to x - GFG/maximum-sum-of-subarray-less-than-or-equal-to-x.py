class Solution:
    def findMaxSubarraySum(self, arr, n, k):
        left = Max = Sum = 0
        for right in range(n):
            Sum += arr[right]
            while(Sum>k):
                Sum -= arr[left]
                left += 1
            Max = max(Max,Sum)
        return Max


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a=list(map(int,input().split()))
        k = int(input())
        ob = Solution()
        ans=ob.findMaxSubarraySum(a,n,k)
        print(ans)

# } Driver Code Ends