#User function Template for python3

class Solution:
    def ExcelColumnNumber(self, s):
        power = 0
        s = s[::-1]
        final = 0
        for i in s:
            final += (ord(i)-64)*(26**(power))
            power += 1
        return final


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        s=input()
        ob=Solution()
        print(ob.ExcelColumnNumber(s))
# } Driver Code Ends