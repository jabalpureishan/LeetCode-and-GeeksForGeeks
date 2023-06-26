#User function Template for python3

class Solution:
    def maximizeArray(self, arr1, arr2, n):
        New = set(arr1+arr2)
        New = sorted(New,reverse=True)
        New = New[:n]
        New = set(New)
        out = []
        Done = set()
        for i in arr2:
            if i in New:
                if i not in Done:
                    out.append(i)
                    Done.add(i)
        for i in arr1:
            if i in New:
                if i not in Done:
                    out.append(i)
                    Done.add(i)
        return out


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maximizeArray(arr1, arr2, n)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1

# } Driver Code Ends