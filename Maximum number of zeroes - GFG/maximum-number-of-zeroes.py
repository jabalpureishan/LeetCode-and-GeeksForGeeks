# User Template code

def MaxZero(arr, n):
        Max = 0
        ele = 0
        for i in arr:
            count = str(i).count("0")
            if count>Max:
                Max = count
                ele = i
            elif count==Max:
                ele = max(ele,i)
        if Max==0:
            return -1
        return ele


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a=list(map(int,input().split()))
        print(MaxZero(a,n))
# } Driver Code Ends