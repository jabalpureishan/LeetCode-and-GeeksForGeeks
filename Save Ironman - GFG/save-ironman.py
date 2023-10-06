#User function Template for python3

def saveIronman (s) : 
    ans = ""
    for i in s:
        if i.isalnum():
            ans += i.lower()
    return ans==ans[::-1]




#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    s = input()
    ans = saveIronman(s)
    if(ans == True):
        print("YES")
    else:
        print("NO")
# } Driver Code Ends