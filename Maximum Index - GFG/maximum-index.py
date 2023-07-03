#User function Template for python3
class Solution:

	def maxIndexDiff(self,arr,n):
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
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends