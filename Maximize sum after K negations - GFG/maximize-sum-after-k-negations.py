#User function Template for python3
from heapq import heapify,heapreplace
class Solution:
    def maximizeSum(self, a, n, k):
        heapify(a)
        for i in range(k):
            insert = -a[0]
            heapreplace(a,insert)
        return sum(a)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maximizeSum(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends