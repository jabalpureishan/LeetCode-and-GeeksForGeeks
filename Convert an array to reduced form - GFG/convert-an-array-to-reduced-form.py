
class Solution:
	def convert(self,arr, n):
		new = arr[:]
		out = arr[:]
		new.sort()
		D = {}
		Index = 0
		for i in new:
		    D[i] = Index
		    Index += 1
		arr.clear()
		for i in out:
		    arr.append(D.get(i))
		

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends