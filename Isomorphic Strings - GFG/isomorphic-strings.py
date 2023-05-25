#User function Template for python3

class Solution:
    def areIsomorphic(self,str1,str2):
        D = {}
        l1 = len(str1)
        l2 = len(str2)
        Done = set()
        if l1!=l2:
            return False
        for i in range(l1):
            first = str1[i]
            second = str2[i]
            if first not in D:
                if second in Done:
                    return False
                else:
                    Done.add(second)
                D[first] = second
            else:
                if second!=D.get(first):
                    return False
        return True



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

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
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends