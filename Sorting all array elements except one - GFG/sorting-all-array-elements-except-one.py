#User function Template for python3

def sortExceptK (arr, n, k) : 
        rem = arr.pop(k)
        new = sorted(arr)
        new.insert(k,rem)
        for i in new:
            print(i,end=" ")
        return ""



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = sortExceptK(arr, n, k)
    print(ans)




# } Driver Code Ends