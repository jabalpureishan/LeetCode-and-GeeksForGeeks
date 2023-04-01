class Solution:
    def leaders(self, A, N):
        Max = 0
        O = []
        for i in range(1,N+1):
            i = -i
            if A[i]>=Max:
                Max = A[i]
                O.append(A[i])
        return O[::-1]
        
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends