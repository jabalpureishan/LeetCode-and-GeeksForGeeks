#User function Template for python3

def max_sum(a,n):
    new = [a[-1]]
    new.extend(a)
    if n==1:
        return 0
    Sum = sum(a[:n-1])
    SLIndex = n - 1
    last = a[-1]
    s_last = a[-2]
    Initial = 0
    for i in range(n):
        Initial += i*a[i]
    Max = Initial
    for i in range(n-1):
        Initial -= last*(n-1)
        Initial += Sum
        if Initial>Max:
            Max = Initial
        Sum += last
        Sum -= s_last
        last = s_last
        SLIndex -= 1
        s_last = new[SLIndex]
    return Max


#{ 
 # Driver Code Starts
#Initial Template for Python 3


    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr,n))
# } Driver Code Ends