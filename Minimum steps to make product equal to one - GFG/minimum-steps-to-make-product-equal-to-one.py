#User function Template for python3

class Solution:
    def makeProductOne(self, arr, N):
        count = 0
        prod = 1
        for i in arr:
            prod *= i
            count += abs(abs(i)-1)
        if prod<0:
            count += 2
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.makeProductOne(arr,N))
# } Driver Code Ends