#User function Template for python3
import math
class Solution:
    def minimumNumber(self, n, arr):
        ans = arr[0]
        for i in range(1,n):
            ans = math.gcd(arr[i],ans)
        return ans
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        obj=Solution()
        print(obj.minimumNumber(n,arr))
# } Driver Code Ends