#User function Template for python3
class Solution:
	def printString(self, S, ch, count):
	    if count==0:
	       return S
        length = len(S)
        ind = 0
        while(count>0 and ind<length):
            if S[ind]==ch:
                count -= 1
            if count==0:
                if ind==length-1:
                    return "Empty string"
                return S[ind+1:]
            ind +=1
        return "Empty string"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ch = input()[0]
		count = int(input())
		ob = Solution()	
		answer = ob.printString(s,ch,count)
		
		print(answer)


# } Driver Code Ends