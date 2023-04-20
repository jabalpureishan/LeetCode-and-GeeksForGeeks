#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
		S=S.split(" ")
		out = ""
		for i in S:
		    out += i[0]
        return out


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.firstAlphabet(S)
		
		print(answer)


# } Driver Code Ends