from collections import OrderedDict
class Solution:
	def FirstNonRepeating(self, A):
        d = OrderedDict()
        ans = ""
        for i in A:
            d[i] = d.get(i,0) +1 
            for i in d:
                if d[i]==1:
                    ans += i
                    break
            else:
                ans += "#"
        return ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends