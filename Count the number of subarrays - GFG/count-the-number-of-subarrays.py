#User function Template for python3
class Solution:
    def countSubarray(self, N, A, L, R):
        def sub(n,nums,k):
            left = sum_ = count = 0
            for right in range(n):
                sum_ += nums[right]
                while sum_>k:
                    sum_ -= nums[left]
                    left += 1
                count += right - left + 1
            return count
        return sub(N,A,R)- sub(N,A,L-1)


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