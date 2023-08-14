#User function Template for python3

class Solution:
	def singleNumber(self, nums):
        d,ans = {},[]
        for i in nums:
            d[i] = d.get(i,0) + 1
        for i in d:
            if d[i]==1:
                ans.append(i)
        return sorted(ans)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends