#User function Template for python3
class Solution:

	
	def search(self,pat, txt):
	    text = txt
        window = count = 0
        dp = {}
        for i in pat:
            window += 1
            dp[i] = dp.get(i,0) + 1
        #print("dp:",dp)
        slides = len(text) - window
        dt = {}
        for i in range(window):
            dt[text[i]] = dt.get(text[i],0) + 1
        #print("dt:",dt)
        if dt==dp:
            count += 1
        for i in range(slides):
            dt[text[window]] = dt.get(text[window],0) + 1
            dt[text[i]] -= 1
            if dt[text[i]]==0:
                dt.pop(text[i])
            #print("dt:",dt)
            window += 1
            if dt==dp:
                count += 1
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends