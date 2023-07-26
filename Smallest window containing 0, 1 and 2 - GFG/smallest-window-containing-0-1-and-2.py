#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        left,Min,hashmap = 0,float("inf"),{"0":0,"1":0,"2":0}
        for right in range(len(S)):
            if S[right] in hashmap:
                hashmap[S[right]] += 1
            while(hashmap["0"]>0 and hashmap["1"]>0 and hashmap["2"]>0):
                if hashmap["0"]>0 and hashmap["1"]>0 and hashmap["2"]>0 :
                    Min = min(Min,right - left + 1)
                hashmap[S[left]] -= 1
                left += 1
        if Min==float("inf"):
            return -1
        return Min


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends