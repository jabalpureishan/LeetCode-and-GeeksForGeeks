#User function Template for python3
class Solution:

	def printUnsorted(self,arr, n):
        copy,end,length,start = arr[:],0,0,0
        copy.sort()
        once = True
        for i in range(n):
            if copy[i]!=arr[i]:
                while(once):
                    start = i
                    once = False
                end = i
        return [start,end]


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printUnsorted(arr, n)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends