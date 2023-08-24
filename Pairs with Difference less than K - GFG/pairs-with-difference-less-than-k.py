#User function Template for python3

class Solution:
    def countPairs(self,a, n, k): 
        a.sort()
        left,count = 0,0
        for right in range(1,n):
            diff = a[right] - a[left]
            #print("diff:",diff)
            while(diff>=k):
                left += 1
                diff = a[right] - a[left]
            #print(a[left:right+1])
            count += right - left
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