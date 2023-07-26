#User function Template for python3

class Solution:
    def reverse(self, s):
        letters=[]
        index=[]
        for i in range(0,len(s)):
            value=ord(s[i])
            if(value>=97):
                if(value<=122):
                    letters.append(s[i])
                    index.append(i)
            if(value>=65):
                if(value<=90):
                    letters.append(s[i])
                    index.append(i)
        #print("letters",letters)
        #print("index",index)
        letters.reverse()
        s=list(s)
        #print("list s",s)
        for j in range(0,len(letters)):
            s[index[j]]=letters[j]
        s="".join(s)
        
        return(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        ans = ob.reverse(s)
        print(ans)
# } Driver Code Ends