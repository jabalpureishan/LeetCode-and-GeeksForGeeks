#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        d = {}
        Max = 0
        sum_ = 0
        for i,j in enumerate(arr):
            sum_ += j
            if sum_==0:
                Max = max(Max,i+1)
            if sum_ in d:
                Max = max(Max,i-d[sum_])
            else:
                d[sum_] = i
        return Max




#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends