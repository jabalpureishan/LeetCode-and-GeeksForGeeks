class Solution:
    def getMaxOccurringChar(self,s):
        D = {}
        for i in s:
            D[i] = D.get(i,0) + 1
        S = sorted(D.items(),key = lambda x : x[1],reverse = True)
        value = S[0][1]
        out = []
        for i in range(len(S)):
            if S[i][1]==value:
                out.append(S[i][0])
            else:
                break
        out.sort()
        return out[0]

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
        print(Solution().getMaxOccurringChar(s))
# } Driver Code Ends