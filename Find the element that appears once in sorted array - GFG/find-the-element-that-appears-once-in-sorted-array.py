#User function Template for python3

class Solution:
    def findOnce(self,arr : list, n : int):
        D = {}
        for i in arr:
            D[i] = D.get(i,0) + 1
        for i in D:
            if D.get(i)==1 :
                return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))
# } Driver Code Ends