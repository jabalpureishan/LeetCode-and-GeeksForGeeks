from collections import Counter
class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        Done =[]
        Output = []
        DA,DB,DC = {},{},{}
        for i in A:
            DA[i] = 0
        for i in B:
            DB[i] = 0
        for i in C:
            DC[i] = 0            
        for i in A:
            if i in DB:
                if i in DC:
                    if i not in Done:
                        Done.append(i)
                        Output.append(i)
        return Output
#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends