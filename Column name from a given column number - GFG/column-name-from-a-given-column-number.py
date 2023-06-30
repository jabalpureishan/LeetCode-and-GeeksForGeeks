#User function Template for python3

class Solution:
    def colName (self, n):
        s = ""
        while(n>26):
            div = n%26
            if div==0:
                curr = "Z"
            else:
                curr = chr(64+n%26)
            s += curr
            if div==0:
                n = n//26 - 1
            else:
                n = n//26
        s += chr(64+n)
        return s[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends