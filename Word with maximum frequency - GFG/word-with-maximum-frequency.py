#User function Template for python3
from collections import OrderedDict
def maximumFrequency (S) : 
    #Complete the function
    S = S.split(" ")
    d = {}
    d = OrderedDict()
    Max,word = 0,""
    for i in S:
        d[i] = d.get(i,0) + 1
    for i in d:
        if d.get(i)>Max:
            Max = d.get(i)
            word = i
    return word+" "+str(Max)




#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    S = input()
    
    print(maximumFrequency(S))




# } Driver Code Ends