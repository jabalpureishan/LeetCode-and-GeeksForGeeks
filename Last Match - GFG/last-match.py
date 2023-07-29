#User function Template for python3
class Solution:
    def findLastOccurence(self, A, B):
        ind = -1
        window = len(B)
        for i in range(len(A)-window+1):
            if A[i:window]==B:
                ind = i
            window += 1
        if ind==-1:
            return ind
        return ind+1


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        A = input()
        B= input()

        ob = Solution()
        print(ob.findLastOccurence(A,B))
# } Driver Code Ends