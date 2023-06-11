#User function Template for python3


# function for adding one to number 
class Solution:
    def addOne(self,a, n):
        if a[-1]!=9:
            a[-1]+=1
            return a
        else:
            carry = 1
            for i in range(-1,-(n+1),-1):
                #print("A[i]",A[i])
                if a[i]+carry==10:
                    a[i] = 0
                else:
                    a[i] += carry
                    carry = 0
            if carry==1:
                a = [1] + a
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    def printAns(ans):
        for x in ans:
            print(x, end=" ");
        print()
    
    tc=int(input())
    while tc:
        n=int(input())
        a=list(map(int, input().strip().split()))
        ob = Solution()
        printAns(ob.addOne(a, n))
        tc=tc-1
# } Driver Code Ends