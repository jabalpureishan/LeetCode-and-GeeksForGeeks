#User function template for Python
from collections import OrderedDict
class Solution:	
	def remove_duplicate(self, A, N):
        
        d = OrderedDict({})
        for i in A:
            d[i] = 0
        A.clear()
        for i in d:
            A.append(i)
        return len(A)


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends