#User function Template for python3

class Solution:
    def calc_Sum (self, arr,  n, brr, m) : 
        a,b = "",""
        for i in arr:
            a = a + str(i)
        for i in brr:
            b = b + str(i)
        return int(a) + int(b)
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    m = int(input())
    brr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.calc_Sum(arr, n, brr, m)
    print(res)


# } Driver Code Ends