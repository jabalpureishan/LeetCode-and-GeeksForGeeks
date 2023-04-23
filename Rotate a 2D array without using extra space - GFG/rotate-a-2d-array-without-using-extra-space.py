#User function Template for python3
class Solution:
    
    def rotateMatrix(self,arr, n):
        Output = arr[:]
        arr.clear()
        for i in range(1,n+1):
            arr.append([])
            for j in range(n):
                arr[i-1].append(Output[j][-i])

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                arr[i][j] = inputLine[i * n + j]
        ob = Solution()
        ob.rotateMatrix(arr, n)
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=" ")
        print()
        tc -= 1

# } Driver Code Ends