class Solution:
    def minSum(self, arr, n):
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
import heapq as hq

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minSum(arr,n))

# } Driver Code Ends