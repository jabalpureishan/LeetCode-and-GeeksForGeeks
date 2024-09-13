#User function Template for python3
class Solution:
    def print2largest(self, arr):
        Max = SMax = -1
        for i in arr:
            if i>Max:
                SMax = Max
                Max = i
            elif Max>i>SMax:
                SMax = i
        return SMax


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends