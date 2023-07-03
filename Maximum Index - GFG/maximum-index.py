#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,A, N): 
        arr = A
        n = N
        d = {}
        for i in range(n):
            if arr[i] in d:
                d[arr[i]].append(i)
            else:
                d[arr[i]] = [i]
        arr.sort()
        Diff = 0
        Min = n
        for i in arr:
            Min = min(d[i][0],Min)
            Diff = max(Diff,d[i][-1]-Min)
        return Diff


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends