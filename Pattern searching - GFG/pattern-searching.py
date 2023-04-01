#User function Template for python3

def searchPattern(st, pat):
	    window = len(pat)
	    length = len(st)
	    slides = length - window + 1
	    for i in range(slides):
	        if st[i:window]==pat:
	            return True
            window+=1
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for i in range(t):
    st=input()
    pat=input()
    if (searchPattern(st, pat)):
        print("Present")
    else:
        print("Not present")
# } Driver Code Ends