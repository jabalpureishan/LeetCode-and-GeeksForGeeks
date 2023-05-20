#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def countSubstring(self, S): 
        total = 0
        length = len(S)
        for i in range(2,length+1):
            window = i
            slides = length - window
            lower = 0
            upper = 0
            for j in range(i):
                if S[j].islower():
                    lower += 1
                else:
                    upper += 1
            if upper==lower:
                total += 1
            for j in range(slides):
                if S[j].islower():
                    lower -= 1
                else:
                    upper -= 1
                if S[window].islower():
                    lower += 1
                else:
                    upper += 1
                if upper==lower:
                    total += 1
                window += 1
        return total

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countSubstring(S)
        print(ans)

# } Driver Code Ends