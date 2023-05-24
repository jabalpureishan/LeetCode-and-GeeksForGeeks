#User function Template for python3
class Solution:

	def findSum(self,a, b):
		A,B = "",""
		for i in a:
		    A += str(i)
		for i in b:
		    B += str(i)
		result = int(A) + int(B)
		output = []
		for i in str(result):
		    output.append(i)
		return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findSum(a, b)
        for i in ans:
            print(i, end=" ")
        print()
        tc -= 1

# } Driver Code Ends