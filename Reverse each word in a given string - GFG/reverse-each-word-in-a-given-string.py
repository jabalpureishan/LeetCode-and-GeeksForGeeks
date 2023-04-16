#User function Template for python3

class Solution:
    def reverseWords(self, s):
        s += "."
        output = ""
        current = ""
        for i in s:
            if i==".":
                output += current[::-1] +"."
                current = ""
            else:
                current += i
        return output[:-1]
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver Code Ends