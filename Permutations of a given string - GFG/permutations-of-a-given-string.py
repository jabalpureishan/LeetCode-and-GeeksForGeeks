#User function Template for python3
from itertools import permutations
class Solution:
    def find_permutation(self, S):
        P = permutations(S)
        Output = []
        for i in P:
            Ans = "".join(i)
            Output.append(Ans)
        Output = list(set(Output))
        Output.sort()
        return Output 
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends