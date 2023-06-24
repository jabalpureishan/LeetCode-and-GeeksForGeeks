#User function Template for python3

class Solution:
    def minRow(self,N,M,A):
        Min = float("inf")
        output = 0
        for i in  range(N):
            count = A[i].count(1)
            if count<Min:
                Min = count
                output = i
        return output + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends