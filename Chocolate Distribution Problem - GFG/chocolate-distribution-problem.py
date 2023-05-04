#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        
        A.sort()
        #print("A:",A)
        loop  = N - M + 1
        Min = A[-1]
        for i in range(loop):
            #print("1st:",A[i])
            #print("2nd:",A[M-1])
            #print("Diff:",A[M-1]-A[i])
            Min = min(Min,A[M-1]-A[i])
            M+=1
        return Min


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends