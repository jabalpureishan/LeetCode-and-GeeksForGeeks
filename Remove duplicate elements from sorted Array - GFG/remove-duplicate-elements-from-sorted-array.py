
class Solution:	
	def remove_duplicate(self, A, N):
        ind = 1
        while(ind<len(A)):
            if A[ind]==A[ind-1]:
                A.pop(ind-1)
            else:
                ind += 1
        
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