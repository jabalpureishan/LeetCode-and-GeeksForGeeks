#User function Template for python3
class Solution:
	def search(self, text, pat):
	    window = len(pat)
	    length = len(text)
	    slides = length - window + 1
	    for i in range(slides):
	        if text[i:window]==pat:
	            return 1
            window+=1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		text,pat = input().split()
		ob = Solution()
		answer = ob.search(text,pat)
		print(answer)


# } Driver Code Ends