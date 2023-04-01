class Solution:
    def minOperations(self, N):
        term = (N+1)//2
        term = term - 1
        if N%2 == 0:
            return term*(N-term) + 1
        return term*(N-term)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N =int(input())
        ob = Solution()
        print(ob.minOperations(N))
        
        T -= 1

# } Driver Code Ends