#User function Template for python3

class Solution:
    def factorial(self, N):
        for i in range(N-1,1,-1):
            N *= i
        return str(N)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
# } Driver Code Ends