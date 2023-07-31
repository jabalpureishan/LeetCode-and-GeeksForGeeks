#User function Template for python3

class Solution:
    def solve(self, arr, n):
        arr.sort()
        x,y = "",""
        for i in range(0,n,2):
            x += str(arr[i])
        for i in range(1,n,2):
            y += str(arr[i])
        if x=="":
            x = 0
        if y=="":
            y = 0
        return int(x)+int(y)


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.solve(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends