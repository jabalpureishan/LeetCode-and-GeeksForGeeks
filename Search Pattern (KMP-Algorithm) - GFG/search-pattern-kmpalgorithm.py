#User function Template for python3

class Solution:
    def search(self, pat, txt):
        window = len(pat)
        length = len(s)
        slides = length - window + 1
        O = []
        for i in range(slides):
            if s[i:window]==pat :
                O.append(i+1)
            window+=1
        if O==[]:
            return [-1]
        return O


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print(-1,end="")
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends