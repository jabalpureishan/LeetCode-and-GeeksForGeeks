#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):
        paisa = {}
        for i in bills:
            if i==5:
                paisa[i] = paisa.get(i,0) + 1
            elif i==10:
                if paisa.get(5,0)>=1:
                    paisa[5] -= 1
                    paisa[10] = paisa.get(10,0) + 1
                else:
                    return False
            elif i==20:
                if((paisa.get(10,0)>=1) and (paisa.get(5,0)>=1)):
                    paisa[5] -= 1
                    paisa[10] -= 1
                    paisa[20] = paisa.get(20,0) + 1
                elif paisa.get(5,0)>=3 :
                    paisa[5] -= 3
                    paisa[20] = paisa.get(20,0) + 1
                else:
                    return False
        return True

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends