class Solution:
    def search(self, patt, s):
        window = len(patt)
        length = len(s)
        slides = length - window + 1
        O = []
        for i in range(slides):
            if s[i:window]==patt :
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
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends