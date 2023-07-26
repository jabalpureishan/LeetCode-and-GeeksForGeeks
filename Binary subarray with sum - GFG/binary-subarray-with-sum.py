#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def numberOfSubarrays(self, arr, N, target):
        goal,nums = target,arr
        def count(nums,k):
            if k<0:
                return 0
            left,total,Sum = 0,0,0
            for right in range(len(nums)):
                Sum += nums[right]
                while(Sum>k):
                    Sum -= nums[left]
                    left += 1
                total += right - left + 1
            return total
        return count(nums,goal) - count(nums,goal-1)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, target = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.numberOfSubarrays(arr, N, target)
        print(res)
# } Driver Code Ends