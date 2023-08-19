#User function Template for python3

def Max_Sum(arr,n,k):
    arr.sort()
    left,right,Max,ans = 0,n-1,0,[0,0]
    while(left<right):
        Sum = arr[left] + arr[right]
        if Sum<k:
            if Sum>Max:
                Max = Sum
                ans = [arr[left],arr[right]]
            left += 1
        else:
            right -= 1
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n,k=[int(x) for x in input().split()]
        arr=[int(x) for x in input().split()]
        ans=Max_Sum(arr,n,k)
        print(ans[0],ans[1])
# } Driver Code Ends