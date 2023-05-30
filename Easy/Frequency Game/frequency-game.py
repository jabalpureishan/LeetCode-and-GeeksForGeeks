#User function Template for python3


def LargButMinFreq(arr,n):
    d = dict()
    for i in arr:
        d[i] = d.get(i,0) + 1
    minfreq = float("inf")
    for i in d.values():
        minfreq = min(minfreq,i)
    maxele = -1
    for i in d:
        if d[i]==minfreq:
            maxele = max(maxele,i)
    return maxele


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends