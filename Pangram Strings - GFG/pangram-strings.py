#User function Template for python3
class Solution:
	def isPanagram(self, S):
        S = S.lower()
        alpha = set()
        count = 0
        for i in S:
            if i.isalpha():
                alpha.add(i)

        if len(alpha)==26:
            return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPanagram(S)
		print(answer)

# } Driver Code Ends