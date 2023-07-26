#User function Template for python3
class Solution:
    def countSubarray(self, N, A, L, R):
        def count(N,A,K):
            left = Sum = total = 0
            for right in range(N):
                Sum += A[right]
                while(Sum>K):
                    Sum -= A[left]
                    left += 1
                total += right -left + 1
            return total
        return count(N,A,R) - count(N,A,L-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,L,R = map(int,input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countSubarray(N, A, L, R)
        print(ans)

# } Driver Code Ends