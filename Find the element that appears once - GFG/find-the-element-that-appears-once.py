#User function Template for python3
class Solution:
    def search(self, A, N):
        D = {}
        for i in A:
            D[i] = D.get(i,0) + 1
        for i in D:
            if D.get(i)==1 :
                return i
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends