#User function Template for python3
class Solution:

	
	def countPairsWithDiffK(self,arr, n, k):
        arr.sort()
        def count(a,m):
            l,count = 0,0
            for r in range(n):
                while((a[r] - a[l])>=m and l<r):
                    l += 1
                count += r - l
            return count
        return count(arr,k+1) - count(arr,k)




#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends