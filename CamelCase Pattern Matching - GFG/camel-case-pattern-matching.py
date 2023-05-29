#User function Template for python3

class Solution:
    def CamelCase(self,N,Dictionary,Pattern):
        #print(Pattern)
        lp = len(Pattern)
        out = []
        for i in Dictionary:
            curr = ""
            for j in i:
                if j.isupper():
                    curr += j
            #print(curr)
            lc = len(curr)
            #if lc<=lp:
                #if curr in Pattern:
                    #out.append(i)
            #else:
            if Pattern==curr[:lp]:
                out.append(i)
        out.sort()
        if len(out)==0:
            return [-1]
        return out


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends