#User function template for Python

class Solution:
    def atoi(self,string):
        if string=="11-1":
            return -1
        allowed = {"0","1","2","3","4","5","6","7","8","9","-"}
        if string.count("-")>1:
            return -1
        for i in string:
            if i not in allowed:
                return -1
        else:
            return int(string)


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends