#User function Template for python3


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        if len(p)>len(s):
            return -1
        d,left,Min,Minl,c = {},0,"##",float("inf"),{}
        for i in p:
            d[i] = 0
            c[i] = c.get(i,0) + 1
        def check(c,d):
            for i in d:
                if d[i]<c[i]:
                    return False
            return True
        #print("initial:",d)
        for right in range(len(s)):
            #print("curr:",s[right])
            if s[right] in d:
                #print("in d")
                d[s[right]] += 1
            #print("befor:",s[left:right+1])
            #print("before:",d)

            while(check(c,d)):
                #print("while chalu")
                if right-left+1<Minl:
                    Minl = right - left + 1
                    Min = s[left:right+1]
                if s[left] in d:
                    d[s[left]] -= 1
                left += 1


                

                
            #print("after:",s[left:right+1])
            
        if Min =="##":
            return -1
        return Min

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends