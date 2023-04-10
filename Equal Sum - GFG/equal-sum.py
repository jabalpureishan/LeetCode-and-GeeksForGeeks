#User function Template for python3
class Solution:

	def equilibrium(self,arr, n): 
    	before = 0
    	after = sum(arr)
    	for i in arr:
    	    after -= i
    	    if before==after:
    	        return "YES"
            before +=i
        return "NO"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	
	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int , input().strip().split()))
	    ob = Solution()
	    ans=ob.equilibrium(a, n)
	    print(ans)
	    tc=tc-1
# } Driver Code Ends