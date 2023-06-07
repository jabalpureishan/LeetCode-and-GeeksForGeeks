#User function Template for python3
class Solution:
	def countSubstr(self, S):
	    if S=="0":
	       return 0
        C = S.count("1",S.index("1")+1,len(S))
        return (C*(C+1))//2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		print (ob.countSubstr (s))

	# Contributed By: Pranay Bansal
# } Driver Code Ends