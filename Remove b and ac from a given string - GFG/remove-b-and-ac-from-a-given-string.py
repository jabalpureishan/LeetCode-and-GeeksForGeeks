#User function Template for python3

class Solution:
    def stringFilter(self, str):
        length = len(str)
        out = ""
        for i in range(length-1):
            #print("i:",i,"str[i]",str[i])
            if str[i]=="b":
                continue
            elif str[i]=="a" and str[i+1]=="c":
                continue
            elif str[i]=="c" and str[i-1]=="a":
                continue
            else:
                out += str[i]
                #print("out update:",out)
        if str[-2:]!="ac" and str[-1]!="b":
            out += str[-1]
        return out
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.stringFilter(s)
        print(ans)
# } Driver Code Ends