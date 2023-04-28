from collections import deque
class Solution:
    def rotateArr(self,A,D,N):
        B = deque(A)
        A.clear()
        for i in range(D):
            B.append(B[0])
            B.popleft()
        for i in B:
            A.append(i)

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends