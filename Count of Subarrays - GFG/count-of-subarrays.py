#User function Template for python3
class Solution:


	def countSubarray(self,arr, n, k):
        arr.append(float("inf"))
        total = 0
        count = 0
        for i in range(n+1):
            if arr[i]<=k:
                count += 1
            else:
                total += (count*(count+1))//2
                count = 0
        return (n*(n+1))//2 - total


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, k=map(int, input().strip().split())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.countSubarray(arr, n, k)
        print(ans)
        tc=tc-1
# } Driver Code Ends