#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        Max = -1
        sMax = -1
        for i in arr:
            if i>Max:
                sMax = Max
                Max = i
            if Max>i>sMax:
                sMax = i
        return sMax


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)

# } Driver Code Ends