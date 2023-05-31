#User function Template for python3
class Solution: 
    def firstAndLast(self, arr, n, x): 
        first,last = None,None
        for i in range(n):
            if arr[i]==x:
                first = i
                break
        for i in range(-1,-(n+1),-1): 
            #print(i)
            if arr[i]==x:
                last = i
                break
        if first==None:
            return [-1]
        return [first,last+n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input()) 
    for _ in range(t):
        n,x = [int(i) for i in input().split()] 
        arr = [int(i) for i in input().split()] 
        ob=Solution() 
        ans=ob.firstAndLast(arr,n,x) 
        s=(" ").join(map(str,ans))
        print(s)

# } Driver Code Ends