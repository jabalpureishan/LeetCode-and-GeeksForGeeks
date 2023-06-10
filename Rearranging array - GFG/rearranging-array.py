#User function Template for python3

class Solution:    
    def Rearrange(self, a, n, answer):
        a.sort()
        loop = n//2
        answer.clear()
        for i in range(loop):
            answer.append(a[i])
            answer.append(a[-(i+1)])
        if n%2!=0:
            answer.append(a[(n-1)//2])
        #return answer[n:]
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        answer = [0 for x in range(n)]
        ob = Solution()
        ob.Rearrange(a, n, answer)
        print(*answer)

        T -= 1


if __name__ == "__main__":
    main()






# } Driver Code Ends