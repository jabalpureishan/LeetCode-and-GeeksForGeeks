#User function Template for python3

class Solution:
    def setSetBit(self, x, y, l, r):
        x = bin(x)
        y = bin(y)
        x = str(x)[2:]
        y = str(y)[2:]
        x = x[::-1]
        y = y[::-1]
        if r>len(y):
            y += "0"*(r-len(y)+1)
        if r>len(x):
            x += "0"*(r-len(x)+1)
        #print("x:",x,"y:",y)
        ans = ""
        for i in range(l-1,r):
            ans += str(int(x[i])|int(y[i]))
        #print("ans:",ans)
        ans = x[:l-1] + ans + x[r:]
        ans = ans[::-1]
        #print("ans:",ans)
        ans = int(ans,2)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        x = int(arr[0])
        y = int(arr[1])
        l = int(arr[2])
        r = int(arr[3])
        
        ob = Solution()
        print(ob.setSetBit(x, y, l, r))
# } Driver Code Ends