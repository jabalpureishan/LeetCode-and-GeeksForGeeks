#User function Template for python3

class Solution:
    def max_of_subarrays(self,arr,n,k):
        if k==1:
            return arr
        slides = n - k
        Max = max(arr[:k])
        output = [Max]
        window = k
        for j in range(slides):
            sub = arr[j]
            if sub==Max:
                Max = max(arr[j+1:window])
            Max = max(Max,arr[window])
            output.append(Max)
            window += 1
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends