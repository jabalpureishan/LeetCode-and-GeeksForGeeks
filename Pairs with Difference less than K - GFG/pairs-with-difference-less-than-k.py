#User function Template for python3

class Solution:
    def countPairs(self,a, n, k): 
        a.sort()
        left,right,count = 0,1,0
        while(right<n):
            diff = a[right] - a[left]
            if diff>=k:
                left += 1
                diff = a[right] - a[left]
            else:
                count += right - left
                right += 1
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