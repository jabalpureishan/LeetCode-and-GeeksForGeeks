#User function Template for python3

class Solution:
    def ExcelColumn(self, N):
        s = ""
        while(N>26):
            div = N%26
            if div==0:
                curr = "Z"
            else:
                curr = chr(64+N%26)
            s += curr
            if div==0:
                N = N//26 - 1
            else:
                N = N//26
        s += chr(64+N)
        return s[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob=Solution()
        print(ob.ExcelColumn(n))

# } Driver Code Ends