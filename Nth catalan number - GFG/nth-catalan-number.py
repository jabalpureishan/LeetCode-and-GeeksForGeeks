#User function Template for python3
import math
class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
        Num = math.factorial(2*n)
        Den = (math.factorial(n+1))*(math.factorial(n))
        return Num//Den
 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        
        print(Solution().findCatalan(n))
        
# } Driver Code Ends