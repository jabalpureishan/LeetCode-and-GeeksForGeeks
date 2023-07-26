#User function Template for python3
class Solution:
	def sentencePalindrome(self, s):
        new = ""
        for i in s:
            if i.isalpha():
                new += i
        return new==new[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		if ob.sentencePalindrome (s):
			print (1)
		else:
			print (0)
# } Driver Code Ends