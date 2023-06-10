#User function Template for python3



class Solution:
    def arranged(self,a,n):
        pos,neg = [],[]
        for i in a:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        a.clear()
        for i in range(len(pos)):
            a.extend([pos[i],neg[i]])
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=Solution().arranged(a,n)
    print(*ans)

# } Driver Code Ends